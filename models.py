from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(40))
    nickname = Column(String(40))
    password = Column(String(100))
    admin = Column(Boolean, default=False)


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60))
    bazl_number = Column(Integer)
    description = Column(String(100))
    content = Column(String(2000))
    date = Column(Date, default=datetime.datetime.utcnow)
