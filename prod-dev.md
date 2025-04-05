
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

### 2. Django loyihasida `dev` bilan `prod` ni ajratish uchun `settings` papkasini yaratish

Keling, Django loyihasida `development` (ishlab chiqish) va `production` (ishlash) muhitlari uchun alohida sozlamalarni qanday tashkil qilishni batafsil va qadam-baqadam tushuntiraman:

1. **Papka tuzilmasini yaratish**

    Avval loyihangizdagi `settings.py` ni quyidagicha qayta tashkil qilamiz:

    ```
    project_name/
    ├── settings/          # Yangi papka
    │   ├── __init__.py    # Bo'sh fayl (papkani Python package qilish uchun)
    │   ├── base.py        # HAR IKKALA muhit uchun umumiy sozlamalar
    │   ├── dev.py         # Faqat development uchun sozlamalar
    │   └── prod.py        # Faqat production uchun sozlamalar
    ```
2. **Fayllarga ma'lumotlarni ko'chirish**


   - a) `base.py` - Barcha umumiy sozlamalar
      
        ```python
        # project_name/settings/base.py
        from pathlib import Path
        
        BASE_DIR = Path(__file__).resolve().parent.parent
        
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            ...  # Barcha umumiy applar
        ]
        
        MIDDLEWARE = [
            ...  # Umumiy middlewarelar
        ]
        
        # Boshqa umumiy sozlamalar (TEMPLATES, AUTH_PASSWORD_VALIDATORS, etc.)
        ```
   
   - b) `dev.py` - Development sozlamalari
        ```python
        # project_name/settings/dev.py
        from .base import *  # base.py dagi hamma narsani import qilamiz
        
        DEBUG = True
        
        ALLOWED_HOSTS = ['*']  # Barcha hostlarga ruxsat
        
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        
        # Qo'shimcha dev uchun sozlamalar
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        ```
   - c) `prod.py` - Production sozlamalari
      
        ```python
                     # project_name/settings/prod.py
        from .base import *  # base.py dagi hamma narsani import qilamiz
        
        DEBUG = False
        
        ALLOWED_HOSTS = ['example.com', 'www.example.com']  # Faqat ruxsat berilgan domaynlar
        
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
        
        # Xavfsizlik sozlamalari
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True
        SECURE_SSL_REDIRECT = True 
        ```

3. **Djangoga yangi sozlama joyini ko'rsatish**
   - a) `manage.py` **ni o'zgartiring:**
   
     ```python
     # Eski: os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')
     # Yangi (default dev muhitda ishlaydi):
     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings.dev')
     ```
   
   - b) `wsgi.py` **ni o'zgartiring (Production uchun):**
     ```python
     # Eski: os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')
     # Yangi:
     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings.prod')
     ```

4. **Ishlatish usullari**

   - **`Developmentda` ishga tushirish:**
     ```shell
     # Avtomatik ravishda dev.py ishlatiladi (manage.py da ko'rsatilgani uchun)
     python manage.py runserver
     ```
   - **`Productionda` ishga tushirish::**
     ```shell
     DJANGO_SETTINGS_MODULE=project_name.settings.prod python manage.py migrate
     ```
   - **`Docker-compose.yml` misoli:**
     ```yaml
     services:
       web:
         environment:
           - DJANGO_SETTINGS_MODULE=project_name.settings.prod  # Production uchun
     ```
5. **Qo'shimcha yaxshi amaliyotlar**  

   1. **Environment variables:**

      `.env` faylidan foydalaning (django-environ paketi yordamida):
       ```python
       # settings/base.py
       import environ
    
       env = environ.Env()
       environ.Env.read_env()
    
       SECRET_KEY = env('SECRET_KEY')
       ```
   2. **Fayl import tartibi:**
   
       ```python
       from .base import *  # Har doim birinchi
       # Keyin override qilish
       DEBUG = False
       ```
   3. **Test muhiti:**
   
      Agar kerak bo'lsa, test.py yaratishingiz mumkin:
   
      ```python
       from .base import *  # Har doim birinchi
       # Keyin override qilish
       DEBUG = False
       ```
6. **Nega bu yaxshi usul?**
   1. **Xavfsizlik:** Productionda nochor sozlamalar qolmaydi
   2. **Aniqlik:** Qaysi sozlama qaysi muhit uchun ko'rinadi
   3. **Moslashuvchanlik:** Yangi muhit (masalan, staging) qo'shish oson
   4. **Jamoa ishi:** Boshqa dasturchilar development sozlamalarini o'zgartirishi mumkin
   
7. **Misol loyiha tuzilmasi**

    ```
    myproject/
    ├── .env.dev
    ├── .env.prod
    ├── manage.py
    ├── myproject/
    │   ├── settings/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── dev.py
    │   │   └── prod.py
    │   └── urls.py
    └── requirements.txt
    ```
   `Bu usul bilan siz`:
   - Har bir muhit uchun aniq sozlamalarga ega bo'lasiz
   - Kodni productionga deploy qilishda xatolarga yo'l qo'ymaysiz
   - Jamoa a'zolari bilan ishlash osonlashadi


    























































