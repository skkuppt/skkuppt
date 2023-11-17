from passlib.context import CryptContext
from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate, UserDelete
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user_create: UserCreate):
    db_user = User(username=user_create.username,
                   password=pwd_context.hash(user_create.password1),
                   email=user_create.email)
    db.add(db_user) 
    db.commit()

def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first()

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def delete_user(db: Session, user_delete: UserDelete):
    db_user = db.query(User).filter(User.username == user_delete.username).first()
    if not db_user:
        return False
    if not pwd_context.verify(user_delete.password, db_user.password):
        return False
    db.delete(db_user)
    db.commit()
    return True