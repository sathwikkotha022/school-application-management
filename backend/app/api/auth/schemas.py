from pydantic import BaseModel

class RegisterTeacher(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    name: str
    subject: str

class RegisterStudent(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    name: str
    grade: str

class Login(BaseModel):
    email: str
    password: str
