#In Here The Flask App we create
from flask import Flask
from flask_mail import Mail,Message
from .config import Config
from flask_migrate import Migrate
from .routes.auth import auth_bp
from .routes.home import home_bp
from .extenstions import db,csrf,mail
from app.models.user import User,Blog
import os

migrate=Migrate()


def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)


    @app.after_request
    def add_global_headers(response):
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, private"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response

    mail.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)


    return app