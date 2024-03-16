from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

roles_users = db.Table('roles_users', 
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')), 
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                    )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users'))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
