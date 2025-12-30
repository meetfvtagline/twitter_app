from app.extenstions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    blogs = db.relationship('Blog', backref='user', lazy=True)
    
class Blog(db.Model):

    __tablename__="blogs"

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50),unique=True,nullable=False)
    discription = db.Column(db.Text, nullable=True)
    image_path = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)