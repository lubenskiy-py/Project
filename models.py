from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from enum import Enum



db = SQLAlchemy()

class Role(Enum):
    WORKER = 'worker'
    MANAGER = 'manager'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    surname = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    role = db.Column(db.String, nullable = False)
    portfolio = db.relationship('Portfolio', backref='user', lazy=True)


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False, unique = True)
    position = db.Column(db.String(150), nullable = False)
    category = db.Column(db.String(150), nullable = False)
    country = db.Column(db.String(100), nullable = False)
    work_exp = db.Column(db.Integer, nullable = True, default = 0)
    salary_expectation = db.Column(db.Integer, nullable = False)
    english_level = db.Column(db.String(50), nullable = False)
    skills = db.Column(db.Text, nullable = False)
    knowledge_ukrainian = db.Column(db.Boolean, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
