from app import app, DATABASE_URL
from models import db, User, Post, Group, Comment, Like
from werkzeug.security import generate_password_hash

# ---------------- Data ----------------
users_seed = [
    {"username": "mel", "email": "mel@example.com", "password": "password123"},
    {"username": "alex", "email": "alex@example.com", "password": "password123"},
    {"username": "sam", "email": "sam@example.com", "password": "password123"},
]

groups_seed = [
    {"name": "Techies", "description": "A group for tech lovers."},
    {"name": "Foodies", "description": "Share and discover food experiences."},
    {"name": "Gamers", "description": "A place for gamers to connect."},
]

posts_seed = [
    {"content": "Just started learning Flask!", "user_index": 0, "group_index": 0},
    {"content": "React makes frontend so much fun", "user_index": 1, "group_index": 0},
    {"content": "Any gamers here?", "user_index": 2, "group_index": 2},
    {"content": "Best pizza place in town?", "user_index": 1, "group_index": 1},
    {"content": "Who’s going to PyCon?", "user_index": 0, "group_index": 0},
]

comments_seed = [
    {"content": "That’s awesome, Flask is cool!", "user_index": 1, "post_index": 0},
    {"content": "I’m also starting Flask this week", "user_index": 2, "post_index": 0},
    {"content": "Totally agree, React makes UI fun!", "user_index": 2, "post_index": 1},
    {"content": "React hooks are game-changers", "user_index": 0, "post_index": 1},
    {"content": "I’m definitely a gamer", "user_index": 0, "post_index": 2},
    {"content": "What games are you into?", "user_index": 1, "post_index": 2},
    {"content": "Best pizza is at Mario’s downtown", "user_index": 0, "post_index": 3},
    {"content": "I vote for Pizza Inn", "user_index": 0, "post_index": 3},
    {"content": "I’ll be at PyCon this year!", "user_index": 1, "post_index": 4},
    {"content": "Wish I could join, maybe next year", "user_index": 2, "post_index": 4},
]

likes_seed = [
    {"user_index": 0, "post_index": 0},
    {"user_index": 2, "post_index": 0},
    {"user_index": 0, "post_index": 1},
    {"user_index": 2, "post_index": 1},
    {"user_index": 0, "post_index": 2},
    {"user_index": 1, "post_index": 2},
    {"user_index": 0, "post_index": 3},
    {"user_index": 1, "post_index": 3},
    {"user_index": 2, "post_index": 3},
    {"user_index": 0, "post_index": 4},
    {"user_index": 1, "post_index": 4},
]

# ---------------- Seed DB ----------------
with app.app_context():
    # Only drop and recreate tables for local dev (SQLite)
    if DATABASE_URL.startswith("sqlite"):
        print("Dropping all tables (local dev)...")
        db.drop_all()
        db.create_all()
    else:
        print("Production database detected, skipping drop_all()...")

    # Seed Users
    print("Seeding users...")
    users = [User(
        username=u["username"],
        email=u["email"],
        password=generate_password_hash(u["password"])
    ) for u in users_seed]
    db.session.add_all(users)

    # Seed Groups
    print("Seeding groups...")
    groups = [Group(**g) for g in groups_seed]
    db.session.add_all(groups)
    db.session.flush()  # ensure IDs are generated for FK references

    # Seed Posts
    print("Seeding posts...")
    posts = []
    for p in posts_seed:
        post = Post(
            content=p["content"],
            user_id=users[p["user_index"]].id,
            group_id=groups[p["group_index"]].id
        )
        posts.append(post)
    db.session.add_all(posts)
    db.session.flush()

    # Seed Comments
    print("Seeding comments...")
    comments = []
    for c in comments_seed:
        comment = Comment(
            content=c["content"],
            user_id=users[c["user_index"]].id,
            post_id=posts[c["post_index"]].id
        )
        comments.append(comment)
    db.session.add_all(comments)

    # Seed Likes
    print("Seeding likes...")
    likes = []
    for l in likes_seed:
        like = Like(
            user_id=users[l["user_index"]].id,
            post_id=posts[l["post_index"]].id
        )
        likes.append(like)
    db.session.add_all(likes)

    # Link users to groups
    print("Seeding memberships...")
    for i, user in enumerate(users):
        user.groups.append(groups[i])

    db.session.commit()
    print("Database seeded successfully!")
