from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker

class DbSessionMiddleware(BaseMiddleware):
    def __init__(self, session_factory: async_sessionmaker):
        self.session_factory = session_factory

    async def __call__(self, handler, event, data):
        async with self.session_factory() as session:
            try:
                data["session"] = session

                result = await handler(event, data)

                # если всё ок → коммит
                await session.commit()

                return result

            except Exception:
                # если ошибка → откат
                await session.rollback()
                raise