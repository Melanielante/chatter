# routes/comments.py
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Comment, User, Post

class CommentResource(Resource):
    def get(self, comment_id=None):
        if comment_id:
            comment = Comment.query.get(comment_id)
            if not comment:
                return {"error": "Comment not found"}, 404

            comment_data = comment.to_dict()
            comment_data["user"] = comment.user.to_dict(only=("id", "username"))
            comment_data["post"] = comment.post.to_dict(only=("id", "content"))

            return comment_data
        else:
            comments = Comment.query.all()
            return [
                {
                    "id": c.id,
                    "content": c.content,
                    "user_id": c.user_id,
                    "post_id": c.post_id
                }
                for c in comments
            ]

    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()

        post = Post.query.get(data.get("post_id"))
        if not post:
            return {"error": "Invalid post_id"}, 400

        new_comment = Comment(
            content=data.get("content"),
            user_id=current_user_id,
            post_id=data.get("post_id")
        )
        db.session.add(new_comment)
        db.session.commit()

        return new_comment.to_dict(), 201

    @jwt_required()
    def delete(self, comment_id):
        comment = Comment.query.get(comment_id)
        if not comment:
            return {"error": "Comment not found"}, 404

        db.session.delete(comment)
        db.session.commit()
        return {"message": "Comment deleted"}
