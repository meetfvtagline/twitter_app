'''
Docstring for app.routes.admin

All the admin acces route are in this file
'''


from flask import Blueprint,render_template,session,redirect,flash,url_for,request
from flask import abort
from flask_login import current_user
from functools import wraps
from app.models.user import User,Blog,Like
from app.routes.auth import get_current_user
from app.extenstions import db

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please login first")
            return redirect(url_for("auth.login"))

        if session.get('role') != 'admin':
            flash("Unauthorized access")
            return redirect(url_for("home.dashboard"))

        return f(*args, **kwargs)
    return wrapper


admin_bp=Blueprint("admin",__name__,url_prefix='/admin')

@admin_required
@admin_bp.route("/dashboard")
def dashboard():
    user = get_current_user()
    blogs= Blog.query.order_by(Blog.id.desc()).all()

    return render_template("admin/admin_dashboard.html",curr_user=user,blogs=blogs)

@admin_bp.route("/blogs", methods=["GET", "POST"])
@admin_required
def blogs():
    curr_user = get_current_user()

    if request.method == "POST":
        blog_id = request.form.get("delete")
        if blog_id:
            blog = Blog.query.get_or_404(blog_id)
            db.session.delete(blog)
            db.session.commit()
            flash("Blog deleted")

    blogs = Blog.query.order_by(Blog.id.desc()).all()

    return render_template(
        "admin/all_blog.html",
        curr_user=curr_user,
        blogs=blogs
    )

    
@admin_bp.route("/users", methods=["GET", "POST"])
@admin_required
def users():
    curr_user = get_current_user()

    if request.method == "POST":
        user_id = request.form.get("delete")
        if user_id:
            user = User.query.get_or_404(user_id)

            if user.id == curr_user.id:
                flash("You cannot delete yourself")
            else:
                db.session.delete(user)
                db.session.commit()
                flash("User deleted")

    users = User.query.all()

    return render_template(
        "admin/all_users.html",
        curr_user=curr_user,
        users=users
    )
