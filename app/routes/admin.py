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


@admin_bp.route("/dashboard")
def dashboard():
    user = get_current_user()
    blogs= Blog.query.order_by(Blog.id.desc()).all()

    return render_template("admin/admin_dashboard.html",curr_user=user,blogs=blogs)

@admin_bp.route("/all_blog")
def allblog():
    user = get_current_user()
    blogs= Blog.query.order_by(Blog.id.desc()).all()
    return render_template("admin/all_blog.html",curr_user=user,blogs=blogs)

@admin_bp.route("/all_users")
def allusers():
    user = get_current_user()
    all=User.query.all()
    return render_template("admin/all_users.html",curr_user=user,all_user=all)

@admin_bp.route("/deleteuserblog",methods=['POST','GET'])
def deleteuserblog():
    curr_user=get_current_user()
    if request.method=='POST':
        blog_id=request.form['delete']
        blog = Blog.query.get_or_404(blog_id)
        db.session.delete(blog)
        db.session.commit()
        return render_template("admin/all_blog.html",curr_user=curr_user)

@admin_bp.route("/deleteuser",methods=['POST','GET'])
def deleteuser():
    curr_user=get_current_user()
    if request.method=='POST':
        user_id=request.form['delete']
        user=User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return render_template("admin/all_users.html",curr_user=curr_user)