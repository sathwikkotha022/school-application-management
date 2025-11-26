from fastapi import APIRouter

# Auth
from app.api.auth.router import router as auth_router

# Admin
from app.api.admin.router import router as admin_router
from app.api.admin.attendance import router as admin_attendance_router
from app.api.admin.academic import router as academic_router

# Student
from app.api.student.router import router as student_router
from app.api.student.marks import router as student_marks_router
from app.api.student.attendance import router as student_attendance_router

# Teacher
from app.api.teacher.router import router as teacher_router
from app.api.teacher.marks import router as teacher_marks_router
from app.api.teacher.classes import router as teacher_classes_router
from app.api.teacher.attendance import router as teacher_attendance_router
from app.api.teacher.teacher_subjects import router as teacher_subjects_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(admin_router, prefix="/admin", tags=["Admin"])
router.include_router(admin_attendance_router)
router.include_router(academic_router)

router.include_router(student_router, prefix="/student", tags=["Student"])
router.include_router(student_marks_router, prefix="/student/marks", tags=["Student Marks"])
router.include_router(student_attendance_router, prefix="/student/attendance", tags=["Student Attendance"])

router.include_router(teacher_router, prefix="/teacher", tags=["Teacher"])
router.include_router(teacher_marks_router, prefix="/teacher/marks", tags=["Teacher Marks"])
router.include_router(teacher_classes_router, prefix="/teacher/classes", tags=["Teacher Classes"])
router.include_router(teacher_attendance_router, prefix="/teacher/attendance", tags=["Teacher Attendance"])
router.include_router(teacher_subjects_router, prefix="/teacher", tags=["Teacher Subjects"])
