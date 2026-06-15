# Employee Management System

## Project Overview

Employee Management System is a CRUD (Create, Read, Update, Delete) web application developed using Flask and SQLite. The application allows users to manage employee records efficiently through a simple and user-friendly interface.

---

## Features

### Create Employee

* Add new employee records
* Store employee information in the database

### Read Employee Data

* Display all employee records in a structured table
* View employee details instantly

### Update Employee

* Edit existing employee information
* Save updated records to the database

### Delete Employee

* Remove employee records
* Confirmation prompt before deletion

### Search Employee

* Search employees dynamically
* Filter records instantly

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python Flask

### Database

* SQLite

---

## Project Structure

```text
employee-management-system/

├── app.py
├── employees.db
├── requirements.txt

├── templates/
│   ├── index.html
│   └── edit.html

├── static/
│   ├── style.css
│   └── script.js

├── screenshots/

└── README.md
```

---

## Database Schema

### Employees Table

| Field      | Type                              |
| ---------- | --------------------------------- |
| id         | INTEGER PRIMARY KEY AUTOINCREMENT |
| name       | TEXT                              |
| department | TEXT                              |
| role       | TEXT                              |
| salary     | REAL                              |
| join_date  | TEXT                              |

---

## Installation

### Clone Repository

```bash
git clone <repository-link>
```

### Navigate to Project Folder

```bash
cd employee-management-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Screenshots

### Home Page

Add screenshot here

### Add Employee

Add screenshot here

### Employee List

Add screenshot here

### Edit Employee

Add screenshot here

### Delete Employee

Add screenshot here

### Search Employee

Add screenshot here

---

## Learning Outcomes

* Flask Application Development
* CRUD Operations
* Database Integration
* SQLite Database Management
* Frontend and Backend Integration
* Form Handling
* Responsive User Interface Design

---

## Future Enhancements

* User Authentication
* Role-Based Access Control
* Export Employee Data
* Dashboard Analytics
* Email Notifications

---

## Author

**Sakshi Kulkarni**

Computer Science Engineering Student

---

## License

This project was developed for educational and internship evaluation purposes.
