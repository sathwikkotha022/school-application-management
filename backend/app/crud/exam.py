# app/crud/exam.py
from sqlalchemy.orm import Session
from app.models.exam import Exam

def create_exam(db: Session, name: str, date=None):
    e = Exam(name=name, date=date)
    db.add(e)
    db.commit()
    db.refresh(e)
    return e

def get_exam(db: Session, exam_id: int):
    return db.query(Exam).filter(Exam.id == exam_id).first()
