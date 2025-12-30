from flask import Blueprint, render_template
from app.routes.auth import get_current_user, login_required

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    user=get_current_user()
    return render_template("home.html")


@home_bp.route("/dashboard")
@login_required
def dashboard():
    user = get_current_user()
    return render_template("dashboard.html", user=user)
