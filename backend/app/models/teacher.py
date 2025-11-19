# app/models/teacher.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(255))
    subject = Column(String(100))  # simple subject string; later you can normalize into a subject table

    user = relationship("User", back_populates="teacher")
    # relations for attendance
    attendance_records = relationship("TeacherAttendance", back_populates="teacher", cascade="all, delete-orphan")
    student_attendance_records = relationship("StudentAttendance", back_populates="teacher")
