# app/crud/student_attendance.py
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from fastapi import HTTPException, status

from app import models
from app.schemas import student_attendance as schemas
from app.crud.student import get_student

def create_student_attendance(db: Session, attendance_in: schemas.StudentAttendanceCreate):
    # Check if student exists
    student = get_student(db, attendance_in.student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Student with id {attendance_in.student_id} does not exist"
        )

    # avoid duplicates for same student/date/period
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
    db.add(obj)
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

def bulk_create_student_attendance(db: Session, attendances_in: list[schemas.StudentAttendanceCreate]):
    created = []
    for attendance_in in attendances_in:
        # Check if student exists
        student = get_student(db, attendance_in.student_id)
        if not student:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Student with id {attendance_in.student_id} does not exist"
            )

        # avoid duplicates for same student/date/period
        existing = db.query(models.StudentAttendance).filter(
            models.StudentAttendance.student_id == attendance_in.student_id,
            models.StudentAttendance.date == attendance_in.date,
            models.StudentAttendance.period == attendance_in.period,
        ).first()
        if existing:
            created.append(existing)
            continue

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
        created.append(db_obj)
    db.commit()
    for obj in created:
        db.refresh(obj)
    return created

def assign_student_attendance_for_class(db: Session, assign_in: schemas.StudentAttendanceAssign):
    from app.crud.student import get_students_by_class_section
    from app.crud.subject import get_subject
    subject = get_subject(db, assign_in.subject_id)
    if not subject:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Subject with id {assign_in.subject_id} does not exist"
        )
    subject_name = subject.name
    students = get_students_by_class_section(db, assign_in.class_id, assign_in.section_id)
    attendances_in = []
    for student in students:
        attendance_in = schemas.StudentAttendanceCreate(
            student_id=student.id,
            date=assign_in.attendance_date,
            period=assign_in.period,
            status=assign_in.status,
            subject=subject_name,
            teacher_id=assign_in.teacher_id,
            remarks=assign_in.remarks
        )
        attendances_in.append(attendance_in)
    return bulk_create_student_attendance(db, attendances_in)
