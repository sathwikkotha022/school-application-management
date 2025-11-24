# app/crud/marks.py
from sqlalchemy.orm import Session
from app.models.marks import Mark

def create_or_update_mark(db: Session, payload, teacher_id: int = None):
    # payload is expected to be a MarkCreate-like object/dict
    existing = db.query(Mark).filter(
        Mark.student_id == payload.student_id,
        Mark.subject_id == payload.subject_id,
        Mark.exam_id == payload.exam_id
    ).first()

    if existing:
        existing.marks_obtained = payload.marks_obtained
        existing.max_marks = payload.max_marks
        existing.teacher_id = teacher_id or payload.teacher_id
        db.commit()
        db.refresh(existing)
        return existing

    m = Mark(
        student_id=payload.student_id,
        subject_id=payload.subject_id,
        exam_id=payload.exam_id,
        marks_obtained=payload.marks_obtained,
        max_marks=payload.max_marks,
        teacher_id=teacher_id or payload.teacher_id,
        class_id=payload.class_id,
        section_id=payload.section_id
    )
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

def get_marks_for_student(db: Session, student_id: int, exam_id: int = None):
    q = db.query(Mark).filter(Mark.student_id == student_id)
    if exam_id:
        q = q.filter(Mark.exam_id == exam_id)
    return q.all()

def delete_mark(db: Session, mark_id: int):
    m = db.query(Mark).filter(Mark.id == mark_id).first()
    if m:
        db.delete(m)
        db.commit()
        return True
    return False
