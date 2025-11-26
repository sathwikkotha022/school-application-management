from sqlalchemy.orm import Session
from app.models.subject import Subject

def get_subject(db: Session, subject_id: int):
    return db.query(Subject).filter(Subject.id == subject_id).first()
