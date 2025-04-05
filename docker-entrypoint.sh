#!/usr/bin/sh

# Migratsiyalarni yaratish va qo'llash
python manage.py makemigrations
python manage.py migrate

# Gunicorn orqali Django ilovasini ishga tushirish
exec gunicorn --bind 0.0.0.0:8000 foodie.wsgi:application

