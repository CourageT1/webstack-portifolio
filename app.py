#!/usr/bin/env python3

"""
Quiz App Backend

This script defines a Flask application to serve as the backend for a quiz app.
It includes user authentication, database persistence, and API endpoints for fetching subjects and questions.

Author: OpenAI
"""

from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random string
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

bcrypt = Bcrypt(app)


# Define database models
class User(UserMixin, db.Model):
    """Database model for users."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))


# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username is already taken
        if User.query.filter_by(username=username).first():
            return jsonify({'success': False, 'message': 'Username already exists'})
        # Hash the password
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        # Create a new user
        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Registration successful'})
    return render_template('register.html')


# API endpoint to fetch subjects
@app.route('/api/subjects')
def get_subjects():
    """
    Render the subject page.

    Args:
        subject_id: ID of the subject to display.

    Returns:
        Rendered HTML template for the subject page.
    """
    subjects = ['Football', 'Cricket', 'African History', 'Mathematics', 'Geography', 'English Language', 'Science']
    return jsonify({'success': True, 'subjects': subjects})


# API endpoint to fetch questions by subject
@app.route('/api/questions')
@login_required
def get_questions():
    """
    Fetch questions for a specific subject.

    Returns:
        JSON response with a list of questions for the specified subject.
    """
    subject = request.args.get('subject')
    # Logic to fetch questions from the database based on the subject
    return jsonify({'success': True, 'questions': []})


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return jsonify({'success': False, 'message': 'Invalid username or password'})
    return render_template('login.html')


# Logout route
@app.route('/logout')
@login_required
def logout():
    """User logout."""
    logout_user()
    return redirect(url_for('index'))


# Index route
@app.route('/')
def index():
    """
    Render the homepage.
    Returns:
    Rendered HTML template for the homepage.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
