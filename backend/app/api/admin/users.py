# app/api/admin/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app import models
from app.core.security import get_current_active_user
from app.schemas import user as user_schemas  # assuming you already have this

router = APIRouter(prefix="/admin", tags=["admin"])

def ensure_admin(user: models.User):
    if user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")

@router.get("/students", response_model=List[user_schemas.UserOut])  # adapt to your user schema
def list_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    # query users joined with student table
    q = db.query(models.User).join(models.Student).filter(models.User.role == "student").offset(skip).limit(limit)
    return q.all()

@router.get("/teachers", response_model=List[user_schemas.UserOut])
def list_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    q = db.query(models.User).join(models.Teacher).filter(models.User.role == "teacher").offset(skip).limit(limit)
    return q.all()
