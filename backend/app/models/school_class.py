from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base


class SchoolClass(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)  # "1st", "10th"

    sections = relationship("Section", back_populates="school_class", cascade="all, delete-orphan")
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
