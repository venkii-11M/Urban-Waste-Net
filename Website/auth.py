from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from .models import get_db_connection
from flask_bcrypt import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

# ---------------------- REGISTER ---------------------- #

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('fullName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        password = request.form.get('password')

        hashed_password = generate_password_hash(password).decode('utf-8')

        conn = get_db_connection()
        cur = conn.cursor()

        sql = """
        INSERT INTO users (name,email, phone_no, password, address)
        VALUES (%s, %s, %s, %s,%s)
        """
        val = (name,email, phone, hashed_password, address)

        try:
            cur.execute(sql, val)
            conn.commit()
            flash("Account created successfully!", "success")
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash("Something went wrong. Try again.", "danger")
            print("Error:", e)

    return render_template('signup.html')


# ---------------------- LOGIN ---------------------- #

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_phone = request.form.get('email')
        password = request.form.get('password')

        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)

        sql = "SELECT * FROM users WHERE email = %s"
        cur.execute(sql, (email_or_phone,))
        user = cur.fetchone()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            return redirect(url_for('view.dashboard'))
        else:
            flash("Invalid details", "danger")
            return redirect(url_for("auth.login"))


    return render_template('login.html')
