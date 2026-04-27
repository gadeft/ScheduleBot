from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)

    student: Mapped["Student"] = relationship(back_populates="user", uselist=False)
    lecturer: Mapped["Lecturer"] = relationship(back_populates="user", uselist=False)


class Student(Base):
    __tablename__ = "students"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )

    group_id: Mapped[int]

    user: Mapped["User"] = relationship(back_populates="student")


class Lecturer(Base):
    __tablename__ = "lecturers"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )

    lecturer_id: Mapped[int]

    user: Mapped["User"] = relationship(back_populates="lecturer")


