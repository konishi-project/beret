# CRUD Database service.
db = None # Temporary

from .model import User
from .schemas import UserCreate

def get_user(username: str):
    return db.session.query(User).filter_by(username=username).first()

def get_user_by_email(email: str):
    return db.session.query(User).filter_by(email=email).first()

def delete_user(email: str):
    return db.session.query(User).filter_by(email=email).first()