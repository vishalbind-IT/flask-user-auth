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
├── app.py # Main Flask application
├── config.py # Configuration for MySQL connection and secret keys
├── templates/ # HTML templates (login.html, register.html, dashboard.html)
├── static/ # Static files (optional, for CSS/JS)
└── README.md # Project documentation

yaml
Copy code

---

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/vishalbind-IT/your-repo-name.git
cd your-repo-name
2. Create and activate a virtual environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
(If you don't have a requirements.txt, create one with these contents:)

nginx
Copy code
Flask
Flask-MySQLdb
Werkzeug
4. Setup MySQL Database
Make sure MySQL server is installed and running on your machine.

a. Login to MySQL shell:
bash
Copy code
mysql -u root -p
(Enter your MySQL root password when prompted)

b. Create the database and users table:
sql
Copy code
CREATE DATABASE your_database_name;
USE your_database_name;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);
c. (Optional) Create a dedicated MySQL user with permissions:
sql
Copy code
CREATE USER 'your_mysql_user'@'localhost' IDENTIFIED BY 'your_mysql_password';
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_mysql_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
5. Configure your Flask app
Create or edit config.py in your project root with the following variables (update with your details):

python
Copy code
MYSQL_HOST = 'localhost'
MYSQL_USER = 'your_mysql_user'
MYSQL_PASSWORD = 'your_mysql_password'
MYSQL_DB = 'your_database_name'
SECRET_KEY = 'your_secret_key_here'
The SECRET_KEY is used by Flask for securely signing the session cookie. Use a random string.

6. Run the Flask application
Make sure your virtual environment is active, then run:

bash
Copy code
python app.py
