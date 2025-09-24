# routes/users.py
from flask import request
from flask_restful import Resource
from models import db, User

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {"error": "User not found"}, 404
            return user.to_dict()
        else:
            users = User.query.all()
            return [u.to_dict() for u in users]

    def post(self):
        data = request.get_json()
        new_user = User(
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password")
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201

    def patch(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        data = request.get_json()
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)

        db.session.commit()
        return user.to_dict()

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}
