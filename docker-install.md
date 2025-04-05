### 1. `Django` loyihasini `Dockerfile` orqlai ishga tushurganda `makemigrations` va

`migrate` qilish bo'yicha muommo chiqishi mumkin.

> Bunga sabab `python manage.py makemigrations` va `python manage.py migrate` buyruqlarini `Dockerfile` da
> joylashtirilgan bo'lishim mumkin.

`Keling, tushuntiraman`:

1. `makemigrations` va `migrate` buyruqlari  `Dockerfile` da yozilmasligi kerak.

   `Sabablari`:

    1. `Build` vaqtida `database` mavjud emas - `Docker` `image` yaratilayotganda `database` containeri hali ishlamaydi
    2. `Code` `changes` tez-tez bo'ladi - Har safar model o'zgartirganda yangi `image` yaratish noqulay
    3. `Statik` qadamlar - `Migratsiya` lar `dynamic` process, `image` esa `static` bo'lishi kerak

2. `makemigrations` va `migrate` buyruqlari quydagicha joylarda ishlatgan ma'qul.

    - **Variant A:** `docker-compose.yml` dagi `command` ichida

   `docker-compose.yml`:

    ```yaml
    services:
      web:
        command: sh -c "python manage.py migrate && gunicorn project.wsgi:application"
    ```

    - **Variant B:** Alohida entrypoint scriptida

   `entrypoint.sh`:

   ```bash
   #!/bin/sh
   python manage.py migrate
   exec "$@"
   ```
   `Dockerfile`:
   ```dockerfile
   COPY entrypoint.sh /
   RUN chmod +x /entrypoint.sh
   ENTRYPOINT ["/entrypoint.sh"]
   CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
   ```
    - **Variant C:** `docker-compose` `exec` orqali qo'lda

   ```shell
   docker-compose up -d  # Containerlarni ishga tushirish
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```

3. **Makemigrations uchun maxsus yondashuv:**

```yaml
   services:
     web:
       command: sh -c "python manage.py makemigrations --noinput && python manage.py migrate && gunicorn project.wsgi:application"
```

4. **Ish tartibi sabablari:**

    1. **Database tayyor bo'lishini kutish** - `Migrate` qilishdan avval `PostgreSQL` tayyor bo'lishi kerak
    2. **Code-model mosligi** - Yangi kod bilan yangi migratsiyalar
    3. **Development/production farqi:**
        - **Development:** `makemigrations` qo'lda ishlatiladi
        - **Production:** Faqat mavjud migratsiyalarni `migrate` qilish

5. **Mukammal `Dockerfile` misoli:**

   `Dockerfile`:

   ```dockerfile
   FROM python:3.9
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   # Faqat statik qadamlar (masalan, collectstatic)
   RUN python manage.py collectstatic --noinput
   
   # Entrypoint dinamik qadamlar uchun
   COPY entrypoint.sh /
   RUN chmod +x /entrypoint.sh
   ENTRYPOINT ["/entrypoint.sh"]
   
   CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]  
   ```
6. **Production uchun eng yaxshi amaliyotlar:**
    1. Migratsiyalarni `CI/CD` da alohida qadam sifatida ishlating
    2. `makemigrations` ni faqat developmentda ishlating
    3. Healthcheck qo'shing:
   ```yaml
   services:
     db:
       healthcheck:
         test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
         interval: 5s
         timeout: 5s
         retries: 5
   ```

`Xulosa`:

> `Migratsiya` buyruqlarini `Dockerfile` ga emas, balki `container` ishga tushganda bajariladigan qismga
`(command/entrypoint)` qo'ying. Bu sizga moslashuvchanlik va ishonchlilik beradi.

### 2. `virtual server` ga `docker` qanday o'rnatiladi?

> `Docker` o'rnatish jarayoni odatda terminal (`SSH` yoki `lokal terminal`) orqali amalga oshiriladi. Bunday holatda sizning terminalingiz ochiq bo'lishi kerak va tizim` administratori (root)` yoki `sudo` huquqlariga ega foydalanuvchi hisobidan foydalanishingiz lozim.

Qanday qilib terminalni ochish kerak:

1. `SSH` **orqali ulanish** (agar siz remote serverda bo'lsangiz)
   - Terminal (`Linux` yoki `MacOS` uchun) `yoki` `PuTTY` yoki `MobaXterm` (Windows uchun) dasturlaridan foydalaning.
   
   - `SSH` orqali serverga ulaning:

      ```shell
      ssh username@ip_address
      ```
   - `username` o'rniga serverda foydalanuvchi nomingizni, `ip_address` o'rniga serveringizning `IP` manzilini yozing.

2. **Lokal tizimda terminal ochish** (agar siz lokal tizimda ishlayotgan bo'lsangiz):

   - `Linux`: Klaviaturadan `Ctrl + Alt + T` tugmalarini bosib terminalni oching.
   - `MacOS`: `Terminal` ilovasini qidirib oching.
   - `Windows`: `Command Prompt` yoki `PowerShell` yoki Windows Subsystem for Linux (WSL) dan foydalaning.

**Docker o'rnatish buyruqlari:**

```shell
      # 1. Tizim paketlarini yangilash
      sudo apt update
      sudo apt upgrade
      
      # 2. Zarur paketlarni o'rnatish
      sudo apt install apt-transport-https ca-certificates curl software-properties-common
      
      # 3. Docker GPG kalitini qo'shish
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      
      # 4. Docker repository'sini qo'shish
      sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      
      # 5. Yangilanishlar mavjudligini tekshirish
      sudo apt update
      
      # 6. Docker'ni o'rnatish
      sudo apt install docker-ce
      
      # 7. Docker holatini tekshirish
      sudo systemctl status docker
      
      # 8. Agar kerak bo'lsa, foydalanuvchini 'docker' guruhiga qo'shish
      sudo usermod -aG docker $USER
      
      # 9. Docker o'rnatishni sinovdan o'tkazish
      docker run hello-world
```
> `Docker` o'rnatish jarayonida yuqorida keltirilgan buyruqlarni terminalda amalga oshirishingiz kerak. Har doim administrator huquqlaridan foydalanishni unutmang (`sudo` bilan).


































































