# app/schemas/exam.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ExamBase(BaseModel):
    name: str
    date: Optional[datetime] = None

    class Config:
        from_attributes = True

class ExamCreate(ExamBase):
    pass

class ExamOut(ExamBase):
    id: int
