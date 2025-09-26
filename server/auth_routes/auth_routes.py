from flask import Blueprint, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# SIGNUP 
@auth_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()

        # Basic validation
        if not data or not data.get("username") or not data.get("email") or not data.get("password"):
            return jsonify({"error": "Missing required fields"}), 400

        # Check if user already exists
        if User.query.filter_by(username=data["username"]).first():
            return jsonify({"error": "Username already exists"}), 400
        if User.query.filter_by(email=data["email"]).first():
            return jsonify({"error": "Email already exists"}), 400

        # Create new user with hashed password
        new_user = User(
            username=data["username"],
            email=data["email"],
            password=generate_password_hash(data["password"])
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.to_dict()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# LOGIN 
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        # Basic validation
        if not data or not data.get("email") or not data.get("password"):
            return jsonify({"error": "Email and password are required"}), 400

        # Find user by email
        user = User.query.filter_by(email=data["email"]).first()
        if not user:
            return jsonify({"error": "Invalid email or password"}), 401

        # Check password
        if not check_password_hash(user.password, data["password"]):
            return jsonify({"error": "Invalid email or password"}), 401

        # If successful, return user data (without password)
        return jsonify(user.to_dict()), 200

    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500
