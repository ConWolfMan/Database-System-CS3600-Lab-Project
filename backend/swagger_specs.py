"""
Centralised Swagger/OpenAPI definitions and operation specs.
- DEFINITIONS: model schemas, loaded into the global Swagger template in app.py
- ACTORS/MOVIES/DIRECTORS/EDGES/GRAPHS: per-route specs used via @swag_from
"""

# ---------------------------------------------------------------------------
# Model definitions
# ---------------------------------------------------------------------------

DEFINITIONS = {
    "GetContacts": {
        "type": "object",
        "properties": {
            "Name": {"type": "string"},
            "Phone": {"type": "string"},
            "City": {"type": "string"},
            "State": {"type": "string"},
            "Address": {"type": "string"},
        },
    }
}
