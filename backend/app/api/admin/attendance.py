# app/api/admin/attendance.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List
from app.database import get_db
from app import models
from app.core.security import get_current_active_user

router = APIRouter(prefix="/admin/attendance", tags=["admin-attendance"])

def ensure_admin(user: models.User):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")


# ---------------------------------------------------
# ADMIN → GET STUDENT ATTENDANCE
# ---------------------------------------------------
@router.get("/students")
def admin_get_student_attendance(
    student_id: Optional[int] = None,
    class_id: Optional[int] = None,
    section_id: Optional[int] = None,
    date: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_admin(current_user)

    query = db.query(models.StudentAttendance)

    if student_id:
        query = query.filter(models.StudentAttendance.student_id == student_id)

    if class_id:
        query = query.filter(models.StudentAttendance.class_id == class_id)

    if section_id:
        query = query.filter(models.StudentAttendance.section_id == section_id)

    if date:
        query = query.filter(models.StudentAttendance.date == date)

    return query.all()


# ---------------------------------------------------
# ADMIN → GET TEACHER ATTENDANCE
# ---------------------------------------------------
@router.get("/teachers")
def admin_get_teacher_attendance(
    teacher_id: Optional[int] = None,
    date: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    ensure_admin(current_user)

    query = db.query(models.TeacherAttendance)

    if teacher_id:
        query = query.filter(models.TeacherAttendance.teacher_id == teacher_id)

    if date:
        query = query.filter(models.TeacherAttendance.date == date)

    return query.all()
