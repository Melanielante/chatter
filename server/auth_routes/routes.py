from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt
from werkzeug.exceptions import BadRequest, Unauthorized

# Blueprint and Bcrypt instance
auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")
bcrypt = Bcrypt()

# Signup route
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    # Validate required fields
    if not data.get("username") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing fields"}), 400

    # Hash password using Flask-Bcrypt
    hashed_pw = bcrypt.generate_password_hash(data["password"]).decode('utf-8')

    # Create new user
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

# Login route
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    # Validate required fields
    if not data.get("email") or not data.get("password"):
        raise BadRequest("Email and password required.")

    # Find user by email
    user = User.query.filter_by(email=data["email"]).first()
    if not user or not bcrypt.check_password_hash(user.password, data["password"]):
        raise Unauthorized("Invalid credentials.")

    # Create JWT access token
    access_token = create_access_token(identity=user.id)

    return jsonify({
        "message": "Login successful",
        "access_token": access_token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 200

# Protected route to test JWT
@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
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
