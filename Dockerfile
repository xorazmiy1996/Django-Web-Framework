# Pythonning rasmiy tasviridan foydalanamiz
FROM python:3.13.2

# Ishchi katalogni yaratamiz
WORKDIR /app

# Talablar faylini konteynerga nusxalash
COPY requirements.txt .

# Talablarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# Barcha kodni konteynerga nusxalash
COPY . .

# Django serverini ishga tushirish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]