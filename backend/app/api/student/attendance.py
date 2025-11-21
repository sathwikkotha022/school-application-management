from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import date

from app.database import get_db
from app.core.security import get_current_user
from app import models
from app.schemas import student_attendance as sa_schemas
from app.crud import student_attendance as crud_sa

# Prefix handled in api/router.py
router = APIRouter(tags=["Student Attendance"])

def ensure_student(user: models.User):
    """
    Validates that the logged-in user is a student.
    Admins are allowed to access student APIs as well.
    """
    if user.role not in ["student", "admin"] or (user.role == "student" and not user.student):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student credentials required",
        )

@router.get("/my", response_model=List[sa_schemas.StudentAttendanceOut])
def get_my_attendance(
    skip: int = 0,
    limit: int = 200,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    ensure_student(current_user)

    # Use actual student ID or dummy for admin
    if current_user.role == "admin" and not current_user.student:
        # Optional: admin can only view student 0 (or create dummy student)
        student_id = 0
    else:
        student_id = current_user.student.id

    return crud_sa.get_attendances_for_student(db, student_id, skip, limit)
