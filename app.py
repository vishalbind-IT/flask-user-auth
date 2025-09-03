from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import config
import re

app = Flask(__name__)
app.config.from_object(config)

# Initialize MySQL database connection

mysql = MySQL(app)

# Home route - Redirects to login

@app.route('/')
def home():
    return redirect(url_for('login'))

# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    errors = {}
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        # Validate inputs
        if len(username) < 3:
            errors['username'] = "Username must be at least 3 characters long"
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors['email'] = "Invalid email format"
        if len(password) < 6:
            errors['password'] = "Password must be at least 6 characters long"

        # Check if email exists
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", [email])
        existing_user = cur.fetchone()

        if existing_user:
            errors['email'] = "Email already registered. Please use another."

        # If no errors → insert user
        if not errors:
            hashed_pw = generate_password_hash(password)
            cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                        (username, email, hashed_pw))
            mysql.connection.commit()
            cur.close()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for('login'))

        cur.close()
    else:
        errors = {}

    return render_template('register.html', errors=errors)

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    errors = {}
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        if not email:
            errors['email'] = "Email is required"
        if not password:
            errors['password'] = "Password is required"

        if not errors:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users WHERE email = %s", [email])
            user = cur.fetchone()
            cur.close()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['username'] = user['username']
                flash("Login successful!", "success")
                return redirect(url_for('dashboard'))
            else:
                errors['general'] = "Invalid email or password"

    return render_template('login.html', errors=errors)

# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully", "info")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
