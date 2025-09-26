from flask import request
from flask_restful import Resource
from models import db, User, Post, Group
from werkzeug.security import generate_password_hash

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {"error": "User not found"}, 404

            # Safe user serialization
            user_data = user.to_safe_dict()
            user_data["posts"] = [
                {"id": p.id, "content": p.content} for p in user.posts
            ]
            user_data["groups"] = [
                {"id": g.id, "name": g.name, "description": g.description}
                for g in user.groups
            ]
            return user_data, 200

        else:
            users = User.query.all()
            return [
                {
                    **u.to_safe_dict(),
                    "posts": [{"id": p.id, "content": p.content} for p in u.posts],
                    "groups": [{"id": g.id, "name": g.name} for g in u.groups],
                }
                for u in users
            ], 200

    def post(self):
        data = request.get_json()

        # Basic validation
        if not data.get("username") or not data.get("email") or not data.get("password"):
            return {"error": "Missing required fields"}, 400

        new_user = User(
            username=data["username"],
            email=data["email"],
            password=generate_password_hash(data["password"])  # ✅ secure
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_safe_dict(), 201

    def patch(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        data = request.get_json()
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)

        db.session.commit()
        return user.to_safe_dict(), 200

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200
