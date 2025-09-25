from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from models import db
from auth_routes import auth_bp
from routes.users import UserResource
from routes.posts import PostResource
from routes.comments import CommentResource
from routes.likes import LikeResource
from routes.groups import GroupResource


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chatter.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
db.init_app(app)

migrate = Migrate(app, db)
CORS(app)

with app.app_context():
    db.create_all()

@app.route ("/health")
def health_check():
    return {"status": "ok"}, 200
  
# import routes 
api.add_resource(UserResource, "/users", "/users/<int:user_id>")
api.add_resource(PostResource, "/posts", "/posts/<int:post_id>")
api.add_resource(CommentResource, "/comments", "/comments/<int:comment_id>")
api.add_resource(LikeResource, "/likes", "/likes/<int:like_id>")
api.add_resource(GroupResource, "/groups", "/groups/<int:group_id>")


# Register blueprints
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run( debug=True)
