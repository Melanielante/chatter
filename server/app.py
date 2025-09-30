import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from models import db, User
from auth_routes import auth_bp
from routes.users import UserResource
from routes.posts import PostResource
from routes.comments import CommentResource
from routes.likes import LikeResource
from routes.groups import GroupResource
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)

# Use DATABASE_URL from Render, fallback to local SQLite
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///chatter.db")

# Fix Render’s postgres:// → postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "super-secret-key")

api = Api(app)
db.init_app(app)
jwt = JWTManager(app)

migrate = Migrate(app, db)
CORS(app)

with app.app_context():
    db.create_all()

@app.route("/health")
def health_check():
    return {"status": "ok"}, 200

@app.route("/test-jwt")
@jwt_required()
def test_jwt():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user:
        return {"error": "User not found"}, 404
    return {
        "message": "JWT authentication successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }, 200

# API routes
api.add_resource(UserResource, "/users", "/users/<int:user_id>")
api.add_resource(PostResource, "/posts", "/posts/<int:post_id>")
api.add_resource(CommentResource, "/comments", "/comments/<int:comment_id>")
api.add_resource(LikeResource, "/likes", "/likes/<int:like_id>")
api.add_resource(GroupResource, "/groups", "/groups/<int:group_id>")

# Register blueprints
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
