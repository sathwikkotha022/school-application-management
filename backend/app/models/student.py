# app/models/student.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(255))
    grade = Column(String(50))

    user = relationship("User", back_populates="student")
    # now points to StudentAttendance table
    attendance_records = relationship("StudentAttendance", back_populates="student", cascade="all, delete-orphan")
