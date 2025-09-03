# Flask User Authentication System

A simple web application built with **Flask** that provides user registration, login, session management, and a basic dashboard. The app uses **MySQL** for data storage and **Werkzeug** for password hashing.

---

## Features

- User registration with validation (username, email format, password length)
- Secure password hashing and verification using Werkzeug
- User login with session handling
- Dashboard accessible only to logged-in users
- Logout functionality to clear session
- Flash messages for feedback on actions
- Input validation and error handling
- Uses MySQL database to store user data

---

## Technologies Used

- Python 3.x
- Flask (Micro web framework)
- Flask-MySQLdb (MySQL database connector for Flask)
- Werkzeug (Password hashing utilities)
- MySQL (Relational database)
- HTML/CSS (via Jinja2 templates)

---

## Project Structure

/flask-user-auth
│
├── app.py               # Main Flask application
├── config.py            # Configuration for MySQL connection and secret keys
├── templates/           # HTML templates (login.html, register.html, dashboard.html)
└── static/              # Static files (optional, for CSS/JS) 

yaml
Copy code

---

## Setup and Installation

```bash
1. Install dependencies
bash
Copy code
pip install -r requirements.txt

nginx
Copy code
Flask
Flask-MySQLdb
Werkzeug

2.Create Database
CREATE DATABASE your_database_name;
USE your_database_name;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

bash

python app.py
