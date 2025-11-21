from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MarkBase(BaseModel):
    student_id: int
    subject_id: int
    class_id: int
    section_id: int
    exam_id: int
    marks_obtained: Optional[float] = None
    grade: Optional[str] = None
    remarks: Optional[str] = None


class MarkCreate(MarkBase):
    pass


class MarkOut(MarkBase):
    id: int
    teacher_id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
