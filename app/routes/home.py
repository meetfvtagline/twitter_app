from flask import Blueprint, render_template,request,url_for,redirect,current_app
from app.routes.auth import get_current_user, login_required
from werkzeug.utils import secure_filename
from app.models.user import Blog
from app.extenstions import db
import os
import uuid

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    user=get_current_user()
    return render_template("home.html")


@home_bp.route("/dashboard")
@login_required
def dashboard():
    user = get_current_user()
    blogs= Blog.query.order_by(Blog.id.desc()).all()
    return render_template("dashboard.html", user=user,blogs=blogs)

@home_bp.route("/create_blog",methods=['POST','GET'])
@login_required
def create_blog():
    user=get_current_user()
    if request.method=="POST":
        title=request.form['title']
        discription=request.form['discription']
        image=request.files['image']

        image_path=None

        if image and image.filename:
            filename = secure_filename(image.filename)
            unique_name = f"{uuid.uuid4()}_{filename}"

            upload_folder = os.path.join(   
                current_app.root_path,
                "static/uploads/blogs"
            )

            os.makedirs(upload_folder, exist_ok=True)

            image.save(os.path.join(upload_folder, unique_name))    
            image_path = f"uploads/blogs/{unique_name}"


        blog=Blog(
            title=title,
            discription=discription,
            image_path=image_path,
            user_id=user.id
        )

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for("home.dashboard"))

    return render_template("create_blog.html")
