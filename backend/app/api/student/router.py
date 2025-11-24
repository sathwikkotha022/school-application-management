# app/api/student/router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import get_current_user, get_current_student
from app.crud import student as crud_student
from app.schemas.student import StudentOut, StudentCreate

router = APIRouter()

@router.get("/me", response_model=StudentOut)
def me(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    student = crud_student.get_student_by_user_id(db, current_user.id)
    if not student:
        raise HTTPException(status_code=404, detail="Student profile not found")
    return student

@router.post("/", response_model=StudentOut)
def create_student(payload: StudentCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_student)):
    # you might only allow admin to create students - adjust as needed
    s = crud_student.create_student(db, user_id=payload.user_id, roll_number=payload.roll_number, class_id=payload.class_id, section_id=payload.section_id)
    return s
