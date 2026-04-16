FACULTIES = ["ИПЗ", "ОПИ", "КН", "ПМ"]

COURSES = [1, 2, 3, 4]

GROUPS_PER_COURSE = [1, 2, 3, 4, 5]

TEACHERS = [
    "Иванов", "Петров", "Петриченко", "Петрова", "Сидоров",
    "Коваленко", "Бондаренко",
    "Шевченко", "Ткаченко",
]


TEXT = {
    "choose_role": "Хто Ви?",

    "choose_faculty": "Оберіть спеціальність",
    "choose_course": "Оберіть курс",
    "choose_group": "Оберіть групу",

    "search_teacher": "Введіть прізвище викладача",
    "choose_teacher": "Оберіть викладача з перечислених",
    "not_found_teacher": "Викладача не знайдено. Спробуйте ще раз",
}

TEXT_TEMPLATES = {
    "role": "{0}",
    "faculty": "{0}",
    "course": "Курс {0}",
    "group": "{1}-{2}{0}",
    "choose_teacher": "{0}",
}


def student_finish_text(faculty, course, group_number):
    text = f"<b>Реєстрацію завершено</b>\nВи студент групи <b>{faculty}-{course}{group_number}</b>"
    return text

def teacher_finish_text(surname):
    text = f"<b>Реєстрацію завершено</b>\nВи викладач\nВаше прізвище: <b>{surname}</b>"
    return text
