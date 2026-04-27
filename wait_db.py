import asyncio
import asyncpg
import os

async def wait_for_db():
    while True:
        try:
            conn = await asyncpg.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                database=os.getenv("DB_NAME"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
            )
            await conn.close()
            print("DB ready!")
            break
        except Exception:
            print("Waiting for DB...")
            await asyncio.sleep(2)

asyncio.run(wait_for_db())