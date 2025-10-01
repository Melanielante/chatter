
from app import app, DATABASE_URL
from models import db, User, Post, Group, Comment, Like
from werkzeug.security import generate_password_hash


#  data

users_seed = [
    {"id": 4, "username": "mel", "email": "mel@example.com", "password": "password123"},
    {"id": 5, "username": "alex", "email": "alex@example.com", "password": "password123"},
    {"id": 6, "username": "sam", "email": "sam@example.com", "password": "password123"},
]

groups_seed = [
    {"id": 1, "name": "Techies", "description": "A group for tech lovers."},
    {"id": 2, "name": "Foodies", "description": "Share and discover food experiences."},
    {"id": 3, "name": "Gamers", "description": "A place for gamers to connect."},
]

posts_seed = [
    {"id": 1, "content": "Just started learning Flask!", "user_id": 4, "group_id": 1},
    {"id": 2, "content": "React makes frontend so much fun", "user_id": 5, "group_id": 1},
    {"id": 3, "content": "Any gamers here?", "user_id": 6, "group_id": 3},
    {"id": 4, "content": "Best pizza place in town?", "user_id": 5, "group_id": 2},
    {"id": 5, "content": "Who’s going to PyCon?", "user_id": 4, "group_id": 1},
]

comments_seed = [
    {"content": "That’s awesome, Flask is cool!", "user_id": 5, "post_id": 1},
    {"content": "I’m also starting Flask this week", "user_id": 6, "post_id": 1},
    {"content": "Totally agree, React makes UI fun!", "user_id": 6, "post_id": 2},
    {"content": "React hooks are game-changers", "user_id": 4, "post_id": 2},
    {"content": "I’m definitely a gamer", "user_id": 4, "post_id": 3},
    {"content": "What games are you into?", "user_id": 5, "post_id": 3},
    {"content": "Best pizza is at Mario’s downtown", "user_id": 4, "post_id": 4},
    {"content": "I vote for Pizza Inn", "user_id": 4, "post_id": 4},
    {"content": "I’ll be at PyCon this year!", "user_id": 5, "post_id": 5},
    {"content": "Wish I could join, maybe next year", "user_id": 6, "post_id": 5},
]

likes_seed = [
    {"user_id": 4, "post_id": 1},
    {"user_id": 6, "post_id": 1},
    {"user_id": 4, "post_id": 2},
    {"user_id": 6, "post_id": 2},
    {"user_id": 4, "post_id": 3},
    {"user_id": 5, "post_id": 3},
    {"user_id": 4, "post_id": 4},
    {"user_id": 5, "post_id": 4},
    {"user_id": 6, "post_id": 4},
    {"user_id": 4, "post_id": 5},
    {"user_id": 5, "post_id": 5},
]


# database

with app.app_context():
    # Only drop and recreate tables for local dev (SQLite)
    if DATABASE_URL.startswith("sqlite"):
        print("Dropping all tables (local dev)...")
        db.drop_all()
        db.create_all()
    else:
        print("Production database detected, skipping drop_all()...")

    
    #  users
   
    print("Seeding users...")
    users = []
    for u in users_seed:
        user = User(
            id=u["id"],
            username=u["username"],
            email=u["email"],
            password=generate_password_hash(u["password"])
        )
        users.append(user)
    db.session.add_all(users)

   
    # groups
    
    print("Seeding groups...")
    groups = [Group(**group) for group in groups_seed]
    db.session.add_all(groups)

    
    #  posts
    
    print("Seeding posts...")
    posts = [Post(**post) for post in posts_seed]
    db.session.add_all(posts)

    
    # comments
   
    print("Seeding comments...")
    comments = [Comment(**comment) for comment in comments_seed]
    db.session.add_all(comments)

  
    # likes
    
    print("Seeding likes...")
    likes = [Like(**like) for like in likes_seed]
    db.session.add_all(likes)

    
    # Link users to groups
    
    print("Seeding memberships...")
    users[0].groups.append(groups[0])
    users[1].groups.append(groups[1])
    users[2].groups.append(groups[2])

    db.session.commit()
    print(" Database seeded successfully!")
