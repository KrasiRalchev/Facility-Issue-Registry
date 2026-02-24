# Facility Issue Registry

**Facility Issue Registry** is a web application built with **Django**, designed to register, manage, and track issues in buildings and facilities of an airport or enterprise. The project demonstrates core Django concepts: models, forms, views, templates, CRUD functionality, and Bootstrap-based UI design.

---

## 🛠 Key Features

- **Facility Management**  
  - Create, edit, delete, and view facility details  
  - Upload facility images  
  - Dashboard showing summary of issues per unit  

- **Issue Management**  
  - Create, edit, delete, and view issues  
  - Statuses: Open, In Progress, Resolved, Closed  
  - Image attachments for issues  
  - Linked to a specific facility and filterable by status  

- **Maintenance Actions**  
  - Create actions for a given issue  
  - Resolve actions and mark the issue as **Resolved**  
  - Forms with partially disabled fields for data protection  

- **Dashboard & Reports**  
  - View counts of open, in progress, and resolved issues per unit  
  - Lists of issues with filtering by status or unit  

- **Template Features**  
  - Base template and template inheritance  
  - Navbar and footer included on all pages  
  - Bootstrap styling  
  - Custom template tags for counting open issues and total facilities  
  - Custom 404 error page  

---

## 📦 Technologies

- Python 3.11  
- Django 5.2+  
- PostgreSQL 
- Bootstrap 5  
- Git for version control  

---

## 🗂 Project Structure

The project consists of three Django apps:

1. **facilities**  
   - Models: `Unit`, `Facility`  
   - CRUD operations and dashboard  

2. **issues**  
   - Models: `Issue`,  `Tag` 
   - Statuses, priorities, facility relations  
   - Create, edit, and delete issues  

3. **maintenance**  
   - Model: `MaintenanceAction`  
   - Link actions to issues  
   - Forms for creating and resolving actions  

---

## 📝 Installation and Running

1. **Clone the repository:**
   ```bash
   git clone git clone https://github.com/KrasiRalchev/Facility-Issue-Registry.git
   cd facility_issue_registry
   
2. **Create a virtual environment and install dependencies**
python -m venv venv
source venv/bin/activate      # Linux / MacOS
venv\Scripts\activate         # Windows
pip install -r requirements.txt

3. **Configure sensitive data via .env**
All sensitive information such as Django SECRET_KEY and database credentials must be stored in a .env file in the root folder (same level as manage.py).

Example .env:

SECRET_KEY=your_secure_django_secret_key
DB_USER=your_db_user
DB_PASSWORD=your_db_password

Important:

.env is ignored in Git via .gitignore

Never commit .env to GitHub

4. **Modify settings.py to read from .env**
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "facility_issue_registry_db",
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

5. **Apply migrations**
python manage.py makemigrations
python manage.py migrate

6. **Run the server**
python manage.py runserver

7. **Access the application**
Open http://127.0.0.1:8000/ in your browser.

---

**Navigation**

Facility Dashboard: /

Facility List: /facilities/

Create Facility: /facilities/create/

Facility Detail / Edit / Delete: /facilities/<id>/, /edit/, /delete/

Issues List: /issues/

Create Issue: /issues/create/

Issue Detail / Edit / Delete: /issues/<id>/, /edit/, /delete/

Maintenance Actions: /maintenance/<issue_id>/create/, /resolve/


**Features**

Full CRUD functionality for Facilities and Issues

Maintenance actions linked to issues

Status and priority indicators for issues

Dynamic templates displaying database data

Filter issues by status

Confirmation step for deletions

Disabled/read-only fields where appropriate

Custom template tags showing the number of open issues and total facilities

Bootstrap-based responsive design

Custom 404 page
