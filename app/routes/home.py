'''
Docstring for app.routes.home

All the dashboard for user endpoints handle in here.
'''



from flask import Blueprint, render_template,request,url_for,redirect,current_app,abort,flash,jsonify
from app.routes.auth import get_current_user, login_required
from werkzeug.utils import secure_filename
from app.models.user import Blog,Like,User,Follow
from app.extenstions import db
import os
import uuid

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    return render_template("home.html")


@home_bp.route("/dashboard")
@login_required
def dashboard():
    user = get_current_user()
    blogs= Blog.query.order_by(Blog.id.desc()).all()

    liked_blog_ids = [
        like.blog_id
        for like in Like.query.filter_by(user_id=user.id).all()
    ]

    return render_template(
        "dashboard.html", user=user,blogs=blogs,liked_blog_ids=liked_blog_ids
    )

@home_bp.route("/create_blog",methods=['POST','GET'])
@login_required
def create_blog():
    user=get_current_user()
    MAX_WORDS=150
    
    if request.method=="POST":
        title=request.form['title']
        description=request.form['description']
        image=request.files['image']

        image_path=None

        word_count = len(description.split())
      
        
        if word_count > MAX_WORDS:
            flash("Description cannot exceed 150 words")
            return redirect(request.url)
    
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
            description=description,
            image_path=image_path,
            user_id=user.id,
        )

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for("home.dashboard"))

    return render_template("create_blog.html")


@home_bp.route("/delete_blog", methods=["POST"])
@login_required
def delete_blog():
    user = get_current_user()

    blog_id = request.form.get("delete")
    blog = Blog.query.get_or_404(blog_id)

    if blog.user_id != user.id:
        abort(403)

    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for("home.dashboard"))
     



@home_bp.route("/update_blog/<int:blog_id>",methods=['POST','GET'])
@login_required
def update_blog(blog_id):
    
    MAX_WORDS=150
    blog=Blog.query.get_or_404(blog_id)

    user = get_current_user()
    if blog.user_id != user.id:
        abort(403)
    
    if request.method=="POST":
        blog.title = request.form['title']
        description = request.form['description']

        word_count = len(description.split())
        if word_count > MAX_WORDS:
            flash("Description cannot exceed 150 words")
            return redirect(request.url)
        
        blog.description = description

        image = request.files.get("image")
        if image and image.filename:
            filename = secure_filename(image.filename)
            unique_name = f"{uuid.uuid4()}_{filename}"

            upload_folder = os.path.join(
                current_app.root_path,
                "static/uploads/blogs"
            )
            os.makedirs(upload_folder, exist_ok=True)

            image.save(os.path.join(upload_folder, unique_name))
            blog.image_path = f"uploads/blogs/{unique_name}"

        db.session.commit()
        return redirect(url_for("home.dashboard"))


    return render_template("update_blog.html",blog=blog)

@home_bp.route("/like/<int:blog_id>", methods=["POST"])
@login_required
def like_blog(blog_id):
    user = get_current_user()
    blog = Blog.query.get_or_404(blog_id)

    like = Like.query.filter_by(
        user_id=user.id,
        blog_id=blog.id
    ).first()

    if like:
        db.session.delete(like)
        liked = False
    else:
        db.session.add(Like(user_id=user.id, blog_id=blog.id))
        liked = True

    db.session.commit()

    return jsonify({
        "liked": liked,
        "likes_count": len(blog.likes)
    })

@home_bp.route("/user_profile/<int:user_id>")
@login_required
def userprofile(user_id):
    user_curr=get_current_user()
    if user_id==user_curr.id:
        return redirect(url_for("auth.profile"))
    user=User.query.get_or_404(user_id)
    blogs = Blog.query.filter_by(user_id=user.id).order_by(Blog.id.desc()).all()
    return render_template("user_profile.html",user=user,blogs=blogs)

@home_bp.route("/followuser/<int:user_id>", methods=["POST"])
def followuser(user_id):
    user_follower = get_current_user()          # User object
    user_following = User.query.get_or_404(user_id)

    # prevent self-follow
    if user_follower.id == user_following.id:
        return redirect(url_for("home.dashboard"))

    # prevent duplicate follow
    existing = Follow.query.filter_by(
        follower_id=user_follower.id,
        following_id=user_following.id
    ).first()

    if not existing:
        follow = Follow(
            follower_id=user_follower.id,
            following_id=user_following.id
        )
        db.session.add(follow)
        db.session.commit()

    return redirect(url_for("home.dashboard"))
