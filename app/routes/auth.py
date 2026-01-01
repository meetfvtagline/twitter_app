'''
Docstring for app.routes.auth 
All the Authectication is handle by this file. 
'''

from flask import Blueprint,render_template,request,redirect,url_for,flash,jsonify,make_response,session
from flask_mail import Message,Mail
from app.routes.utils import generate_reset_token,verify_reset_token
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.extenstions import db,mail
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

@auth_bp.route("/profile")
@login_required
def profile():
    user=get_current_user()
    user_name=user.username
    user_email=user.email
    return render_template("profile.html",username=user_name,user_email=user_email)

@auth_bp.route("/change_pass",methods=['POST','GET'])
@login_required
def change_pass():
    user=get_current_user()
    if request.method=="POST":
        old_pass=request.form['oldpass']
        new_pass=request.form['newpass']

        if check_password_hash(user.password_hash,old_pass):
            user.password_hash=generate_password_hash(new_pass)
            flash("Password changed succesfully")
            db.session.commit()
            return redirect(url_for("auth.profile"))
        else:
            flash("Invalid Old pass..")
            redirect(url_for("auth.change_pass"))

        
    return render_template("password_change.html")




@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()

        if user:
            token = generate_reset_token(user.email)
            reset_url = url_for(
                "auth.reset_password",
                token=token,
                _external=True
            )

            msg = Message(
                subject="Password Reset Request from Twitter App",
                recipients=[user.email],
                body=f"""
Hello {user.username},
Click the link below to reset your password:
{reset_url}
This link expires in 30 minutes.
"""
            )
            mail.send(msg)

        flash("If that email exists, a reset link has been sent.")
        return redirect(url_for("auth.login"))

    return render_template("forget_pass.html")

@auth_bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    email = verify_reset_token(token)

    if not email:
        flash("Invalid or expired token.")
        return redirect(url_for("auth.login"))

    user = User.query.filter_by(email=email).first_or_404()

    if request.method == "POST":
        password = request.form['password']
        user.password_hash = generate_password_hash(password)
        db.session.commit()

        flash("Password reset successful. Please login.")
        return redirect(url_for("auth.login"))

    return render_template("reset_password.html")
