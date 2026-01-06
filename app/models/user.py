from app.extenstions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="user")

    blogs = db.relationship(
        "Blog",
        backref="user",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    likes = db.relationship(
        "Like",
        backref="user",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    
class Blog(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    image_path = db.Column(db.String(255))

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    likes = db.relationship(
        "Like",
        backref="blog",
        cascade="all, delete-orphan",
        passive_deletes=True
    )



class Like(db.Model):
    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    blog_id = db.Column(
        db.Integer,
        db.ForeignKey("blogs.id", ondelete="CASCADE"),
        nullable=False
    )

    __table_args__ = (
        db.UniqueConstraint("user_id", "blog_id", name="unique_user_blog_like"),
    )




