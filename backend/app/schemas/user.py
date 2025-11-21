from pydantic import BaseModel, EmailStr
from typing import Optional


# ========== Base ==========
class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = "student"
    is_active: Optional[bool] = True


# ========== Create ==========
class UserCreate(UserBase):
    password: str


# ========== Update ==========
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


# ========== Output ==========
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
