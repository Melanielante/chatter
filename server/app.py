from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from models import db  
from auth_routes import auth_bp
from routes.users import UserResource
from routes.posts import PostResource
from routes.comments import CommentResource
from routes.likes import LikeResource
from routes.groups import GroupResource
from flask_jwt_extended import JWTManager

import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = Flask(__name__)

# Database
DATABASE_URL = os.environ.get(
    "DATABASE_URL", "sqlite:///chatter.db"
)
# Fix legacy postgres:// URLs
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Ensure SSL is required on Render
if "render.com" in DATABASE_URL:
    if "?" in DATABASE_URL:
        DATABASE_URL += "&sslmode=require"
    else:
        DATABASE_URL += "?sslmode=require"

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.environ.get(
    "JWT_SECRET_KEY", "super-secret-key"
)

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)  # Flask-Migrate will handle DB creation
CORS(app)
api = Api(app)

# Routes
api.add_resource(UserResource, "/users", "/users/<int:user_id>")
api.add_resource(PostResource, "/posts", "/posts/<int:post_id>")
api.add_resource(CommentResource, "/comments", "/comments/<int:comment_id>")
api.add_resource(LikeResource, "/likes", "/likes/<int:like_id>")
api.add_resource(GroupResource, "/groups", "/groups/<int:group_id>")
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
