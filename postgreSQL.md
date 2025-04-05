
### 1. Men `virtual server` dagi `Django` loyihamni bazasini `postgreSQL` ga o'zgartirmoqchiman buning uchun `virtaual server` da  nima qilishim kerak.

> `Django` loyihangizni `PostgreSQL` ma'lumotlar bazasiga o'tkazish uchun quyidagi qadamlarni bajaring. Ushbu jarayon `virtual server` da `PostgreSQL` serverini o'rnatishni, `Django` da ma'lumotlar bazasini sozlashni va `migratsiyalar` ni amalga oshirishni o'z ichiga oladi.

**virtual server da PostgreSQL o'rnatish:**

>  `PostgreSQL` o'rnatish jarayoni odatda terminal (`SSH` yoki `lokal terminal`) orqali amalga oshiriladi. Bunday holatda sizning terminalingiz ochiq bo'lishi kerak va tizim` administratori (root)` yoki `sudo` huquqlariga ega foydalanuvchi hisobidan foydalanishingiz lozim.

```shell
#  1. Tizim paketlarini yangilash
sudo apt update
sudo apt upgrade

# PostgreSQL o'rnatish
sudo apt install postgresql postgresql-contrib

# 2. PostgreSQL foydalanuvchisini va ma'lumotlar bazasini yaratish
# PostgreSQL'ga kirish:
sudo -i -u postgres

# PostgreSQL interaktiv terminalini oching:
psql

# Yangi foydalanuvchini yaratish:
CREATE USER django_user WITH ENCRYPTED PASSWORD 'your_password';

# Yangi ma'lumotlar bazasini yaratish:
CREATE DATABASE django_db WITH OWNER django_user;

# Foydalanuvchiga ma'lumotlar bazasi ustidan to'liq huquqlar berish:
GRANT ALL PRIVILEGES ON DATABASE django_db TO django_user;

# PostgreSQL terminalini yopish:
\q


# PostgreSQL xizmatining ishlayotganligini tekshirish uchun terminalda quyidagi buyruqni bajaring:
# Agar xizmat muvaffaqiyatli o'rnatilgan va ishlayotgan bo'lsa, 
# siz "active (running)" yoki shunga o'xshash holatni ko'rishingiz kerak.
# Agar xato yoki "inactive" holati ko'rsatilsa, xizmat ishlamayotganligini bildiradi.
sudo systemctl status postgresql
```
**Djangoda `PostgreSQL` adapterini o'rnatish**

> `Django` loyhasi uchun `PostgreSQL` adapterini o'rnatish kerak. Virtual muhit `(venv)` ichida quyidagi buyruqni bajarish orqali `psycopg2` o'rnatiladi:

```shell
pip install psycopg2-binary
```
 **Django sozlamalarini yangilash**

> `Django` loyhasida `settings.py` faylini tahrirlang va ma'lumotlar bazasini `PostgreSQL` ga sozlang:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_db',          # Yaratilgan ma'lumotlar bazasi nomi
        'USER': 'django_user',        # Yaratilgan foydalanuvchi nomi
        'PASSWORD': 'your_password',   # Foydalanuvchining paroli
        'HOST': 'localhost',           # Agar PostgreSQL lokal serverda bo'lsa
        'PORT': '',                    # Standart port 5432
    }
}
```
**Migratsiyalarni amalga oshirish**

   ```shell
      python manage.py makemigrations
      python manage.py migrate   
   ```

**Django serverini ishga tushirish**

`python manage.py runserver`

**Django Admin panelini sozlash**
   - Django admin paneli uchun `superuser` hisobini yarating, bu orqali siz ma'lumotlar bazasini boshqarasiz:
   
      `python manage.py createsuperuser`

### 2. `Windows` ga `PostgreSQL`  o'rnatish.

1. `PostgreSQL` Rasmiy Saytiga O'ting
   - PostgreSQL ning rasmiy veb-saytiga o'ting: [PostgreSQL Downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) . Bu yerda Windows uchun kerakli versiyani tanlashingiz mumkin.

2. O'rnatishni Boshlash
   - Yuklab olingan .`exe` faylni ikki marta bosib oching.
   -  O'rnatish Joyini Tanlash
     - `PostgreSQL` ning o'rnatiladigan joyini tanlang yoki standart joyini qoldiring (C:\Program Files\PostgreSQL\XX, bu yerda XX versiya raqami).
       
   - Yuklangan fayllarni saqlanadigan joyni tanlang.
   - Ma'lumotlar Katalogini Tanlash
     - `PostgreSQL` ma'lumotlar katalogini tanlang. Odatda, bu joy C:\ProgramData\PostgreSQL\XX\data bo'ladi.
   - `Superuser` Parolini Belgilash
     - `postgres` foydalanuvchisi uchun parolni o'rnating. Bu parolni yodda saqlang, chunki siz ma'lumotlar bazasi bilan aloqa o'rnatishda foydalanasiz.
   - `Portni` Tanlash
     - `PostgreSQL` uchun foydalaniladigan portni tanlang. Standart port `5432`-dir.
   - `Locale` o'rnatish
     - O'rnatilish joyi `(locale)` ni tanlang. Agar sizga kerak bo'lsa, bu qadamni o'zgartirishingiz mumkin yoki standart qolishini qoldiring.
   - O'rnatishni Tugatish
     - O'rnatish jarayonini tugatish uchun `Install` tugmasini bosing. O'rnatish jarayoni tugagach, `Finish` tugmasini bosing.

3. `PostgreSQL` xizmatini ishga tushirish

   > O'rnatgandan so'ng, `PostgreSQL` xizmatini avtomatik ravishda ishga tushadi. Agar kerak bo'lsa, quyidagi qadamlarni bajarib, xizmatni qo'lda ishga tushirishingiz mumkin.
   - `Windows Services` (Xizmatlar) panelini oching va `PostgreSQL` xizmatini qidiring (masalan, postgresql-x.x).
   - Xizmatni tanlang va `Start` (Ishga tushirish) ni bosing.

4.  `PgAdmin` O'rnatish

   > `PgAdmin` `PostgreSQL` uchun grafik interfeysda boshqaruv vositasidir. O'rnatish jarayonida `PgAdmin` ham o'rnatilgan bo'ladi. O'rnatilgan `PgAdmin` dasturini oching va `postgres` foydalanuvchisi deb, belgilangan parolni kiritib tizimga kiring.

5. `PostgreSQL` bilan ishlash

   O'rnatish muvaffaqiyatli o'tgandan so'ng, siz `PostgreSQL` ma'lumotlar bazasi bilan ishlashni boshlashingiz mumkin. `Terminal` da yoki `PgAdmin` dan foydalanib, ma'lumotlar bazalarini yaratishingiz, o'zgartirishingiz yoki so'rovlar yuborishingiz mumkin

6.  Hujjatlar va Qo'llab-quvvatlash
   - `PostgreSQL` ning rasmiy veb-saytida versiyalarning o'zgarishlari va yangiliklari haqida batafsil axborot beriladi. Shuning uchun, hozirgi versiyalarni ham, ularning tarixi va hujjatlarini o'rganishishingiz kerak:

     - [PostgreSQL Release Notes](https://www.postgresql.org/docs/)

### 3. PgAdmin foydalanuvchilarga PostgreSQL ma'lumotlar bazalarini boshqarish va ularga kirishga imkon beruvchi grafik interfeysdir. PgAdmin dasturida server qo'shish va uning ma'nosi haqida tushunchani chuqurlashtiraylik:

1. Server Nima?
   - **Ma'lumotlar Bazasi Serveri:** `PostgreSQL` ma'lumotlar bazasi serveri - bu ma'lumotlarni saqlash, boshqarish va qayta ishlash uchun mo'ljallangan dastur. U o'z ichiga o'z ma'lumotlar bazasini, foydalanuvchilarni va ulanadigan dasturlarni o'z ichiga olaydi.
   - **Foydalanuvchilar va Bağlantilar:** Barcha foydalanuvchilar (shu jumladan siz) serverga ulangan holda ma'lumotlar bazalarini yaratishi, qo'shishi va boshqarishi mumkin.
   > Har bir serverga ulanishda foydalanuvchi `nomi` va `parol` kiritilishi kerak. Bu, ma'lumotlarga kirishni nazorat qilish imkoniyatini beradi. Foydalanuvchilar ma'lumotlarni ko'rish yoki o'rganishdan oldin o'z autentifikatsiyasini bajonidil o'tkazishi kerak.

2. **Qanday Server Qo'shish Kerak?**

**PgAdmin da yangi server qo'shish jarayoni:**
   1. PgAdmin dasturini oching va `Servers` bo'limida o'ng tugmachini bosing.
   2. `Create` -> `Server` ni tanlang.
   3. Server nomini kiriting va `Connection` tabda kerakli parametrlarni to'ldiring:
      - **Host:** `localhost` (agar siz mahalliy serverga ulanayotgan bo'lsangiz) yoki serverning IP manzili (agar u masofadagi server bo'lsa).
      - **Port:** Standart port `5432`.
      - **Username:** postgres yoki siz yaratgan boshqa foydalanuvchi.
      - **Password:** Siz belgilagan parol.

   4. Hammasini to'ldirgandan so'ng, `Save` ni bosing.

### 4. `pgAdmin` da `sereve group` nima uchun kerak ?

>`PgAdmin` dasturida `Server Group` (server guruhi) - bu foydalanuvchilarga bir yoki bir nechta `PostgreSQL` serverlarini tashkil qilish va ularni boshqarish jarayonini yengillashtirish imkoniyatini beruvchi tuzilma. Quyida `Server Group` qanday maqsadlarga xizmat qilishi va undan qanday foydalanish mumkinligi haqida batafsil ma'lumot keltirilgan:

1. Tashkilot va Boshqaruv
   - `Server` guruhlari bir nechta serverlarni birlashtirishga imkon beradi. Masalan, sizda bir nechta PostgreSQL serverlari mavjud bo'lsa va ularni bir xil loyihada ishlatayotgan bo'lsangiz, siz bu serverlarni bitta guruhga joylashtirib, boshqarishni osonlashtirishingiz mumkin.

2. Vizual Tashkiliy Qaytish
   > `PgAdmin` dasturida serverlarni guruhlash orqali siz ularni ko'rish va boshqarishni osonlashtirasiz:
   - Serverlar ko'p bo'lganda, guruhlar yordamida alohida kategoriyalarga ajratish mumkin.
   - Foydalanuvchilar uchun interfeysda qidiruv va navigatsiyani tezlashtiradi.
3. Bir Muddati Ishlash
   > Agar sizning bir xil maqsadda ishlatadigan bir nechta serveringiz bo'lsa (masalan, ishlab chiqish, test qilish va ishlab chiqarish muhiti), ularni bir guruhda tashkil qilishingiz va ularga bir vaqtning o'zida kirishingiz mumkin. Bu bir vaqtning o'zida bir nechta serverlar bilan ishlash jarayonini soddalashtiradi.

4. Halqaro Ko'rsatkich
   - Guruhlar yordamida serverlar haqidagi ma'lumotlarni bir joyda yig'ish imkonini beradi va qaysi server qo'shilgan yoki o'chirilganini kuzatish osonroq bo'ladi.

`Qanday qilib Server Guruhi Yaratish:`
   1. PgAdmin dasturini oching.
   2. `Servers` bo'limi ostida o'ng tugma bilan bosing.
   3. `Create` va keyin `Server Group` ni tanlang.
   4. Guruhga nom bering va `Save` tugmasini bosing.
   5. Endi siz yangi guruhi ichiga serverlarni qo'shishingiz mumkin.

### 5. Menda yana bir savol bor men `pgAdmin` dan chiqib ketsam men yaratgan server bo'g'lanish saqlanib qolami?

> Ha, `PgAdmin` dasturidan chiqib ketganingizda, siz yaratgan serverlar yoki ularning bog'lanishlari saqlanib qoladi. `PgAdmin` ma'lumotlari va server konfiguratsiyalari diskda saqlanadi, shuning uchun dastur yana ochilganda, siz oldin yaratgan serverlarni yana ko'rishingiz va ularga ulangani davom ettirishingiz mumkin.


