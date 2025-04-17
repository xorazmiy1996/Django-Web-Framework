### 1. django.db.utils.OperationalError: connection to server at `db` (172.18.0.2), port 5432 failed: FATAL:  `password authentication` failed for user "test" hatoliki kuzatilsa, u holda quydagicha harakat qiling.

1. `setting.py` ichidagi `DATABASES` yoki `docker-compose.yml` ichidagi `environment` hato bo'lishi mumkin.

    `setting.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB'),             # Yaratilgan ma'lumotlar bazasi nomi
            'USER': os.getenv('POSTGRES_USER'),           # Yaratilgan foydalanuvchi nomi
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),   # Foydalanuvchining paroli
            'HOST': os.getenv('POSTGRES_HOST'),           # Agar PostgreSQL lokal serverda bo'lsa
            'PORT': os.getenv('POSTGRES_PORT','5432'),    # Standart port 5432
        }
    }
    ```
    `docker-compose.yml`:

    ```ini
    version: '3.8'
    services:
      web:
        build: .
        ports:
          - "5000:8000"
        volumes:
          - .:/app
        depends_on:
          - db
        env_file:
          - ./.env
      db:
        image: postgres
        environment:
          - POSTGRES_DB=${POSTGRES_DB}
          - POSTGRES_USER=${POSTGRES_USER}
          - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
        volumes:
          - postgres_data:/var/lib/postgresql/data
    volumes:
      postgres_data:
    ```

    > Ko'pincha bu hato `POSTGRES_DB`, `POSTGRES_USER` , `POSTGRES_PASSWORD` kalit so'zlarida yoki qiymatlari hato kiritilgan bo'ladi

2. **Asosiy kamchiliklar va tuzatishlar:**

   - `db` **Service Environment Sozlamalari:**
     - **Xato:** `DATABASE_HOST`, `DATABASE_PORT` – `PostgreSQL` imageʼi ularni talab qilmaydi.
     - **Toʻgʻrilash:** Faqat `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` ishlating.
     - **Sabab:** `PostgreSQL` imejiga `POSTGRES_*` oʻzgaruvchilari orqali sozlamalar beriladi.
   
   - **Port Mapping:**
     - **Xato:** `db` serviceʼda port ochilmagan (lekin bu shart emas, chunki `web` service tarmoq orqali `db:5432` ga ulanadi).
     - **Yechim:** Agar hostdan test qilish kerak boʻlsa, `db` ga port qoʻshing:
     ```yaml
     ports:
       - "5432:5432"  # Hostda 5432 portni ochish
     ```
**Muhim Eslatmalar**
- `.env` fayl strukturasini tekshiring:
    ```ini
    POSTGRES_DB=foodie
    POSTGRES_USER=test
    POSTGRES_PASSWORD=1996
    # POSTGRES_HOST=db  # Bu web app uchun kerak (DB_HOST sifatida)
    # POSTGRES_PORT=5432
    ```
- **Django settings.py sozlamalari:**

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': 'db',  # Docker Compose service nomi
            'PORT': '5432',
        }
    }
    ```
  
**Eski volumeni tozalash:**
- Terminalda:

    ```bash
    docker compose down -v  # Eski volumeni tozalash
    docker compose up -d    # Yangi konteynerlarni ishga tushirish
    docker compose logs web # Xatoliklarni tekshirish
    ```       


### 2. windows operatsion tizimida docker-compose yordamica ishga tushuriladigan django loliyhasida quydagicha hatolik bo'lishi mumkin:

```ini
usage: manage.py collectstatic [-h] [--noinput] [--no-post-process]
web-1  |                                [-i PATTERN] [-n] [-c] [-l]
web-1  |                                [--no-default-ignore] [--version]
web-1  |                                [-v {0,1,2,3}] [--settings SETTINGS]
web-1  |                                [--pythonpath PYTHONPATH] [--traceback]
web-1  |                                [--no-color] [--force-color] [--skip-checks]
web-1  | manage.py collectstatic: error: unrecognized arguments: --no-input


Unknown command: 'migrate\r'. Did you mean migrate?
web-1  | Type 'manage.py help' for usage.
```
> `docker-entrypoint.sh` faylining `line separator` hatoligi ya'ni `docker compose up -d --build` bilan project ishga tushurilganda `docker-entrypoint.sh` ichidagi commandalar bajarilmaydi.

> Bu xatoliklar `docker-entrypoint.sh` faylida qator ajratuvchilari muammosi borligini ko'rsatadi. Windows operatsion tizimida fayllar odatda `CRLF (\r\n)` formatida saqlanadi, bu esa Linux konteynerlarida muammolarga olib kelishi mumkin.
    
> Yuqoridagi hatoni oldini olish ya'ni o'rnatilyotgan project joriy operatsion tizimga bog'liqligini oldini olish uchun `docker-entrypoint.sh` ishlatmaslik kerak buning o'rniga Dockerfile ichidagi `CMD` ichiga yozish kerak.




































































































