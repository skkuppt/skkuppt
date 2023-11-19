from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True) 
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

class Question(Base):
    __tablename__ = "question"

    id=Column(Integer, primary_key=True)
    topic=Column(Text, nullable=False)
    content=Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", backref="question_users")
