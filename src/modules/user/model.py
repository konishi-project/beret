from sqlalchemy import Boolean, Column, Integer, String
from src.middleware.orm import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)

    username = Column(String(15), unique=True, index=True)
    fullName = Column(String(50), nullable=True)
    hashed_password = Column(String)
