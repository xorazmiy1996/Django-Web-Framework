### 1. `virtual server` ga kirgandan so'ng eng ko'p ishlatiladigan asosiy buyruqlar.

1. **Fayl va kataloglar bilan ishlash**
    - **Katalogni ko'rish:**
        ```shell
        ls
        ```

    - **Joriy katalogni ko'rish:**
        ```shell
        pwd
        ```

    - **Katalog yaratish:**
        ```shell
        mkdir katalog_nomi
        ```

    - **Fayl yoki katalogni o'chirish:**
        ```shell
        rm fayl_nomi
        ```
        **yoki katalog uchun:**
    
        ```shell
        rm -r katalog_nomi
        ```

2. **Fayllarni ko'rish va tahrirlash**

    - **Faylni ko'rish:**
        ```shell
        cat fayl_nomi
        ```
    - **Faylni tahrirlash** (nano yoki vim editorlaridan biri yordamida):
        ```shell
        nano fayl_nomi
        ```
        **yoki**  
   
        ```shell
        vim fayl_nomi
        ```
3. **Tizim va jarayonlar bilan ishlash**
    
    - **Tizim holatini ko'rish:**
        ```shell
        top
        ```
    - **Jarayonni to'xtatish:**
        ```shell
        kill jarayon_id
        ```
    - **Jarayonlar ro'yxatini ko'rish:**
        ```shell
        ps aux
        ```


4. **O'rnatish va yangilash**
    
    - **Dastur o'rnatish** (Ubuntu/Debian misolida):
        ```shell
        sudo apt update
        sudo apt install dastur_nomi
      ```
    - **Dasturlarni yangilash:**
        ```shell
        sudo apt upgrade
        ```



5. **Tarmoq buyruqlari**
    
    - **IP manzilini ko'rish:**
        ```shell
        ifconfig
        ```
      **yoki**

        ```shell
        ip a
        ```
    - **Tarmoqning ping-ni tekshirish:**
        ```shell
        ping -c 4 www.example.com
        ```

6. **Foydalanuvchilar bilan ishlash**
    
    - **Foydalanuvchilar ro'yxatini ko'rish:**
        ```shell
        cat /etc/passwd
        ```
    - **Yangi foydalanuvchi qo'shish:**
        ```shell
        sudo adduser yangi_foydalanuvchi
        ```
  

7. **Xavfsizlik va ruxsatlar**
    
    - **Fayl ruxsatlarini ko'rish:**
        ```shell
        ls -l fayl_nomi
        ```
    - **Ruxsatlarni o'zgartirish:**
        ```shell
        chmod 755 fayl_nomi
        ```
   > Bu buyruqlar sizga `virtual server` da ishlashda yordam beradi. Har bir buyruqni ehtiyotkorlik bilan ishlating va muhim fayllarni o'zgartirishdan oldin zaxira olishni unutmang.

### 2. `virtual server` da foydalanuvchi yaratish.

**Foydalanuvchi yaratish uchun qadamlar:**

1. **Terminalga kiring:** Virtual serverga `SSH` orqali kiring. Buning uchun terminaldan foydalaning:

   ```shell
   ssh username@ip_address
   ```
2. **Yangi foydalanuvchini yaratish:**

   > `adduser` yoki `useradd` buyruqlaridan biri yordamida yangi foydalanuvchini yaratishingiz mumkin. adduser ko'proq qulay va o'ziga xos bo'lib, interaktiv tarzda o'zgartirish imkonini beradi.

   **Misol uchun:**

   ```shell
   sudo adduser yangi_foydalanuvchi
   ```
   Yoki `useradd` buyruqdan foydalanish:

   ```shell
      sudo useradd -m yangi_foydalanuvchi
   ```
   `-m` flagi yangi foydalanuvchi uchun uy katalogini yaratadi.

3. **Parolni belgilash:**

   > `adduser` buyruği avtomatik ravishda foydalanuvchining parolini so'raydi. Agar useradd buyruqidan foydalangan bo'lsangiz, foydalanuvchining parolini belgilash uchun quyidagi buyruqni bajarishingiz kerak:

   ```shell
   sudo passwd yangi_foydalanuvchi
   ```
   > Yuqoridagi buyruqdagi `passwd` o'rniga o'zingizning yangi passwordingizn yozmang chungi bu hato, bu yerda `passwd ` kalit so'z hisoblanadi. Bu buyruqda siz `yangi_foydalanuvchi` o'rniga `useradd` orqali yaratilgan foydalanuvchini kiritasiz va `enter` tugmasini bosasiz. Shundan so'ng sizdan yangi foydalanuvchi uchun password kiritishni so'raladi.  



4. **Foydalanuvchini qo'shimcha guruhlarga kiritish:**

   > Agar foydalanuvchini biror guruhga kiritsangiz (masalan, `sudo` guruhiga, agar uni `administrator` qilishni xohlasangiz), quyidagi buyruqni bajarishingiz mumkin:

   ```shell
   sudo usermod -aG sudo yangi_foydalanuvchi
   ```
5. **Foydalanuvchini yaratish jarayonini yakunlash:**

   > Hamma narsa to'g'ri bajarilgandan so'ng, yangi foydalanuvchi serverda o'ziga xos huquqlarga ega bo'ladi. U o'z profiliga kirishi mumkin va belgilangan huquqlarga mos ravishda ish olib borish imkoniyatiga ega bo'ladi.

**Misol:**

Agar siz `developer` nomli foydalanuvchini yaratmoqchi bo'lsangiz, quyidagi buyruqlarni bajarishingiz mumkin:

```shell
   sudo adduser developer
   # Parolni kiritish
   sudo usermod -aG sudo developer  # Agar uni administrator qilishni xohlasangiz
```

### 3. `virtual server` ga kiradigan `root foydalanuchisi` bilan va yangi yaratilgan   `yangi_foydalanuvchi` foydalanuvchi o'rtasidagi farqlar ni tushuntirib bering.
1. `Huquqlar` va `Ruxsatlar`
   - **Root foydalanuvchisi:**
     - `Superuser` yoki `administrator` hisoblanadi.
     - Tizimning barcha resurslariga (fayllar, dasturlar, boshqa foydalanuvchi hisoblari va boshqalar) to'liq kirish huquqiga ega.
     - Har qanday komanda va operatsiyalarning bajarilishiga ruxsat beriladi, shu jumladan tizim sozlamalarini o'zgartirish, foydalanuvchilarni yaratish va o'chirish.
   - **Oddiy foydalanuvchi `yangi_foydalanuvchi`:**
     - Tizimda cheklangan huquqlarga ega.
     - Faqat o'z uy katalogidagi fayllarga kirish va o'zgartirish huquqiga ega.
     - Boshqa foydalanuvchilarning kataloglarini o'zgartira olmaydi va tizim konfigatsiyalarini o'zgartirish uchun `sudo` huquqlariga ega bo'lmasa, `root` buyruqlarini bajarish imkoniyatiga ega emas.

### 4. `virtual server` ga `docker` qanday o'rnatiladi?

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

### 5. Men `virtual server` dagi `Django` loyihamni bazasini `postgreSQL` ga o'zgartirmoqchiman buning uchun `virtaual server` da  nima qilishim kerak.

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

### 6. `Windows` ga `PostgreSQL`  o'rnatish.

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

### 7. PgAdmin foydalanuvchilarga PostgreSQL ma'lumotlar bazalarini boshqarish va ularga kirishga imkon beruvchi grafik interfeysdir. PgAdmin dasturida server qo'shish va uning ma'nosi haqida tushunchani chuqurlashtiraylik:

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

### 8. `pgAdmin` da `sereve group` nima uchun kerak ?

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

### 9. Menda yana bir savol bor men `pgAdmin` dan chiqib ketsam men yaratgan server bo'g'lanish saqlanib qolami?

> Ha, `PgAdmin` dasturidan chiqib ketganingizda, siz yaratgan serverlar yoki ularning bog'lanishlari saqlanib qoladi. `PgAdmin` ma'lumotlari va server konfiguratsiyalari diskda saqlanadi, shuning uchun dastur yana ochilganda, siz oldin yaratgan serverlarni yana ko'rishingiz va ularga ulangani davom ettirishingiz mumkin.



















































































































































































