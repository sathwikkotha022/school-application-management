# app/crud/marks.py
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from app.models.marks import Marks  # Adjust if your model name is different

from app import models
from app.schemas import marks as marks_schemas

def create_or_update_mark(db: Session, payload: marks_schemas.MarkCreate, teacher_id: Optional[int] = None) -> models.Mark:
    """
    Create new mark row or update existing if same student-exam-subject-class-section exists.
    Teacher_id is optional and stored if provided.
    """
    existing = db.query(models.Mark).filter(
        models.Mark.student_id == payload.student_id,
        models.Mark.exam_id == payload.exam_id,
        models.Mark.subject_id == payload.subject_id,
        models.Mark.class_id == payload.class_id,
        models.Mark.section_id == payload.section_id
    ).first()

    if existing:
        if payload.marks_obtained is not None:
            existing.marks_obtained = payload.marks_obtained
        if payload.grade is not None:
            existing.grade = payload.grade
        if payload.remarks is not None:
            existing.remarks = payload.remarks
        if teacher_id:
            existing.teacher_id = teacher_id
        db.add(existing)
        db.commit()
        db.refresh(existing)
        return existing

    db_obj = models.Mark(
        student_id=payload.student_id,
        teacher_id=teacher_id,
        subject_id=payload.subject_id,
        class_id=payload.class_id,
        section_id=payload.section_id,
        exam_id=payload.exam_id,
        marks_obtained=payload.marks_obtained,
        grade=payload.grade,
        remarks=payload.remarks
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_marks_for_student(db: Session, student_id: int, skip: int = 0, limit: int = 200) -> List[models.Mark]:
    return db.query(models.Mark).filter(models.Mark.student_id == student_id).order_by(models.Mark.created_at.desc()).offset(skip).limit(limit).all()

def get_marks_for_class_subject_exam(db: Session, class_id: int, subject_id: int, exam_id: int, section_id: Optional[int] = None) -> List[models.Mark]:
    q = db.query(models.Mark).filter(
        models.Mark.class_id == class_id,
        models.Mark.subject_id == subject_id,
        models.Mark.exam_id == exam_id
    )
    if section_id is not None:
        q = q.filter(models.Mark.section_id == section_id)
    return q.order_by(models.Mark.marks_obtained.desc()).all()

def filter_marks_by_grade(db: Session, subject_id: int, exam_id: int, grade: str, class_id: Optional[int] = None, section_id: Optional[int] = None) -> List[models.Mark]:
    q = db.query(models.Mark).filter(
        models.Mark.subject_id == subject_id,
        models.Mark.exam_id == exam_id,
        models.Mark.grade == grade
    )
    if class_id is not None:
        q = q.filter(models.Mark.class_id == class_id)
    if section_id is not None:
        q = q.filter(models.Mark.section_id == section_id)
    return q.order_by(models.Mark.marks_obtained.desc()).all()

def get_marks_for_teacher(db: Session, teacher_id: int, skip: int = 0, limit: int = 200) -> List[models.Mark]:
    return db.query(models.Mark).filter(models.Mark.teacher_id == teacher_id).order_by(models.Mark.created_at.desc()).offset(skip).limit(limit).all()

def delete_mark(db: Session, mark_id: int) -> bool:
    obj = db.query(models.Mark).filter(models.Mark.id == mark_id).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
def get_student_marks(db: Session, student_id: int):
    return db.query(Marks).filter(Marks.student_id == student_id).all()