import asyncpg
import logging

from pydantic import BaseModel, Field, ConfigDict


class UserSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    telegram_id: int = Field(ge=0)


class StudentSchema(UserSchema):
    group_id: int = Field(ge=0)


class LecturerSchema(UserSchema):
    lecturer_id: int = Field(ge=0)


class Database:
    def __init__(self):
        self.pool: asyncpg.Pool | None = None


    async def connect(self) -> None:
        self.pool = await asyncpg.create_pool(
            user="postgres",
            password="1234",
            database="mydb",
            host="db",
            port=5432,
            min_size=1,
            max_size=10
        )
        logging.info("Connected to DB")


    async def close(self) -> None:
        await self.pool.close()


    async def create_students_table(self) -> None:
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                telegram_id BIGINT PRIMARY KEY
                , group_id INTEGER
                );
                """
           )


    async def create_lecturers_table(self) -> None:
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                CREATE TABLE IF NOT EXISTS lecturers (
                    telegram_id BIGINT PRIMARY KEY
                    , lecturer_id INTEGER
                );
                """
            )


    async def upsert_student(self, telegram_id: int, group_id: int) -> None:
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO students(telegram_id, group_id) 
                VALUES($1, $2) 
                ON CONFLICT (telegram_id) DO UPDATE SET
                    group_id = EXCLUDED.group_id
                """,
                telegram_id,
                group_id,
            )


    async def upsert_lecturer(self, telegram_id: int, lecturer_id: int) -> None:
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO lecturers(telegram_id, lecturer_id) 
                VALUES($1, $2) 
                ON CONFLICT (telegram_id) DO UPDATE SET
                    lecturer_id = EXCLUDED.lecturer_id
                """,
                telegram_id,
                lecturer_id,
            )


    async def get_student(self, telegram_id: int) -> StudentSchema:
        async with self.pool.acquire() as conn:
            response = await conn.fetch("SELECT group_id FROM students WHERE telegram_id = $1", telegram_id)
            student = StudentSchema(telegram_id=telegram_id, **response[0])
            return student


    async def get_lecturer(self, telegram_id: int) -> LecturerSchema:
        async with self.pool.acquire() as conn:
            response = await conn.fetch("SELECT lecturer_id FROM lecturers WHERE telegram_id = $1", telegram_id)
            lecturer = LecturerSchema(telegram_id=telegram_id, **response[0])
            return lecturer