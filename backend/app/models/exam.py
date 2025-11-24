# app/models/exam.py
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base

class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    date = Column(DateTime, nullable=True)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    marks = relationship("Mark", back_populates="exam", cascade="all, delete-orphan")
