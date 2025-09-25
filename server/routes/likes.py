
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Like, User, Post

class LikeResource(Resource):
    def get(self, like_id=None):
        if like_id:
            like = Like.query.get(like_id)
            if not like:
                return {"error": "Like not found"}, 404
            return {
                "id": like.id,
                "user": like.user.to_dict(only=("id", "username")),
                "post": like.post.to_dict(only=("id", "content"))
            }
        else:
            likes = Like.query.all()
            return [
                {
                    "id": l.id,
                    "user_id": l.user_id,
                    "post_id": l.post_id
                }
                for l in likes
            ]

    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()

        post = Post.query.get(data.get("post_id"))

        if not post:
            return {"error": "Invalid post_id"}, 400

        # check if like already exists
        existing_like = Like.query.filter_by(user_id=current_user_id, post_id=post.id).first()
        if existing_like:
            return {"error": "User already liked this post"}, 400

        new_like = Like(user_id=current_user_id, post_id=post.id)
        db.session.add(new_like)
        db.session.commit()

        return {
            "message": "Post liked",
            "like": new_like.to_dict()
        }, 201

    @jwt_required()
    def delete(self, like_id):
        like = Like.query.get(like_id)
        if not like:
            return {"error": "Like not found"}, 404

        db.session.delete(like)
        db.session.commit()
        return {"message": "Like removed"}
