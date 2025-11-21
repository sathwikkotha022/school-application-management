from sqlalchemy.orm import Session
from app.models.teacher_subject import TeacherSubject
from app.schemas.teacher_subject import TeacherSubjectCreate

def assign_subject_to_teacher(db: Session, ts: TeacherSubjectCreate):
    new_assignment = TeacherSubject(
        teacher_id=ts.teacher_id,
        subject_id=ts.subject_id,
        class_id=ts.class_id,
        section_id=ts.section_id
    )
    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)
    return new_assignment

def get_teacher_subjects(db: Session, teacher_id: int):
    return db.query(TeacherSubject).filter(TeacherSubject.teacher_id == teacher_id).all()

def get_subject_teachers(db: Session, subject_id: int):
    return db.query(TeacherSubject).filter(TeacherSubject.subject_id == subject_id).all()
