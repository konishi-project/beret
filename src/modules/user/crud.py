# Database services
from sqlalchemy.orm import Session
from .model import User
from .schemas import UserCreate

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def delete_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()