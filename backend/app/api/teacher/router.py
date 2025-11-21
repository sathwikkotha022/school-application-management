from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.marks import MarkOut, MarkCreate
from app.crud.marks import add_mark, get_teacher_marks
from app.api.auth.router import get_current_user

router = APIRouter(tags=["Teacher"])

@router.post("/marks", response_model=MarkOut)
def create_mark(mark: MarkCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return add_mark(db, mark, current_user.id)

@router.get("/marks", response_model=list[MarkOut])
def my_marks(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_teacher_marks(db, current_user.id)
