#!/bin/sh

# Kerakli joylarni tayyorlash
#mkdir -p staticfiles && chmod -R 777 staticfiles

# Statik fayllarni yig'ish
python manage.py collectstatic --noinput

# Migratsiyalarni yaratish va qo'llash
python manage.py makemigrations
python manage.py migrate

# Gunicorn orqali Django ilovasini ishga tushirish
exec gunicorn --bind 0.0.0.0:8000 foodie.wsgi:application

