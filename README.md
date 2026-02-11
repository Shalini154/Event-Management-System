# Event Management System

## Overview
The **Event Management System (EMS)** is a **Django-based web application** designed to simplify event planning, resource booking, and management. It provides modules for user management, event resources, reports, and transactions, making event coordination seamless and organized.

---

## Features
- **User & Admin Management:** Create, update, and manage users with different roles.
- **Event Booking:** Book resources for events and check availability.
- **Reports & Transactions:** Generate event reports and track payments.
- **Form Validation & UI:** Includes HTML forms with validation, radio buttons, checkboxes, and password masking.
- **Responsive Design:** Built with HTML & CSS for a clean and user-friendly interface.

---

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default Django DB)

---

## Screenshots

<img width="1832" height="931" alt="Screenshot 2026-02-11 194546" src="https://github.com/user-attachments/assets/93653f01-c800-475a-a9ad-8ef0c91122c2" />


## How to Run Locally (Quick Version)

```bash
# 1. Clone repository
git clone https://github.com/Shalini154/Event-Management-System.git
cd Event-Management-System

# 2. Create & activate virtual environment
python -m venv env
# Windows
env\Scripts\activate
# Linux / Mac
source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations & run server
python manage.py migrate
python manage.py runserver

5. Open in browser
http://127.0.0.1:8000/
