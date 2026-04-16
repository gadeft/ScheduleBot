from src.handlers.register.roles.student import choose_faculty
from src.handlers.register.roles.teacher import search_teacher

ROLES = ["студент", "викладач"]

FUNCTIONS_ROLES = {
    "студент": choose_faculty,
    "викладач": search_teacher,
}