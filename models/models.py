"""
models.py - Data models for the Todo API Application


Author: Matthew Sunner, 2022
"""

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import os

from app import app

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)


class User(db.Model):
    """User - User database model schema

    Args:
        db (object): SQLAlchemy Model Base
    """
    
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String, nullable=False)
    firstt_name = db.Column(db.String, nullable=False)
    
    # Login Credentials
    user_name = db.Column(db.String, unique=True, nullable=False)
    user_pass = db.Column(db.String, nullable=False)