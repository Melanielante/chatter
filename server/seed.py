from server.app import app
from server.models import db, User, Post, Group

users_seed = [
    {"id": 1, "username": "mel", "email": "mel@example.com", "password": "password123"},
    {"id": 2, "username": "alex", "email": "alex@example.com", "password": "password123"},
    {"id": 3, "username": "sam", "email": "sam@example.com", "password": "password123"},
]

groups_seed = [
    {"id": 1, "name": "Techies", "description": "A group for tech lovers."},
    {"id": 2, "name": "Foodies", "description": "Share and discover food experiences."},
    {"id": 3, "name": "Gamers", "description": "A place for gamers to connect."},
]

posts_seed = [
    {"id": 1, "content": "Just started learning Flask! ", "user_id": 1},
    {"id": 2, "content": "React makes frontend so much fun ", "user_id": 2},
    {"id": 3, "content": "Any gamers here? ", "user_id": 3},
    {"id": 4, "content": "Best pizza place in town?", "user_id": 2},
    {"id": 5, "content": "Who’s going to PyCon?", "user_id": 1},
]

with app.app_context():
    db.drop_all()   # clears old data
    db.create_all() # creates tables

    print("Seeding users...")
    for user in users_seed:
        new_user = User(**user)
        db.session.add(new_user)

    print("Seeding groups...")
    for group in groups_seed:
        new_group = Group(**group)
        db.session.add(new_group)

    print("Seeding posts...")
    for post in posts_seed:
        new_post = Post(**post)
        db.session.add(new_post)

    db.session.commit()
    print(" Database seeded!")
