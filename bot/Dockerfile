# Используем легкую версию Python на базе Alpine
FROM python:3.9-slim

# Устанавливаем библиотеку для работы с Telegram
RUN pip install pyTelegramBotAPI

# Копируем код бота в контейнер
COPY main.py /app/main.py
WORKDIR /app

# Запускаем бота
CMD ["python", "main.py"]
