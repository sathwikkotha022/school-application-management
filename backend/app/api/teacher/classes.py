from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_teacher
from app.database import get_db
from app.crud.teacher_classes import get_teacher_classes

router = APIRouter(tags=["Teacher Classes"])

@router.get("/classes")
def get_classes_for_teacher(
    db: Session = Depends(get_db),
    current_teacher=Depends(get_current_teacher)
):
    return get_teacher_classes(db, current_teacher.id)
