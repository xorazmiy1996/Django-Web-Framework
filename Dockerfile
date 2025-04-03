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

# Django ma'lumotlar bazasini migratsiya qilish
RUN python manage.py makemigrations
RUN python manage.py migrate

# Django statik fayllarini yig'ish
RUN python manage.py collectstatic

# Django serverini ishga tushirish
CMD ["gunicorn", "foodie.wsgi:application", "--bind", "0.0.0.0:8000"]