# app/crud/student.py
from sqlalchemy.orm import Session
from app.models.student import Student

def create_student(db: Session, user_id: int, roll_number: str, class_id: int, section_id: int):
    s = Student(user_id=user_id, roll_number=roll_number, class_id=class_id, section_id=section_id)
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def get_student_by_user_id(db: Session, user_id: int):
    return db.query(Student).filter(Student.user_id == user_id).first()
