
from flask import request
from flask_restful import Resource
from models import db, Comment, User, Post

class CommentResource(Resource):
    def get(self, comment_id=None):
        if comment_id:
            comment = Comment.query.get(comment_id)
            if not comment:
                return {"error": "Comment not found"}, 404

            comment_data = comment.to_dict(only=("id", "content"))
            comment_data["user"] = comment.user.to_dict(only=("id", "username"))
            comment_data["post"] = comment.post.to_dict(only=("id", "content"))

            return comment_data, 200
        else:
            comments = Comment.query.all()
            comments_data = []
            for c in comments:
                comment_obj = c.to_dict(only=("id", "content"))
                comment_obj["user"] = c.user.to_dict(only=("id", "username"))
                comment_obj["post_id"] = c.post_id
                comments_data.append(comment_obj)

            return comments_data, 200

    def post(self):
        data = request.get_json()

        user = User.query.get(data.get("user_id"))
        if not user:
            return {"error": "Invalid user_id"}, 400

        post = Post.query.get(data.get("post_id"))
        if not post:
            return {"error": "Invalid post_id"}, 400

        try:
            new_comment = Comment(
                content=data.get("content"),
                user_id=data.get("user_id"),
                post_id=data.get("post_id")
            )
            db.session.add(new_comment)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

        return new_comment.to_dict(), 201

    def patch(self, comment_id):
        comment = Comment.query.get(comment_id)
        if not comment:
            return {"error": "Comment not found"}, 404

        data = request.get_json()
        comment.content = data.get("content", comment.content)

        db.session.commit()
        return comment.to_dict(), 200

    def delete(self, comment_id):
        comment = Comment.query.get(comment_id)
        if not comment:
            return {"error": "Comment not found"}, 404

        db.session.delete(comment)
        db.session.commit()
        return {"message": "Comment deleted"}, 200


