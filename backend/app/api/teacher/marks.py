# app/api/teacher/marks.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import get_current_teacher
from app.crud import marks as crud_marks
from app.crud import student as crud_student
from app.crud import subject as crud_subject
from app.crud import exam as crud_exam
from app.crud import teacher as crud_teacher
from app.schemas.marks import MarkCreate, MarkOut

router = APIRouter(prefix="", tags=["teacher-marks"])

@router.post("/", response_model=MarkOut)
def create_mark(payload: MarkCreate, db: Session = Depends(get_db), current_teacher = Depends(get_current_teacher)):
    # Check if student exists
    student = crud_student.get_student(db, payload.student_id)
    if not student:
        raise HTTPException(status_code=400, detail="Student not found")
    # Check if subject exists
    subject = crud_subject.get_subject(db, payload.subject_id)
    if not subject:
        raise HTTPException(status_code=400, detail="Subject not found")
    # Check if exam exists
    exam = crud_exam.get_exam(db, payload.exam_id)
    if not exam:
        raise HTTPException(status_code=400, detail="Exam not found")
    # Get teacher record
    teacher = crud_teacher.get_teacher_by_user_id(db, current_teacher.id)
    if not teacher:
        raise HTTPException(status_code=400, detail="Teacher not found")
    return crud_marks.create_or_update_mark(db, payload, teacher_id=teacher.id)
