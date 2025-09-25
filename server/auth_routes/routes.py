from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import db, User

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    # validate required fields
    if not data.get("username") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing fields"}), 400

    # hash password
    hashed_pw = generate_password_hash(data["password"])

    # create new user
    new_user = User(
        username=data["username"],
        email=data["email"],
        password=hashed_pw
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email
    }), 201
