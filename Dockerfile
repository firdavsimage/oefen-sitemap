# Python bazaviy imiji
FROM python:3.10-slim

WORKDIR /app

# Talablarni o‘rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani nusxalash
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
