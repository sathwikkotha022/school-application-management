# app/api/router.py
from fastapi import APIRouter

# Import sub-routers
from app.api.admin.router import router as admin_router
from app.api.auth.router import router as auth_router
from app.api.student.router import router as student_router
from app.api.teacher.router import router as teacher_router

# Main API router
router = APIRouter()

# Include all sub-routers with prefixes
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(admin_router, prefix="/admin", tags=["Admin"])
router.include_router(student_router, prefix="/student", tags=["Student"])
router.include_router(teacher_router, prefix="/teacher", tags=["Teacher"])
