# app/schemas/subject.py
from pydantic import BaseModel
from typing import Optional

class SubjectBase(BaseModel):
    name: str

    class Config:
        from_attributes = True

class SubjectCreate(SubjectBase):
    pass

class SubjectOut(SubjectBase):
    id: int
