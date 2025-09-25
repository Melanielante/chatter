from flask import request
from flask_restful import Resource
from models import db, Post, User, Group

class PostResource(Resource):
    def get(self, post_id=None):
        if post_id:
            post = Post.query.get(post_id)
            if not post:
                return {"error": "Post not found"}, 404

            post_data = post.to_dict()
            post_data["user"] = post.user.to_dict(only=("id", "username"))
            post_data["group"] = post.group.to_dict(only=("id", "name")) if post.group else None
            post_data["comments"] = [c.to_dict(only=("id", "content", "user_id")) for c in post.comments]
            post_data["likes"] = [l.user.to_dict(only=("id", "username")) for l in post.likes]

            return post_data, 200

        posts = Post.query.all()
        posts_data = []
        for p in posts:
            post_obj = p.to_dict(only=("id", "content"))
            post_obj["user"] = p.user.to_dict(only=("id", "username"))
            post_obj["group"] = p.group.to_dict(only=("id", "name")) if p.group else None
            post_obj["likes_count"] = len(p.likes)
            post_obj["comments_count"] = len(p.comments)
            posts_data.append(post_obj)

        return posts_data, 200

    def post(self):
        data = request.get_json()

        user = User.query.get(data.get("user_id"))
        if not user:
            return {"error": "Invalid user_id"}, 400

        group = None
        if data.get("group_id"):
            group = Group.query.get(data.get("group_id"))
            if not group:
                return {"error": "Invalid group_id"}, 400

        try:
            new_post = Post(
                content=data.get("content"),
                user_id=data.get("user_id"),
                group_id=data.get("group_id")
            )
            db.session.add(new_post)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

        return new_post.to_dict(), 201

    def patch(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            return {"error": "Post not found"}, 404

        data = request.get_json()
        post.content = data.get("content", post.content)

        db.session.commit()
        return post.to_dict(), 200

    def delete(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            return {"error": "Post not found"}, 404

        db.session.delete(post)
        db.session.commit()
        return {"message": "Post deleted"}, 200

