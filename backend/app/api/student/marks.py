# app/api/student/marks.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List
from app.database import get_db
from app.core.security import get_current_user
from app import models
from app.schemas import marks as marks_schemas
from app.crud import marks as crud_marks

router = APIRouter(prefix="/student/marks", tags=["student-marks"])

def ensure_student_or_admin(user: models.User):
    if user.role not in ["student", "admin"]:
        raise HTTPException(status_code=403, detail="Student or admin required")

@router.get("/my", response_model=List[marks_schemas.MarkOut])
def my_marks(exam_id: Optional[int] = None, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    ensure_student_or_admin(current_user)
    student_id = current_user.student.id if current_user.role == "student" else None
    if current_user.role == "admin" and student_id is None:
        raise HTTPException(status_code=400, detail="Admin must supply student_id query")
    return crud_marks.get_marks_for_student(db, student_id, exam_id=exam_id)
