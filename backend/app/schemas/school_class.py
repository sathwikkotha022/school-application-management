# app/schemas/school_class.py
from pydantic import BaseModel
from typing import Optional, List

class SchoolClassBase(BaseModel):
    name: str

    class Config:
        from_attributes = True

class SchoolClassCreate(SchoolClassBase):
    pass

class SchoolClassOut(SchoolClassBase):
    id: int
