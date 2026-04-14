"""
Centralised Swagger/OpenAPI definitions and operation specs.
- DEFINITIONS: model schemas, loaded into the global Swagger template in app.py
"""

# ---------------------------------------------------------------------------
# Model definitions
# ---------------------------------------------------------------------------

DEFINITIONS = {
    "Contact": {
        "type": "object",
        "properties": {
            "Name":        {"type": "string", "example": "Jane Smith"},
            "PhoneNumber": {"type": "string", "example": "555-123-4567"},
            "City":        {"type": "string", "example": "Atlanta"},
            "State":       {"type": "string", "example": "GA"},
            "Address":     {"type": "string", "example": "123 Main St"},
        },
    },
    "ContactInput": {
        "type": "object",
        "required": ["Name", "PhoneNumber"],
        "properties": {
            "Name":        {"type": "string", "example": "Jane Smith"},
            "PhoneNumber": {"type": "string", "example": "555-123-4567"},
            "City":        {"type": "string", "example": "Atlanta"},
            "State":       {"type": "string", "example": "GA"},
            "Address":     {"type": "string", "example": "123 Main St"},
        },
    },
    "ContactUpdateInput": {
        "type": "object",
        "properties": {
            "Name":    {"type": "string", "example": "Jane Smith"},
            "City":    {"type": "string", "example": "Atlanta"},
            "State":   {"type": "string", "example": "GA"},
            "Address": {"type": "string", "example": "123 Main St"},
        },
    },
    "Error": {
        "type": "object",
        "properties": {
            "error": {"type": "string", "example": "Contact not found"},
        },
    },
    "Message": {
        "type": "object",
        "properties": {
            "message": {"type": "string", "example": "Contact deleted successfully"},
        },
    },
}

