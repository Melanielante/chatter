from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from routes.auth_routes import auth_bp

# db = SQLAlchemy()
# migrate = Migrate()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chatter.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

migrate = Migrate(app, db)
CORS(app)

# import routes here later


@app.route ("/health")
def health_check():
    return {"status": "ok"}, 200

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
