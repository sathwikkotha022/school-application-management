from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.teacher_subject import TeacherSubjectCreate, TeacherSubjectOut
from app.crud.teacher_subject import assign_subject_to_teacher, get_teacher_subjects
from app.api.auth.teacher_auth import get_current_teacher

router = APIRouter(tags=["Teacher Subjects"])

@router.post("/assign", response_model=TeacherSubjectOut)
def assign_subject(ts: TeacherSubjectCreate, db: Session = Depends(get_db)):
    return assign_subject_to_teacher(db, ts)

@router.get("/my-subjects", response_model=list[TeacherSubjectOut])
def my_subjects(db: Session = Depends(get_db), current_teacher = Depends(get_current_teacher)):
    return get_teacher_subjects(db, current_teacher.id)
