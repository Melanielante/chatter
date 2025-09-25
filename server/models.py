
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Association table for many-to-many (Users - Groups)
user_group = db.Table(
    'user_group',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

# users table
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

# posts table
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

# groups table
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

# likes table
class Like(db.Model, SerializerMixin):
    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)

    user = db.relationship("User", backref="likes")
    post = db.relationship("Post", backref="likes")

    __table_args__ = (db.UniqueConstraint("user_id", "post_id", name="_user_post_uc"),)

    serialize_rules = ("-user.likes", "-post.likes")

    def __repr__(self):
        return f"<Like User {self.user_id} Post {self.post_id}>"

# comments table
class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

    user = db.relationship("User", backref="comments")
    post = db.relationship("Post", backref="comments")

    serialize_rules = ("-user.comments", "-post.comments")

    def __repr__(self):
        return f"<Comment {self.id} by User {self.user_id}>"

