from flask import Blueprint, render_template, session, redirect, url_for

view = Blueprint('view', __name__)

@view.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('admin-dashboard.html')
