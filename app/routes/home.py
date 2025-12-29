from flask import Blueprint,render_template
from app.routes.auth import token_required

home_bp=Blueprint("home",__name__,url_prefix="/")


@home_bp.route("/")
def home():
    return render_template("blog_page.html")


@home_bp.route('/dashboard')
@token_required
def dashboard(current_user):
    return f"Welcome {current_user.name}! You are logged in."