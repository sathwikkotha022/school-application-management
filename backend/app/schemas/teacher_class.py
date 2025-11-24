# app/schemas/teacher_class.py
from pydantic import BaseModel
from typing import Optional

class TeacherClassAssign(BaseModel):
    teacher_id: int
    subject_id: int
    class_id: Optional[int] = None
    section_id: Optional[int] = None

    class Config:
        from_attributes = True
