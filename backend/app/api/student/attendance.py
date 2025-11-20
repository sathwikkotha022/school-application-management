from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import date

from app.database import get_db
from app.core.security import get_current_user
from app import models
from app.schemas import student_attendance as sa_schemas
from app.crud import student_attendance as crud_sa

# ✅ Remove prefix here; it's added in api/router.py
router = APIRouter(tags=["Student Attendance"])

def ensure_student(user: models.User):
    """
    Validates that the logged-in user is a student.
    """
    if user.role != "student" or not user.student:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student credentials required",
        )

# ===============================
# Get my attendance
# ===============================
@router.get("/my", response_model=List[sa_schemas.StudentAttendanceOut])
def get_my_attendance(
    skip: int = 0,
    limit: int = 200,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    ensure_student(current_user)
    student_id = current_user.student.id
    return crud_sa.get_attendances_for_student(db, student_id, skip, limit)
