from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base


class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    name = Column(String(10), nullable=False)  # "A", "B"

    school_class = relationship("SchoolClass", back_populates="sections")
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
