# app/schemas/section.py
from pydantic import BaseModel
from typing import Optional

class SectionBase(BaseModel):
    name: str
    class_id: int

    class Config:
        from_attributes = True

class SectionCreate(SectionBase):
    pass

class SectionOut(SectionBase):
    id: int
