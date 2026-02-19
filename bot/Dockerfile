FROM python:3.9-slim

# Устанавливаем и библиотеку для Telegram, и библиотеку для веб-сервера (Flask)
RUN pip install pyTelegramBotAPI flask flask-cors

COPY bot/main.py /app/main.py
WORKDIR /app

# Открываем порт 5000, через который сайт будет "стучаться" к боту
EXPOSE 5000

CMD ["python", "main.py"]
