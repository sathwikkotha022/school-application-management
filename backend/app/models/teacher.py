# app/models/teacher.py
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    employee_id = Column(String(20), unique=True, index=True)
    qualification = Column(String(255))
    phone = Column(String(20))
    status = Column(Enum('active', 'inactive', 'on_leave'), default='active', index=True)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP"))

    user = relationship("User", back_populates="teacher")
    teacher_subjects = relationship("TeacherSubject", back_populates="teacher", cascade="all, delete-orphan")
    teacher_classes = relationship("TeacherClass", back_populates="teacher", cascade="all, delete-orphan")
