# Student Management System - Documentation

## 1. Title of Application And Group Member Details
- **Title**: Student Management System
- **Group Members**:
    1. [Name 1] (Enrollment No: [No 1])
    2. [Name 2] (Enrollment No: [No 2])
    3. [Name 3] (Enrollment No: [No 3])
    4. [Name 4] (Enrollment No: [No 4])

## 2. Problem Definition
Institutions often struggle to manage student records efficiently using paper-based processes or decentralized spreadsheets. 
This project builds a responsive web application to securely organize this information into an easily accessible digital solution.

## 3. Objective of Application
- To digitize and centralize student records.
- To provide a modern web interface for robust CRUD operations.
- To utilize an advanced web framework (Django) for secure data-handling and UI delivery.

## 4. Key Features of Application
- Comprehensive Student Directory with Enrollment NO, Name, Email, and Division.
- CRUD functionality via user-friendly modern forms.
- Dynamic MVT routing with clean URL endpoints.
- High-aesthetic dashboard presenting live database statistics.
- Strict data validation and constraint handling via Django Forms.

## 5. System Architecture diagram
(Insert System Architecture Diagram Here)
*(Structure: HTTP Web Client -> Django URL Routes -> Django Views/Forms -> Django ORM -> SQLite Database)*

## 6. Django Modules and functionalities used
- Django Projects and Apps logic (`student_management`, `students`).
- Django ORM mapping to SQLite (`views.py` utilizing `.all()`, `.save()`, `.delete()`).
- Explicit HTTP methods (GET/POST) handling in Function-Based Views (`student_list`, `student_create`, `student_update`, `student_delete`).
- `django.forms` for client and server side validation (e.g., alphanumeric check for enrollment).
- Django Template inheritance and routing logic paired with styling tags (`base.html`).
- Sub-app URL encapsulation mapping root paths back to `students/urls.py`.

## 7. Odoo Modules and functionalities used
*(Odoo module skipped for this specific Django-focused iteration of the project)*

## 8. Application Screenshots
1. **Django: Student Dashboard View** (Insert screenshot)
2. **Django: Add Student Form View** (Insert screenshot)
3. **Django: Edit Student Form View** (Insert screenshot)
4. **Django: Delete Student Warning Prompt** (Insert screenshot)
5. **Django: Custom Error Handling/Validation Alert** (Insert screenshot)
6. **Django: Dynamic Success Toast Alert** (Insert screenshot)

## 9. Tools & Technologies Used
- Python 3
- Django 6.0
- SQLite Database
- Web Tech: HTML5, CSS3, JavaScript
- Bootstrap 5 & FontAwesome (UI Design)

## 10. Learning Outcomes
This project provided hands-on experience in full-stack web development, learning how to:
- Build robust and secure web applications using Django.
- Configure and compartmentalize Django views, URLs, models, and forms correctly.
- Integrate visually-stunning modern web-design safely via Template Inheritance.
- Understand and utilize Object Relational Maping (ORM) commands to sidestep manual raw SQL requests.

## 11. Conclusion
The Student Management System successfully fulfills the objectives of centralizing student records, combining beautiful, dynamic presentation capabilities with a highly secure relational database.
