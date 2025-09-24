# seed data for the database
from app import app
from models import db, User, Post, Group, Comment, Like

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
    {"id": 1, "content": "Just started learning Flask!", "user_id": 1, "group_id": 1},
    {"id": 2, "content": "React makes frontend so much fun ", "user_id": 2, "group_id": 1},
    {"id": 3, "content": "Any gamers here?", "user_id": 3, "group_id": 3},
    {"id": 4, "content": "Best pizza place in town?", "user_id": 2, "group_id": 2},
    {"id": 5, "content": "Who’s going to PyCon?", "user_id": 1, "group_id": 1},
]

comments_seed = [
    # Post 1
    {"content": "That’s awesome, Flask is cool!", "user_id": 2, "post_id": 1},
    {"content": "I’m also starting Flask this week ", "user_id": 3, "post_id": 1},
    # Post 2
    {"content": "Totally agree, React makes UI fun!", "user_id": 3, "post_id": 2},
    {"content": "React hooks are game-changers ", "user_id": 1, "post_id": 2},
    # Post 3
    {"content": "I’m definitely a gamer ", "user_id": 1, "post_id": 3},
    {"content": "What games are you into?", "user_id": 2, "post_id": 3},
    # Post 4
    {"content": "Best pizza is at Mario’s downtown ", "user_id": 1, "post_id": 4},
    {"content": "I vote for Pizza Inn ", "user_id": 3, "post_id": 4},
    # Post 5
    {"content": "I’ll be at PyCon this year!", "user_id": 2, "post_id": 5},
    {"content": "Wish I could join, maybe next year ", "user_id": 3, "post_id": 5},
]

likes_seed = [
    # Post 1
    {"user_id": 2, "post_id": 1},
    {"user_id": 3, "post_id": 1},
    # Post 2
    {"user_id": 1, "post_id": 2},
    {"user_id": 3, "post_id": 2},
    # Post 3
    {"user_id": 1, "post_id": 3},
    {"user_id": 2, "post_id": 3},
    # Post 4
    {"user_id": 1, "post_id": 4},
    {"user_id": 2, "post_id": 4},
    {"user_id": 3, "post_id": 4},
    # Post 5
    {"user_id": 1, "post_id": 5},
    {"user_id": 2, "post_id": 5},
]

with app.app_context():
    db.drop_all()
    db.create_all()

    print("Seeding users...")
    users = [User(**user) for user in users_seed]
    db.session.add_all(users)

    print("Seeding groups...")
    groups = [Group(**group) for group in groups_seed]
    db.session.add_all(groups)

    print("Seeding posts...")
    posts = [Post(**post) for post in posts_seed]
    db.session.add_all(posts)

    print("Seeding comments...")
    comments = [Comment(**comment) for comment in comments_seed]
    db.session.add_all(comments)

    print("Seeding likes...")
    likes = [Like(**like) for like in likes_seed]
    db.session.add_all(likes)

    # Create memberships (many-to-many links)
    print("Seeding memberships...")
    users[0].groups.append(groups[0])  
    users[1].groups.append(groups[1])  
    users[2].groups.append(groups[2])  

    db.session.commit()
    print(" Database seeded!")

