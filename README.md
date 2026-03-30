# 🎓 Student Management System

![Python](https://img.shields.io/badge/Python-3-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?style=flat-square&logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=flat-square&logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=flat-square&logo=bootstrap)

A responsive, responsive, high-aesthetic web application built with **Django** to securely manage and organize student records. It digitizes paper-based processes into a centralized, easy-to-use digital dashboard with complete **CRUD** capabilities.

---

## 🚀 Key Features

* **Comprehensive Directory:** Track Student Enrollment No, Name, Email, and Division.
* **Full CRUD Functionality:** Create, Read, Update, and Delete student records with ease.
* **Dynamic Dashboard:** A visually-stunning modern layout presenting live database statistics.
* **Robust Validation:** Strict server-side and client-side data validation via Django Forms (e.g., alphanumeric checks for enrollment).
* **High Aesthetics:** Styled with modern CSS, UI components, custom error alerts, and success toasts.
* **Odoo Integration (Optional):** Foundation files structured to support Odoo ORM integration.

---

## 🛠️ Tools & Technologies Used

* **Backend:** Python 3, Django 6.0
* **Database:** SQLite3 (via Django ORM)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **UI/UX Design:** Bootstrap 5, FontAwesome Icons

---

## ⚙️ Installation & Setup (Local Development)

Follow these steps to run the application locally on your machine.

**1. Clone the repository:**
```bash
git clone https://github.com/khushal3706/Student_Management_System_Django.git
cd Student_Management_System_Django
```

**2. Create and activate a Virtual Environment (Windows):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**3. Install Dependencies:**
If you don't have Django installed in your environment yet, install it via pip:
```bash
pip install django
```

**4. Navigate to the project directory and Apply Migrations:**
```bash
cd student_management
python manage.py makemigrations
python manage.py migrate
```

**5. Start the Development Server:**
```bash
python manage.py runserver
```

**6. Access the Application:**
Open your web browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📂 Project Architecture

This application strictly follows Django's **MVT** (Model-View-Template) architecture. 

* **Models:** Object Relational Mapping (ORM) to handle the SQLite database layer (`students/models.py`).
* **Views:** Explicit HTTP Method (GET/POST) handling using Function-Based Views (`students/views.py`).
* **Templates:** Reusing UI code effectively via Django Template Inheritance logic (`templates/base.html`).

---

## 🎓 Learning Outcomes

Developed as an academic/group project to gain hands-on full-stack development experience. Key takeaways include:
* Understanding HTTP request cycles and explicit routing.
* Preventing raw SQL injections by mastering the Django ORM.
* Compartmentalizing code safely using Django Sub-Apps.
* Implementing strict UI boundaries with modern CSS libraries.

---
*Created by Khushal3706 and Team.*
