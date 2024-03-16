from main import app, user_datastore
from flask_security import hash_password
from model import db

with app.app_context():
    db.create_all()

    user_datastore.find_or_create_role(name="admin", description="This is an Admin role")
    user_datastore.find_or_create_role(name="user", description="This is a User role")

    user_datastore.create_user(
        username = "User1", password=hash_password("12345"), email="user1@gmail.com", roles=["admin"]
    )
    user_datastore.create_user(
        username = "User2", password=hash_password("12345"), email="user2@gmail.com", roles=["user"]
    )
    db.session.commit()

