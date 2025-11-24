# app/models/school_class.py
from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base

class SchoolClass(Base):
    __tablename__ = "school_classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)  # e.g., "1st", "10th"
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    sections = relationship("Section", back_populates="school_class", cascade="all, delete-orphan")
