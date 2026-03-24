from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from database import get_db_connection
from swagger_specs import DEFINITIONS
from contacts import contacts_bp

app = Flask(__name__)
CORS(app)

Swagger(
    app,
    template={
        "info": {
            "title": "Online Phone Book",
            "description": "Online Phone Book Database REST API",
            "version": "1.0.0",
        },
        "definitions": DEFINITIONS,
    },
)

app.register_blueprint(contacts_bp)


@app.route("/api/health")
def health():
    return {"status": "ok"}


@app.route("/api/db-check")
def db_check():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        return {"db": "connected", "result": result}
    finally:
        conn.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)