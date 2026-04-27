from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User, Student, Lecturer


# async def get_user_by_tg(session: AsyncSession, telegram_id: int):
#     result = await session.execute(
#         select(User).where(User.telegram_id == telegram_id)
#     )
#     return result.scalar_one_or_none()


async def get_user_by_tg(session: AsyncSession, telegram_id: int):
    result = await session.execute(
        select(User)
        .options(
            selectinload(User.student),
            selectinload(User.lecturer),
        )
        .where(User.telegram_id == telegram_id)
    )
    return result.scalar_one_or_none()


async def get_or_create_user(session: AsyncSession, telegram_id: int):
    user = await get_user_by_tg(session, telegram_id)

    if user:
        return user

    user = User(telegram_id=telegram_id)
    session.add(user)
    # await session.commit()
    return user


# async def register_student(session: AsyncSession, telegram_id: int, group_id: int):
#     user = await get_or_create_user(session, telegram_id)
#
#     # проверяем что не преподаватель
#     if user.lecturer:
#         raise Exception("User already lecturer")
#
#     if user.student:
#         return user.student
#
#     student = Student(user_id=user.id, group_id=group_id)
#     session.add(student)
#     # await session.commit()
#
#     return student
#
#
# async def register_lecturer(session: AsyncSession, telegram_id: int, lecturer_id: int):
#     user = await get_or_create_user(session, telegram_id)
#
#     if user.student:
#         raise Exception("User already student")
#
#     if user.lecturer:
#         return user.lecturer
#
#     lecturer = Lecturer(user_id=user.id, lecturer_id=lecturer_id)
#     session.add(lecturer)
#     # await session.commit()
#
#     return lecturer


async def make_user_lecturer(
    session: AsyncSession,
    telegram_id: int,
    lecturer_id: int
):
    user = await get_or_create_user(session, telegram_id)

    # если уже преподаватель — ничего не делаем
    if user.lecturer:
        return user.lecturer

    # если был студент → удаляем
    if user.student:
        await session.execute(
            delete(Student).where(Student.user_id == user.id)
        )

    lecturer = Lecturer(
        user_id=user.id,
        lecturer_id=lecturer_id
    )

    session.add(lecturer)
    return lecturer


async def make_user_student(
    session: AsyncSession,
    telegram_id: int,
    group_id: int
):
    user = await get_or_create_user(session, telegram_id)

    if user.student:
        return user.student

    # если был преподаватель → удаляем
    if user.lecturer:
        await session.execute(
            delete(Lecturer).where(Lecturer.user_id == user.id)
        )

    student = Student(
        user_id=user.id,
        group_id=group_id
    )

    session.add(student)
    return student