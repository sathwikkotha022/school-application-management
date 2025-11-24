# app/api/teacher/marks.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import get_current_teacher
from app.crud import marks as crud_marks
from app.schemas.marks import MarkCreate, MarkOut

router = APIRouter(prefix="/marks", tags=["teacher-marks"])

@router.post("/", response_model=MarkOut)
def create_mark(payload: MarkCreate, db: Session = Depends(get_db), current_teacher = Depends(get_current_teacher)):
    return crud_marks.create_or_update_mark(db, payload, teacher_id=current_teacher.id)
