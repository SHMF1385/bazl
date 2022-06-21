from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date

from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(24))
    nickname = Column(String(24))
    password = Column(String(100))
    admin = Column(Boolean, default=False)

    tokens = relationship("Token", back_populates="user")

class Token(Base):
    __tablename__ = 'tokns'

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tokens")

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60))
    description = Column(String(100))
    content = Column(String(2000))
    date = Column(date)
