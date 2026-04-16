FROM python:3.12-slim

WORKDIR /bot

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
COPY bot.py .

EXPOSE 5000

CMD ["python", "bot.py"]