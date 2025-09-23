

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Association table for many-to-many (Users - Groups)
user_group = db.Table(
    'user_group',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    posts = db.relationship("Post", backref="user", lazy=True)
    groups = db.relationship("Group", secondary=user_group, back_populates="users")

    # Control how serialization works
    serialize_rules = ("-posts.user", "-groups.users")

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model, SerializerMixin):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))

    group = db.relationship("Group", back_populates="posts")

    # Avoid recursion
    serialize_rules = ("-user.posts", "-group.posts")

    def __repr__(self):
        return f"<Post {self.id}: {self.content[:20]}>"


class Group(db.Model, SerializerMixin):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=True)

    users = db.relationship("User", secondary=user_group, back_populates="groups")
    posts = db.relationship("Post", back_populates="group")

    # Avoid recursion
    serialize_rules = ("-users.groups", "-posts.group")

    def __repr__(self):
        return f"<Group {self.name}>"
