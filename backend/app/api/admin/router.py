# app/api/admin/router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import get_current_admin
from app.crud import user as crud_user, student as crud_student, teacher as crud_teacher

router = APIRouter()

@router.get("/users")
def list_users(db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return crud_user.get_all_users(db)
