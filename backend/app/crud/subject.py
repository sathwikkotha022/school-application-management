# app/crud/subject.py
from sqlalchemy.orm import Session
from app.models.subject import Subject

def create_subject(db: Session, name: str):
    s = Subject(name=name)
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

def get_subject(db: Session, subject_id: int):
    return db.query(Subject).filter(Subject.id == subject_id).first()

def list_subjects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Subject).offset(skip).limit(limit).all()
