# app/crud/user.py
from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, username: str, email: str, password_hash: str,
                first_name=None, last_name=None, role="student", commit=True):
    u = User(
        username=username,
        email=email,
        password_hash=password_hash,
        first_name=first_name,
        last_name=last_name,
        role=role
    )
    db.add(u)
    if commit:
        db.commit()
        db.refresh(u)
    return u


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()
