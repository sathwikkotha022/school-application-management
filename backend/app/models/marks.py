# app/models/mark.py
from sqlalchemy import Column, Integer, Float, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base

class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)
    class_id = Column(Integer, ForeignKey("school_classes.id"), nullable=True)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=True)
    marks_obtained = Column(Float, nullable=False, default=0.0)
    max_marks = Column(Float, nullable=True)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    student = relationship("Student")
    subject = relationship("Subject")
    exam = relationship("Exam", back_populates="marks")
    teacher = relationship("Teacher")
