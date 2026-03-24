from flask import Blueprint, jsonify
from database import get_db_connection

contacts_bp = Blueprint("contacts", __name__)

@contacts_bp.route("/api/contacts", methods=["GET"])
def get_contacts():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT Name, PhoneNumber, City, State, Address FROM Contacts")
            results = cursor.fetchall()
        return jsonify(results)
    finally:
        conn.close()