FROM python:3.9-slim

WORKDIR /app

# Системные зависимости для PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Копируем список библиотек (убедись, что файл requirements.txt лежит в этой же папке bot/)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY . .

CMD ["python", "main.py"]
