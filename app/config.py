# app configuration
from dotenv import load_dotenv
load_dotenv()
import os

USER = os.getenv('MAIL_USERNAME')
PASS = os.getenv('MAIL_PASSWORD')

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = USER
    MAIL_PASSWORD = PASS
    MAIL_DEFAULT_SENDER = USER
   



