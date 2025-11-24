# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = "student"
    is_active: Optional[bool] = True

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
