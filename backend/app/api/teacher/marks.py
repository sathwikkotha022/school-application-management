# app/api/teacher/marks.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.core.security import get_current_active_user
from app import models
from app.schemas import marks as marks_schemas
from app.crud import marks as crud_marks

router = APIRouter(prefix="/teacher/marks", tags=["teacher-marks"])

def ensure_teacher_or_admin(user: models.User):
    if user.role not in ["teacher", "admin"]:
        raise HTTPException(status_code=403, detail="Teacher or admin required")

@router.post("/add", response_model=marks_schemas.MarkOut)
def add_mark(payload: marks_schemas.MarkCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_teacher_or_admin(current_user)
    teacher_id = current_user.teacher.id if current_user.role == "teacher" else None
    return crud_marks.create_or_update_mark(db, payload, teacher_id=teacher_id)

@router.put("/update/{mark_id}", response_model=marks_schemas.MarkOut)
def update_mark(mark_id: int, updates: marks_schemas.MarkUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_teacher_or_admin(current_user)
    obj = db.query(models.Mark).filter(models.Mark.id == mark_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Mark not found")
    if updates.marks_obtained is not None:
        obj.marks_obtained = updates.marks_obtained
    if updates.grade is not None:
        obj.grade = updates.grade
    if updates.remarks is not None:
        obj.remarks = updates.remarks
    db.commit(); db.refresh(obj)
    return obj

@router.get("/filter", response_model=List[marks_schemas.MarkOut])
def filter_marks(subject_id: Optional[int] = None, grade: Optional[str] = None, exam_id: Optional[int] = None, class_id: Optional[int] = None, section_id: Optional[int] = None, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_teacher_or_admin(current_user)
    return crud_marks.filter_marks(db, subject_id=subject_id, grade=grade, exam_id=exam_id, class_id=class_id, section_id=section_id)
