
### 1. `Development/production farqi` deganda `Development` va `production` nimani tushunish kerak?

> `Development` (Ishlab chiqish) va `Production` (Ishlatish) muhitlari farqi Django loyihalari uchun juda muhim
> tushuncha. Keling, batafsil va oddiy tushuntiraman:

1. `Development` (Dev) - **Ishlab chiqish muhiti**
    - **Maqsad:** Loyihani ishlab chiqish, test qilish
    - **Xususiyatlari:**
        - `DEBUG=True` - Batafsil xatolik habarlari
        - `SECRET_KEY` oddiy (masalan, "dummy-key")
        - `SQLite` ishlatilishi mumkin
        - `makemigrations` tez-tez ishlatiladi
        - `runserver` bilan ishga tushiriladi (8000-port)
        - Ko'p loglar, test ma'lumotlari

**Misol `settings.py`:**

```python
DEBUG = True
ALLOWED_HOSTS = ['*']  # Barcha hostlarga ruxsat
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

2. **Production (Prod) - Ish muhiti**

    - **Maqsad:** Foydalanuvchilar uchun tayyor ilova
    - **Xususiyatlari:**
        - `DEBUG=False` - Xatolik habarlari yashiriladi
        - Haqiqiy `SECRET_KEY` (maxfiy saqlanadi)
        - `PostgreSQL/MySQL` kabi professional DB
        - Faqat `migrate` ishlatiladi
        - `Gunicorn/Nginx` + `HTTPS`
        - `Statik` fayllar alohida serverda

**Misol settings.py:**

```python
DEBUG = False
ALLOWED_HOSTS = ['example.com']  # Faqat ruxsat berilgan domayn
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

3. **Asosiy farqlar jadvali**

| Parametr         | Development              | Production           |
|------------------|--------------------------|----------------------|
| **DEBUG**        | True                     | False                |
| **Database**     | SQLite                   | PostgreSQL/MySQL     |
| **Server**       | runserver                | Gunicorn + Nginx     |
| **Port**         | 8000                     | 80/443 (HTTPS)       |
| **Secret Key**   | Oddiy matn               | Environment variable |
| **Logging**      | Konsolda ko'p log        | Faylga yozish        |
| **Static files** | collectstatic shart emas | Alohida server       |

4. **Docker** kontekstidagi farqlar

   Development uchun `docker-compose.yml`:

   ```yaml
   services:
     web:
       command: python manage.py runserver 0.0.0.0:8000
       volumes:
         - .:/app  # Kodni real-time o'zgartirish mumkin
       environment:
         - DEBUG=True
   ```
   Production uchun `docker-compose.yml`:
   ```yaml
   services:
     web:
       command: gunicorn project.wsgi:application --bind 0.0.0.0:8000
       environment:
         - DEBUG=False
         - DJANGO_SETTINGS_MODULE=project.settings.production
       restart: always
   ```
5. **Qanday ajratish kerak?**
   1. **settings/ papka yaratish:**
      ```
      settings/
      ├── __init__.py
      ├── base.py      # Umumiy sozlamalar
      ├── dev.py       # Development
      └── production.py  # Production
      ```

   2. `manage.py` ni o'zgartirish:
      ```python
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.dev')
      ```
   3. **Productionda ishga tushirish:**
      ```bash
      DJANGO_SETTINGS_MODULE=project.settings.production python manage.py migrate
      ```
6. **Muhim maslahatlar**  
   - **Developmentda:**
     - `python manage.py shell_plus` (IPython bilan)
     - Ko'proq test ma'lumotlari
     - Avtomatik qayta yuklovchilar
   - **Productionda**
     - Har doim `DEBUG=False`
     - `ALLOWED_HOSTS` aniq ko'rsatilishi kerak
     - `python manage.py check --deploy` bilan tekshirish

> **Farqlarni tushunish** - `professional` `Django` dasturchi bo'lishning kalitlaridan biridir. Har ikkala muhit uchun alohida sozlamalarga ega bo'lish sizga ko'p muammolardan qutqaradi!




