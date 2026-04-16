from aiogram.filters.callback_data import CallbackData


class RoleCD(CallbackData, prefix="role"):
    value: str

class FacultyCD(CallbackData, prefix="faculty"):
    value: str

class CourseCD(CallbackData, prefix="course"):
    value: int

class GroupNumberCD(CallbackData, prefix="group_number"):
    value: int

class TeacherCD(CallbackData, prefix="teacher"):
    value: str