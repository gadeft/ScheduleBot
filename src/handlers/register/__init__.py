from aiogram import Router

from .roles.student import router as student_router
from .roles.teacher import router as teacher_router
from .role_selection import router as role_selection_router


router = Router()
router.include_router(role_selection_router)
router.include_router(student_router)
router.include_router(teacher_router)