# app/crud/student_attendance.py
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from app import models
from app.schemas import student_attendance as schemas

def create_student_attendance(db: Session, attendance_in: schemas.StudentAttendanceCreate):
    # prevent duplicate entry for same student/date/period
    existing = db.query(models.StudentAttendance).filter(
        models.StudentAttendance.student_id == attendance_in.student_id,
        models.StudentAttendance.date == attendance_in.date,
        models.StudentAttendance.period == attendance_in.period,
    ).first()
    if existing:
        return existing

    db_obj = models.StudentAttendance(
        student_id=attendance_in.student_id,
        date=attendance_in.date,
        period=attendance_in.period,
        status=attendance_in.status,
        subject=attendance_in.subject,
        teacher_id=attendance_in.teacher_id,
        remarks=attendance_in.remarks
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_student_attendance(db: Session, attendance_id: int, updates: schemas.StudentAttendanceUpdate):
    obj = db.query(models.StudentAttendance).filter(models.StudentAttendance.id == attendance_id).first()
    if not obj:
        return None
    if updates.status is not None:
        obj.status = updates.status
    if updates.remarks is not None:
        obj.remarks = updates.remarks
    db.commit()
    db.refresh(obj)
    return obj

def get_attendances_for_student(db: Session, student_id: int, skip: int = 0, limit: int = 100) -> List[models.StudentAttendance]:
    return db.query(models.StudentAttendance).filter(models.StudentAttendance.student_id == student_id).order_by(
        models.StudentAttendance.date.desc(), models.StudentAttendance.period.asc()
    ).offset(skip).limit(limit).all()

def get_attendance_by_student_date_period(db: Session, student_id: int, date_value: date, period: int) -> Optional[models.StudentAttendance]:
    return db.query(models.StudentAttendance).filter(
        models.StudentAttendance.student_id == student_id,
        models.StudentAttendance.date == date_value,
        models.StudentAttendance.period == period
    ).first()

def get_attendances_for_date_and_class(db: Session, student_ids: list, date_value: date):
    return db.query(models.StudentAttendance).filter(models.StudentAttendance.student_id.in_(student_ids),
                                                   models.StudentAttendance.date == date_value).all()
