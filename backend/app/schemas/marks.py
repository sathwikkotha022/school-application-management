# app/schemas/marks.py
from pydantic import BaseModel
from typing import Optional

class MarkCreate(BaseModel):
    student_id: int
    subject_id: int
    exam_id: int
    marks_obtained: float
    max_marks: Optional[float] = None
    teacher_id: Optional[int] = None
    class_id: Optional[int] = None
    section_id: Optional[int] = None

    class Config:
        from_attributes = True

class MarkOut(MarkCreate):
    id: int
