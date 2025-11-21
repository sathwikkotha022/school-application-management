from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import date, datetime

from app.database import get_db
from app.core.security import get_current_active_user
from app import models
from app.schemas import student_attendance as sa_schemas
from app.schemas import teacher_attendance as ta_schemas
from app.crud import student_attendance as crud_sa, teacher_attendance as crud_ta

router = APIRouter(tags=["Teacher Attendance"])

def ensure_teacher(user: models.User):
    """
    Validates that the logged-in user is a teacher.
    Admins are allowed to access teacher APIs as well.
    """
    if user.role not in ["teacher", "admin"] or (user.role == "teacher" and not user.teacher):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Teacher credentials required"
        )

@router.post("/mark", response_model=sa_schemas.StudentAttendanceOut)
def mark_student_attendance(
    payload: sa_schemas.StudentAttendanceCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_teacher(current_user)

    # Use teacher ID or dummy for admin
    if current_user.role == "admin" and not current_user.teacher:
        payload.teacher_id = None  # Admin can mark without teacher_id or use dummy
    else:
        payload.teacher_id = current_user.teacher.id

    created = crud_sa.create_student_attendance(db, payload)
    return created

@router.put("/{attendance_id}", response_model=sa_schemas.StudentAttendanceOut)
def update_student_attendance(
    attendance_id: int,
    updates: sa_schemas.StudentAttendanceUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_teacher(current_user)
    obj = crud_sa.update_student_attendance(db, attendance_id, updates)
    if not obj:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return obj

@router.post("/login", response_model=ta_schemas.TeacherAttendanceOut)
def teacher_login(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_teacher(current_user)
    teacher_id = current_user.teacher.id if current_user.teacher else None
    today = date.today()
    ta = crud_ta.create_teacher_login(db, teacher_id, today, login_time=datetime.utcnow())
    return ta

@router.post("/logout", response_model=ta_schemas.TeacherAttendanceOut)
def teacher_logout(
    attendance_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_teacher(current_user)
    teacher_id = current_user.teacher.id if current_user.teacher else None
    ta = crud_ta.end_teacher_shift(db, attendance_id, logout_time=datetime.utcnow())
    if not ta:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return ta

@router.get("/my", response_model=List[ta_schemas.TeacherAttendanceOut])
def get_my_attendance(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_teacher(current_user)
    teacher_id = current_user.teacher.id if current_user.teacher else None
    q = db.query(models.TeacherAttendance).filter(
        models.TeacherAttendance.teacher_id == teacher_id
    )
    return q.order_by(models.TeacherAttendance.date.desc()).offset(skip).limit(limit).all()
