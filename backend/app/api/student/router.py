from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.marks import get_student_marks  # Make sure function name matches exactly

router = APIRouter(tags=["Student"])

@router.get("/marks/{student_id}")
def student_marks(student_id: int, db: Session = Depends(get_db)):
    return get_student_marks(db, student_id)
