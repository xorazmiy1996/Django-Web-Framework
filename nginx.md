### 1.` web server` lar deb nimaga aytiladi?

> `Veb-serverlar` — bu veb-sahifalarga va boshqa veb-resurslarga `HTTP` yoki `HTTPS` protokollari orqali foydalanuvchilarga xizmat ko'rsatadigan dasturiy ta'minot yoki uskunalar. Veb-serverlar, asosan, foydalanuvchi so'rovlarini qabul qilib, ularga mos ravishda kerakli ma'lumotlarni yetkazib berish uchun ishlatiladi.

### 2. `gunicorn` nima va nima uchun kerak.

> `Gunicorn` (Green Unicorn) - bu Python uchun WSGI (Web Server Gateway Interface) `HTTP` serveri bo'lib, Python veb-ilovalarini ishga tushirish uchun ishlatiladi.

**Asosiy xususiyatlari:**

   1. `Python` **ilovalari uchun optimallashtirilgan:** `Django`, `Flask`, `Pyramid` kabi frameworklar bilan ishlaydi
   2. **Ko'p protsessli model:** Bir nechta ishchi protsesslarni boshqaradi
   3. **Oddiy konfiguratsiya:** Boshlang'ich sozlash juda oson
   4. **Oddiy konfiguratsiya:** Boshlang'ich sozlash juda oson

**`Gunicorn` qanday ishlaydi?**

**`Gunicorn` asosan quyidagilarni bajaradi:**

   - Veb-so'rovlarni qabul qiladi
   - Ularni `Python` ilovangizga uzatadi
   - Ilovadan qaytgan javoblarni foydalanuvchiga qaytaradi

**O'rnatish**

**`Gunicorn` `pip` orqali oson o'rnatiladi:**


   ```shell
      pip install gunicorn
   ```
**Ishga tushirish**

**Oddiy `Django` ilovasi uchun:**

   ```shell
      gunicorn myproject.wsgi:application
   ```
**Flask ilovasi uchun:**

```shell
  gunicorn myapp:app
```

### 3. WSGI (Web Server Gateway Interface) nima?

`WSGI` - Bu `Python ilovalari` va `veb-serverlar` o'rtasidagi `tarjimon`

**Tasavvur qiling:**

Siz restoranga keldingiz (`veb-server` - masalan, Nginx). Ofitsiant (`WSGI`) sizning buyurtmangizni (`HTTP so'rov`) oshpazga (`Python ilovangizga`) yetkazadi va tayyor ovqatni (HTTP javob) sizga qaytaradi.

**Nega `WSGI` kerak?**

   1. **Til farqi:**
      - `Veb-serverlar` (`Nginx`, `Apache`) `C` tilida yozilgan, `Python` ni tushunmaydi
      - `Python` ilovalari esa serverlarni tushunmaydi
      - `WSGI` ularni `gapirtiradi`

   2. `WSGI` **ularni** `gapirtiradi`
      - Har bir `Python framework` (`Django`, `Flask`) turli yo'llarda ishlaydi
      - `WSGI` ularga umumiy til beradi: `Hammangiz shu interfeysga amal qiling!`
   
   ```python
    # WSGI ilovasi - har bir Python framework shunday ishlaydi
    def application(environ, start_response):
    # So'rovni tahlil qilish
    if environ['PATH_INFO'] == '/salom':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b"<h1>Assalomu alaykum!</h1>"]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return [b"<h1>Sahifa topilmadi</h1>"]
   ```

**Hayotiy taqqosamalar:**

   1. **Telefon ilovasi va OS:**
      - `Android`/`iOS` (veb-server)
      - Ilovalar (`Python` dasturlari)
      - `API` lar (`WSGI`) - ularni bog'lovchi qism

   2. **Avtomobil:** 
      - Dvigatel (Python ilova) 
      - G'ildiraklar (veb-server)
      - Transmissiya (WSGI) - kuchni uzatuvchi

### 4. `gunicorn` bila `wsgi` ni nima farqi bor ikkalasi ham bir narsani bajarmaydimi?

`Gunicorn` va `WSGI` bir-biriga bog'liq, lekin bir xil narsa emas. Keling, farqlarini aniq ko'rsataman:

   1. `WSGI` - Bu QOIDALAR TO'PLAMI (`Spetsifikatsiya`= "texnik xujjat")
      - **Nima?:** `Python` ilovalari va serverlari qanday muloqot qilishi kerakligini belgilaydigan texnik standart
      - **Vazifasi:** "Frameworklar (`Django`, `Flask`) serverlar (`Nginx`, `Apache`) bilan qanday gaplashishi kerak" degan qoidalar
      - **Misol:**
        - `def application(environ, start_response):` - Bu `WSGI` standartiga mos funksiya

   2. `Gunicorn` - Bu `WSGI` STANDARTIGA AMAL QILUVCHI SERVER
      - **Nima?:** `WSGI` qoidalarini amalga oshiradigan haqiqiy dastur
      - **Vazifasi:** `Python` kodini ishga tushiradi va `veb-serverga` ulaydi
      - **Xususiyati:**
        - `gunicorn myapp:app` - Bu buyruq `WSGI` ilovasini ishga tushiradi

   **Hayotiy Misol bilan Tushuntiraman:**

   **Restoran Analogiyasi:**  
   - `WSGI` - "Ofitsiant qanday xolatda kelishi, buyurtmani qanday qabul qilishi, stolga qanday qo'yishi kerak" degan qoidalar
   - `Gunicorn` - Bu qoidalarga amal qiluvchi haqiqiy ofitsiant
   
   **Kompyuter Analogiyasi:** 
   -  `WSGI` - `USB` standarti (qurilmalar qanday ulanishi kerak)
   - `Gunicorn` - `USB` porti (haqiqiy ulanish nuqtasi)

   **Nimaga Ikkalasiga Ham Ehtiyoj Bor?**
   1. **WSGI `Gunicornsiz`:**
      - Qoidalar bor, lekin ularni amalga oshiradigan dastur bo'lmasa (`Gunicorn`), ilova ishlamaydi
   2. **`Gunicorn` `WSGIsiz`:**
      - `Server` bor, lekin u qanday `Python` ilovalari bilan ishlashni bilmaydi (standart yo'q)
      
   **Muhim nuqta:** `Gunicorn` `WSGI` standartiga amal qiladi, shuning uchun u `Django`, `Flask` kabi har qanday `WSGI`-ga mos framework bilan ishlay oladi.

   **Qisqacha:**
   - **WSGI** = "Qanday qilish kerak" qo'llanmasi
   - **Gunicorn** = Shu qo'llanmaga amal qiluvchi ishchi






















































































