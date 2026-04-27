FROM python:3.12-slim

WORKDIR /app

# системные зависимости для asyncpg
RUN apt-get update && apt-get install -y gcc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY bot.py .
COPY wait_db.py .

CMD ["sh", "-c", "python wait_db.py && python bot.py"]