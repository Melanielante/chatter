from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from models import db
from routes.users import UserResource

# db = SQLAlchemy()
# migrate = Migrate()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chatter.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# import routes here later
api.add_resource(UserResource, "/users", "/users/<int:user_id>")



if __name__ == "__main__":
    app.run(debug=True)
