'''
Docstring for app.routes.auth 
All the Authectication is handle by this file. 
'''

from flask import Blueprint,render_template,request,redirect,url_for,flash,jsonify,make_response
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.extenstions import db
from app.config import Config
from datetime import datetime, timezone, timedelta
from functools import wraps
import uuid
import jwt



auth_bp=Blueprint("auth",__name__,url_prefix="/auth")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('jwt_token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@auth_bp.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":
        # if User.query.filter_by(email=request.form['email']).first():
        #     flash("User Alrady Exists")
        #     return redirect(url_for("auth.register"))
        if User.query.filter_by(email=request.form["email"]).first():
            return {"error": "User already exists"}, 409

        user=User(
            public_id=str(uuid.uuid4()),
            username=request.form["username"],  
            email=request.form["email"],
            password_hash=generate_password_hash(request.form["password"])
        ) 
        db.session.add(user)
        db.session.commit()

        flash("Register Succesfully")
        return redirect(url_for("auth.login"))        
    
    return render_template("register.html")     

@auth_bp.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        user=User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password,password):
            return jsonify({'message:invalid email or password'}),401
        
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.now(timezone.utc) + timedelta(hours=1)},Config.SECRET_KEY, algorithm="HS256")

        reponse=make_response(redirect(url_for('dashboard')))
        reponse.set_cookie('jwt_token',token)

        return reponse
    return render_template("login.html")