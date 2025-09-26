from flask import request
from flask_restful import Resource
from models import db, Group, User

class GroupResource(Resource):
    def get(self, group_id=None):
        if group_id:
            group = Group.query.get(group_id)
            if not group:
                return {"error": "Group not found"}, 404

            group_data = group.to_dict(only=("id", "name", "description"))
            group_data["users"] = [u.to_dict(only=("id", "username")) for u in group.users]
            group_data["posts"] = [p.to_dict(only=("id", "content", "user_id")) for p in group.posts]
            return group_data, 200
        else:
            groups = Group.query.all()
            return [g.to_dict(only=("id", "name", "description")) for g in groups], 200

    def post(self):
        data = request.get_json()
        try:
            new_group = Group(
                name=data.get("name"),
                description=data.get("description")
            )
            db.session.add(new_group)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

        return new_group.to_dict(), 201

    def patch(self, group_id):
        group = Group.query.get(group_id)
        if not group:
            return {"error": "Group not found"}, 404

        data = request.get_json()
        group.name = data.get("name", group.name)
        group.description = data.get("description", group.description)

        db.session.commit()
        return group.to_dict(), 200

    def delete(self, group_id):
        group = Group.query.get(group_id)
        if not group:
            return {"error": "Group not found"}, 404

        db.session.delete(group)
        db.session.commit()
        return {"message": "Group deleted"}, 200
