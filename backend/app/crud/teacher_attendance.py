# app/crud/teacher_attendance.py
from sqlalchemy.orm import Session
from datetime import datetime, date
from typing import Optional

from app import models
from app.schemas import teacher_attendance as schemas

def create_teacher_login(db, teacher_id, date, login_time=None):
    from app.models import TeacherAttendance
    
    ta = TeacherAttendance(
        teacher_id=teacher_id,
        date=date,
        login_time=login_time or datetime.utcnow(),  # FULL DATETIME ✔
    )
    db.add(ta)
    db.commit()
    db.refresh(ta)
    return ta

def end_teacher_shift(db: Session, attendance_id: int, logout_time: Optional[datetime] = None):
    obj = db.query(models.TeacherAttendance).filter(models.TeacherAttendance.id == attendance_id).first()
    if not obj:
        return None
    if logout_time is None:
        logout_time=datetime.utcnow()
    obj.logout_time = logout_time
    # optional: compute total_hours as a simple string difference (you can compute float hours later)
    try:
        if obj.login_time and obj.logout_time:
            delta = obj.logout_time - obj.login_time
            hours = delta.total_seconds() / 3600.0
            obj.total_hours = f"{hours:.2f}"
    except Exception:
        obj.total_hours = None
    db.commit()
    db.refresh(obj)
    return obj

def get_latest_teacher_attendance(db: Session, teacher_id: int):
    return db.query(models.TeacherAttendance).filter(models.TeacherAttendance.teacher_id == teacher_id).order_by(
        models.TeacherAttendance.id.desc()
    ).first()

def get_attendance_for_teacher_on_date(db: Session, teacher_id: int, date_value: date):
    return db.query(models.TeacherAttendance).filter(models.TeacherAttendance.teacher_id == teacher_id,
                                                    models.TeacherAttendance.date == date_value).all()
