# Database-System-CS3600-Lab-Project
This is a repository for a group assignment for a University Course

## Project Goal
Create a online phone book that stores information such as (person, phone number, business). Users can search for businesses, numbers, or people and get data back

## Access
**Home Page** http://localhost/Database-System-CS3600-Lab-Project/
**API DOCS** `http://127.0.0.1:5000/apidocs`.

## Getting Started

**Prerequisites:** Python 3.x and XAMPP installed.

**1. Clone the repo**
```powershell
git clone <repo-url>
cd Database-System-CS3600-Lab-Project
```

**2. Install Python dependencies**
```powershell
cd backend
pip install -r requirements.txt
```

**3. Start XAMPP**
- Open the XAMPP Control Panel
- Start **Apache** and **MySQL**

**4. Create the database**
- Go to `http://localhost/phpmyadmin`
- Create a new database named `phonebook`
- Click the **SQL** tab, paste in the contents of `database/schema.sql`, and click **Go**

**5. Run the Flask app**
```powershell
cd backend
python app.py
```

**6. Verify it's working**
```powershell
irm http://127.0.0.1:5000/api/health    # should return: ok
irm http://127.0.0.1:5000/api/db-check  # should return: db connected
irm http://127.0.0.1:5000/api/contacts  # should return: []
```

