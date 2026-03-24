from database import get_db_connection

contacts = [
    ('Alice Johnson',  '208-555-0101', 'Moscow',  'ID', '123 Main St'),
    ('Bob Smith',      '208-555-0102', 'Boise',   'ID', '456 Oak Ave'),
    ('Carol Williams', '509-555-0201', 'Spokane', 'WA', '789 Pine Rd'),
    ('Dave Brown',     '406-555-0301', 'Missoula','MT', None),
]

conn = get_db_connection()
try:
    with conn.cursor() as cursor:
        cursor.executemany(
            "INSERT INTO Contacts (Name, PhoneNumber, City, State, Address) VALUES (%s, %s, %s, %s, %s)",
            contacts
        )
    conn.commit()
    print(f"Inserted {len(contacts)} contacts.")
finally:
    conn.close()