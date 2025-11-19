from fastapi import APIRouter

# Auth router
from app.api.auth.router import router as auth_router

# Attendance routers
from app.api.student.attendance import router as student_attendance_router
from app.api.teacher.attendance import router as teacher_attendance_router

# Admin router
from app.api.admin.users import router as admin_users_router


router = APIRouter()

router.include_router(auth_router, prefix="/auth")
router.include_router(student_attendance_router, prefix="/student-attendance")
router.include_router(teacher_attendance_router, prefix="/teacher-attendance")
router.include_router(admin_users_router, prefix="/admin")
