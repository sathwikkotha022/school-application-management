# app/api/teacher/router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import get_current_user, get_current_teacher
from app.crud import teacher as crud_teacher
from app.schemas.teacher import TeacherOut, TeacherCreate

router = APIRouter()

@router.get("/me", response_model=TeacherOut)
def me(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    t = crud_teacher.get_teacher_by_user_id(db, current_user.id)
    if not t:
        raise HTTPException(status_code=404, detail="Teacher profile not found")
    return t

@router.post("/", response_model=TeacherOut)
def create_teacher(payload: TeacherCreate, db: Session = Depends(get_db)):
    return crud_teacher.create_teacher(db, payload)
