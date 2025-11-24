# app/crud/teacher_subject.py
from sqlalchemy.orm import Session
from app.models.teacher_subject import TeacherSubject

def assign_subject_to_teacher(db: Session, teacher_id: int, subject_id: int, class_id: int = None, section_id: int = None):
    ts = TeacherSubject(teacher_id=teacher_id, subject_id=subject_id, class_id=class_id, section_id=section_id)
    db.add(ts)
    db.commit()
    db.refresh(ts)
    return ts

def get_teacher_subjects(db: Session, teacher_id: int):
    return db.query(TeacherSubject).filter(TeacherSubject.teacher_id == teacher_id).all()
