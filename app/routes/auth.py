'''
Docstring for app.routes.auth 
All the Authectication is handle by this file. 
'''

from flask import Blueprint,render_template,request,redirect,url_for,flash,jsonify,make_response,session
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.extenstions import db
from app.config import Config
from datetime import datetime, timezone, timedelta
from functools import wraps
import uuid
import jwt



auth_bp=Blueprint("auth",__name__,url_prefix="/auth")


def get_current_user():
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    return None 

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please login first")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return wrapper

@auth_bp.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, private"
    return response


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form['email']

        if User.query.filter_by(email=email).first():
            flash("User already exists")
            return redirect(url_for("auth.register"))

        user = User(
            public_id=str(uuid.uuid4()),
            username=request.form["username"],
            email=email,
            password_hash=generate_password_hash(request.form["password"])
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful. Please login.")
        return redirect(url_for("auth.login"))

    return render_template("register.html")   



@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()

        if not user or not check_password_hash(user.password_hash, request.form["password"]):
            flash("Invalid credentials")
            return redirect(url_for("auth.login"))

        session['user_id'] = user.id
        flash("Login successful")
        return redirect(url_for("home.dashboard"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully")
    return redirect(url_for("home.home"))
