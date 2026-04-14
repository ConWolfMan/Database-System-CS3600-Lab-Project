import re

from flask import Blueprint, jsonify, request
from pymysql.err import IntegrityError

from database import get_db_connection

contacts_bp = Blueprint("contacts", __name__)

_PHONE_RE = re.compile(r'^[\d\s\-\(\)\+\.]{7,50}$')


def _validate_phone(phone: str) -> bool:
    return bool(_PHONE_RE.match(phone))


# ---------------------------------------------------------------------------
# GET /api/contacts
# ---------------------------------------------------------------------------
@contacts_bp.route("/api/contacts", methods=["GET"])
def get_contacts():
    """
    List all contacts, with optional search filters.
    ---
    tags:
      - Contacts
    parameters:
      - name: name
        in: query
        type: string
        description: Filter by name (partial, case-insensitive)
      - name: phone
        in: query
        type: string
        description: Filter by phone number (partial match)
      - name: city
        in: query
        type: string
        description: Filter by city (partial, case-insensitive)
      - name: state
        in: query
        type: string
        description: Filter by state (exact, case-insensitive)
    responses:
      200:
        description: Array of contacts
        schema:
          type: array
          items:
            $ref: '#/definitions/Contact'
    """
    name  = request.args.get("name",  "").strip()
    phone = request.args.get("phone", "").strip()
    city  = request.args.get("city",  "").strip()
    state = request.args.get("state", "").strip()

    query  = "SELECT Name, PhoneNumber, City, State, Address FROM Contacts WHERE 1=1"
    params = []

    if name:
        query += " AND Name LIKE %s"
        params.append(f"%{name}%")
    if phone:
        query += " AND PhoneNumber LIKE %s"
        params.append(f"%{phone}%")
    if city:
        query += " AND City LIKE %s"
        params.append(f"%{city}%")
    if state:
        query += " AND State = %s"
        params.append(state)

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            results = cursor.fetchall()
        return jsonify(results), 200
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# GET /api/contacts/<phone_number>
# ---------------------------------------------------------------------------
@contacts_bp.route("/api/contacts/<string:phone_number>", methods=["GET"])
def get_contact(phone_number):
    """
    Get a single contact by phone number.
    ---
    tags:
      - Contacts
    parameters:
      - name: phone_number
        in: path
        type: string
        required: true
        description: The contact's primary phone number
    responses:
      200:
        description: Contact found
        schema:
          $ref: '#/definitions/Contact'
      404:
        description: Contact not found
        schema:
          $ref: '#/definitions/Error'
    """
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT Name, PhoneNumber, City, State, Address FROM Contacts WHERE PhoneNumber = %s",
                (phone_number,),
            )
            result = cursor.fetchone()
        if result is None:
            return jsonify({"error": "Contact not found"}), 404
        return jsonify(result), 200
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# POST /api/contacts
# ---------------------------------------------------------------------------
@contacts_bp.route("/api/contacts", methods=["POST"])
def create_contact():
    """
    Create a new contact.
    ---
    tags:
      - Contacts
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ContactInput'
    responses:
      201:
        description: Contact created
        schema:
          $ref: '#/definitions/Contact'
      400:
        description: Validation error
        schema:
          $ref: '#/definitions/Error'
      409:
        description: Phone number already exists
        schema:
          $ref: '#/definitions/Error'
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    name    = (data.get("Name")        or "").strip()
    phone   = (data.get("PhoneNumber") or "").strip()
    city    = (data.get("City")        or "").strip() or None
    state   = (data.get("State")       or "").strip() or None
    address = (data.get("Address")     or "").strip() or None

    if not name:
        return jsonify({"error": "Name is required"}), 400
    if not phone:
        return jsonify({"error": "PhoneNumber is required"}), 400
    if not _validate_phone(phone):
        return jsonify({"error": "Invalid phone number format"}), 400

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO Contacts (Name, PhoneNumber, City, State, Address) VALUES (%s, %s, %s, %s, %s)",
                    (name, phone, city, state, address),
                )
                conn.commit()
            except IntegrityError:
                return jsonify({"error": "Phone number already exists"}), 409
        return jsonify({
            "Name": name, "PhoneNumber": phone,
            "City": city, "State": state, "Address": address,
        }), 201
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# PUT /api/contacts/<phone_number>
# ---------------------------------------------------------------------------
@contacts_bp.route("/api/contacts/<string:phone_number>", methods=["PUT"])
def update_contact(phone_number):
    """
    Update an existing contact's details (phone number cannot be changed).
    ---
    tags:
      - Contacts
    parameters:
      - name: phone_number
        in: path
        type: string
        required: true
        description: The contact's primary phone number
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ContactUpdateInput'
    responses:
      200:
        description: Updated contact
        schema:
          $ref: '#/definitions/Contact'
      400:
        description: Validation error
        schema:
          $ref: '#/definitions/Error'
      404:
        description: Contact not found
        schema:
          $ref: '#/definitions/Error'
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # Only allow whitelisted fields so field names never reach raw SQL
    fields = {}
    if "Name" in data:
        name = (data["Name"] or "").strip()
        if not name:
            return jsonify({"error": "Name cannot be empty"}), 400
        fields["Name"] = name
    if "City" in data:
        fields["City"] = (data["City"] or "").strip() or None
    if "State" in data:
        fields["State"] = (data["State"] or "").strip() or None
    if "Address" in data:
        fields["Address"] = (data["Address"] or "").strip() or None

    if not fields:
        return jsonify({"error": "No updatable fields provided (allowed: Name, City, State, Address)"}), 400

    set_clause = ", ".join(f"{col} = %s" for col in fields)
    values     = list(fields.values()) + [phone_number]

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                f"UPDATE Contacts SET {set_clause} WHERE PhoneNumber = %s",
                values,
            )
            conn.commit()
            if cursor.rowcount == 0:
                return jsonify({"error": "Contact not found"}), 404
            cursor.execute(
                "SELECT Name, PhoneNumber, City, State, Address FROM Contacts WHERE PhoneNumber = %s",
                (phone_number,),
            )
            result = cursor.fetchone()
        return jsonify(result), 200
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# DELETE /api/contacts/<phone_number>
# ---------------------------------------------------------------------------
@contacts_bp.route("/api/contacts/<string:phone_number>", methods=["DELETE"])
def delete_contact(phone_number):
    """
    Delete a contact by phone number.
    ---
    tags:
      - Contacts
    parameters:
      - name: phone_number
        in: path
        type: string
        required: true
        description: The contact's primary phone number
    responses:
      200:
        description: Contact deleted
        schema:
          $ref: '#/definitions/Message'
      404:
        description: Contact not found
        schema:
          $ref: '#/definitions/Error'
    """
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM Contacts WHERE PhoneNumber = %s",
                (phone_number,),
            )
            conn.commit()
            if cursor.rowcount == 0:
                return jsonify({"error": "Contact not found"}), 404
        return jsonify({"message": "Contact deleted successfully"}), 200
    finally:
        conn.close()