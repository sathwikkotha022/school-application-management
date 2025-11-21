# app/crud/user.py
from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.user import User

from app import models
from app.schemas import user as user_schemas
from app.core.security import hash_password
def get_all_users(db: Session):
    return db.query(User).all()
def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.username == username).first()

def list_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, *, username: str, email: str, password: str,
                first_name: str, last_name: str, role: str = "student", is_active: bool = True) -> models.User:
    """
    Creates a User. Password will be hashed.
    """
    user = models.User(
        username=username,
        email=email,
        password_hash=hash_password(password),
        first_name=first_name,
        last_name=last_name,
        role=role,
        is_active=is_active
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user_password(db: Session, user: models.User, new_password: str) -> models.User:
    user.password_hash = hash_password(new_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user_email(db: Session, user: models.User, new_email: str) -> models.User:
    user.email = new_email
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def deactivate_user(db: Session, user: models.User) -> models.User:
    user.is_active = False
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
