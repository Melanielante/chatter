from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime


db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    # Relationship to posts one to many user > posts

    posts = db.relationship('Post', backref='author', lazy=True)

    serialize_rules = ('-password_hash', '-posts.user') #hide password hash in json


    
class User(db.Model, SerializerMixin):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    serialize_rules = ('-author.posts',)


    def __repr__(self):
        return f'<Post {self.title}>'