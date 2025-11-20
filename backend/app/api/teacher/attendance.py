# app/api/teacher/attendance.py
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


# --------------------------
# Helper to ensure teacher role
# --------------------------
def ensure_teacher(user: models.User):
    if user.role not in ["teacher", "admin"] or not user.teacher:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Teacher credentials required"
        )


# --------------------------
# Mark student attendance
# --------------------------
@router.post("/mark", response_model=sa_schemas.StudentAttendanceOut)
def mark_student_attendance(
    payload: sa_schemas.StudentAttendanceCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_teacher(current_user)
    payload.teacher_id = current_user.teacher.id
    created = crud_sa.create_student_attendance(db, payload)
    return created


# --------------------------
# Update student attendance
# --------------------------
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


# --------------------------
# Teacher login
# --------------------------
@router.post("/login", response_model=ta_schemas.TeacherAttendanceOut)
def teacher_login(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_teacher(current_user)
    today = date.today()
    ta = crud_ta.create_teacher_login(
        db, current_user.teacher.id, today, login_time=datetime.utcnow()
    )
    return ta


# --------------------------
# Teacher logout
# --------------------------
@router.post("/logout", response_model=ta_schemas.TeacherAttendanceOut)
def teacher_logout(
    attendance_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_teacher(current_user)
    ta = crud_ta.end_teacher_shift(db, attendance_id, logout_time=datetime.utcnow())
    if not ta:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return ta


# --------------------------
# Get my teacher attendance records
# --------------------------
@router.get("/my", response_model=List[ta_schemas.TeacherAttendanceOut])
def get_my_attendance(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_teacher(current_user)
    q = db.query(models.TeacherAttendance).filter(
        models.TeacherAttendance.teacher_id == current_user.teacher.id
    )
    return q.order_by(models.TeacherAttendance.date.desc()).offset(skip).limit(limit).all()
