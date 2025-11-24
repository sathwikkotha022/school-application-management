# app/schemas/student.py
from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    user_id: int
    roll_number: Optional[str]
    class_id: Optional[int]
    section_id: Optional[int]

    class Config:
        from_attributes = True

class StudentCreate(BaseModel):
    user_id: int
    roll_number: str
    class_id: int
    section_id: int


    class Config:
        from_attributes = True

class StudentOut(StudentBase):
    id: int
