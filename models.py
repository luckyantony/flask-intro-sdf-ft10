from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    posts = db.relationship('Post', back_populates='user')

    @validates('email')
    def validate_email(self, key, value):
        if "@" not in value:
            raise ValueError("Email must have '@' character to be valid")
        return value

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    

class Post(db.Model, SerializerMixin):
    __tablename__ = "posts"

    serialize_rules = ("-user.posts",)

    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String, nullable=False)
    post_content = db.Column(db.String)
    post_image = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='posts')
