
### Quyida ketirilgan misollarda ushbu SQL datatable ulanishlaridan foydalanilgan:

[sql diagram](https://lucid.app/lucidchart/0f17ca6c-8b14-4f83-9d18-bc37732c3d13/edit?viewport_loc=-897%2C-134%2C1279%2C592%2C0_0&invitationId=inv_f835fc18-8012-4850-9a28-d88e92918a33)

![Bu rasm tavsifi](static/images/foodie-sql-table.png)




### 1. Framwork nima?

>__Framework__ - bu dasturchilar uchun ilovalarni tez va samarali qurish imkonini beruvchi asboblar to'plamidir. 

<ul>
  <li> <b>Asboblar:</b> Dasturchilar uchun foydali bo'lgan dasturiy ta'minot vositalari.</li>
  <li> <b>Kutubxonalar:</b> Dasturchilar tomonidan tez-tez ishlatiladigan kodlar to'plami.</li>
  <li> <b>Konvensiyalar:</b> Dasturlash jarayonida qo'llaniladigan qoidalar va standartlar</li>
</ul>

### 2. Django nima?

>__Django__ - bu veb-ilovalarni tez va samarali yaratish uchun mo'ljallangan Python asosidagi veb frameworkdir. 
 
<ul>
  <li> <b>Tez rivojlanish:</b> Django dasturchilarga ilovalarni tezda yaratishga yordam beradi.</li>
  <li> <b>Xavfsizlik:</b> Django xavfsizlikni ta'minlash uchun ko'plab o'rnatilgan funksiyalarni taklif etadi..</li>
  <li> <b>Kengaytirilgan imkoniyatlar:</b> Django ORM (Object-Relational Mapping) orqali ma'lumotlar bazasi bilan oson ishlash imkonini beradi</li>
</ul>

### 3. HTTP(Hypertext Transfer Protocol) nima?

>vebda ma'lumotlarni uzatish uchun ishlatiladigan protokol.

<ul>
  <li> <b>GET:</b> Ma'lumot olish.</li>
  <li> <b>POST:</b> Ma'lumot yuborish</li>
  <li> <b>PUT:</b> Ma'lumotni yangilash.</li>
  <li> <b>DELETE:</b> Ma'lumotni o'chirish..</li>
</ul>

### 4. FTP (File Transfer Protocol) nima?

>Bu fayllarni tarmoq orqali uzatish uchun ishlatiladigan protokol. FTP yordamida foydalanuvchilar fayllarni serverga yuklash yoki serverdan yuklab olish imkoniyatiga ega.

### 5. IDE (Integrated Development Environment) nima?

>Environment) - bu dasturchilar uchun mo'ljallangan dasturiy ta'minot bo'lib, u kod yozish, tahrirlash, sinovdan o'tkazish va dasturlarni ishlab chiqish jarayonini osonlashtiradi. IDE quyidagi asosiy komponentlarga ega

<ul>
  <li> <b>Kod tahrirlovchi:</b> Kodni yozish va tahrirlash uchun qulay interfeys.</li>
  <li> <b>Konsol:</b> Dastur natijalarini ko'rish uchun.</li>
  <li> <b>Debugger:</b> Dasturdagi xatolarni aniqlash va tuzatish uchun.</li>
  <li> <b>Versiya nazorati:</b> Kodning turli versiyalarini boshqarish imkoniyati.</li>
</ul>

### 6. Loyihada muhit o'zgauchisi qanday buyruq yordamida o'rtantiladi?

> python3 -m venv venv


### 7. Venv qanday activlashtiriladi(Windows va Mac)?

```/venv/Scripts/activate | source/venv/bin/activate```

### 8. Django framowork o'rnatish buyrug'i?

```pip install django```

### 9. Djangoda loyihasini yaratish uchun qanday buyruqdan foydalanasiz?

```django-admin startproject project_name```

### 10. ```django-admin startproject project_name``` va ```django-admin startproject project_name .``` buyruqlarining farqi

<ul>
  <li> Agar siz <b>.</b> ni qo'shsangiz, loyiha joriy papkaga yaratiladi. </li>
  <li> Agar siz <b>.</b> ni qo'shmasangiz, yangi papka yaratiladi va loyiha shu papkada joylashadi. </li>
</ul>

### 11. setting.py ichida INSTALLED_APPS nima uchun kerak?
> Loyihangizda ishlatiladigan ilovalarni __(apps)__ ro'yxatini belgilaydi.

### 12. MIDDLEWARE nima uchun kerak?

>Django'da __HTTP__ so'rovlarini va javoblarini boshqarish uchun ishlatiladigan komponentlar to'plami.

<ul>
    <li> <b>Middleware</b> so'rovlar va javoblar ustida ishlash imkonini beradi, masalan, so'rovlarni autentifikatsiya qilish yoki javoblarni formatlash.</li>
    <li> <b>Middleware</b> xavfsizlikni ta'minlash uchun ishlatilishi mumkin, masalan, <b>Cross-Site Request Forgery (CSRF)</b> himoyasi yoki <b>XSS (Cross-Site Scripting)</b> hujumlariga qarshi himoya.</li>
    <li> <b>Middleware</b> sessiyalarni va cookie fayllarini boshqarish imkonini beradi, bu esa foydalanuvchi ma'lumotlarini saqlashda yordam beradi</li>
</ul>  

### 13. ROOT_URLCONF nima uchun kerak?

>__Django__ da URL marshrutizatsiyasini boshqarish uchun ishlatiladigan parametr. 

### 14. TEMPLATES nima uchun kerak?

>__Django__ da HTML shablonlarini boshqarish uchun ishlatiladigan parametr. 

### 15. ```sgi.py``` va ```vsgi.py``` nima uchun kerak?

> Django ilovalarini serverga joylashtirishda ishlatiladigan fayllar.

<ul>
    <li> <b>ASGI (Asynchronous Server Gateway Interface)</b> fayli asinxron ilovalar uchun mo'ljallangan. Bu, Django ilovalarining asinxron xususiyatlarini qo'llab-quvvatlash imkonini beradi, masalan, <b>WebSocketlar</b> va boshqa asinxron protokollar.</li>
    <li> <b>WSGI (Web Server Gateway Interface)</b> fayli asinxron bo'lmagan ilovalar uchun mo'ljallangan. Bu, <b>Django</b> ilovalarini an'anaviy <b>HTTP</b> serverlar bilan bog'lash imkonini beradi.</li>
</ul>  

### 16. ```urls.py``` nima uchun kerak?

>__Django__ ilovasida __URL__ marshrutizatsiyasini boshqarish uchun ishlatiladigan fayl. 


### 17. ```manage.py``` nima uchun kerak?

>__Django__ ilovalarini boshqarish uchun ishlatiladigan muhim fayl

### 18. Djangoda app nima uchun kerka?

>Loyiha ichida ma'lum bir vazifani bajaradigan mustaqil moduldir. __Django arxitekturasida__, bir loyiha bir nechta ilovalarni o'z ichiga olishi mumkin

<ul>
    <li> <b>Modularlik</b> Har bir app o'z vazifasini bajaradi, bu esa kodni tartibga solishga yordam beradi.</li>
    <li> <b>Qayta foydalanish</b> Bir app boshqa loyihalarda ham ishlatilishi mumkin, bu esa kodni qayta ishlatishni osonlashtiradi</li>
    <li> <b>Kengaytirilish</b> Loyiha o'sgan sari yangi app'lar qo'shish mumkin, bu esa loyihani kengaytirishni osonlashtiradi.</li>
</ul>  

### 19. Django da yangi app yaratish uchun qanday buyruqdan foydalanasiz?

 ```python manage.py startapp app_nomi```

### 20. app  ichidagi admin.py nim uchun kerak

>__Admin__ interfeysini boshqarish uchun ishlatiladi. Bu faylda siz o'z __app__ ingizdagi modellarning admin panelda qanday ko'rsatilishini belgilaysiz. 

### 21. app  ichidagi views.py nim uchun kerak?

> __Web__ ilovangizning biznes logikasini va foydalanuvchi so'rovlariga qanday javob berilishini belgilaydi. Bu faylda siz foydalanuvchilarga ko'rsatiladigan ma'lumotlarni tayyorlaysiz va ularni __HTML__ shablonlariga uzatasiz

### 22. app  ichidagi urls.py nim uchun kerak?

> Bu faylda siz foydalanuvchilarning so'rovlarini qaysi __view funksiya__ siga yo'naltirishni belgilaysiz.


### 23. Asosiy ```urls.py``` ichidagi ```from django.urls import include``` nima uchun kerak?

>Asosiy ```urls.py``` faylida __include__ funksiyasini ishlatib, __app__ ining __URL__ larini qo'shishingiz mumkin.

### 24. ```app``` ichidagi ```views.py``` modulidagi ```from django.shortcuts import render``` nima uchn kerak?

> __HTML__ shablonlarini render qilish uchun ishlatiladi. Bu funksiya, ma'lumotlarni __HTML__ shabloniga uzatish va foydalanuvchiga ko'rsatish jarayonini osonlashtiradi.

<ul>
    <li> Siz belgilangan shablonni yuklab olasiz. </li>
    <li> Siz shablonga ma'lumotlarni uzatishingiz mumkin, bu esa foydalanuvchiga ko'rsatiladigan dinamik kontentni yaratadi. </li>
    <li> <b>render</b> funksiyasi avtomatik ravishda <b>HTTP</b> javobini yaratadi va uni qaytaradi.</li>
</ul> 

```python
from django.shortcuts import render

def index(request):
    context = {
        'message': 'Salom, Dunyo!'
    }
    return render(request, 'index.html', context)
```

### 25. ```request``` nima uchun kerak?

<ul>
    <li> Siz foydalanuvchining yuborgan ma'lumotlarini, masalan, formalar yoki URL parametrlarini olish uchun request obyektidan foydalanasiz. </li>
    <li> So'rovning qaysi HTTP metodidan (GET, POST, va hokazo) foydalanayotganini aniqlashingiz mumkin. </li>
    <li> Siz foydalanuvchi sessiyasi va cookie ma'lumotlariga kirishingiz mumkin.</li>
</ul> 

```python
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    if request.method == 'POST':
        user_input = request.POST.get('input_field')
        return HttpResponse(f"Siz kiritgan ma'lumot: {user_input}")
    return render(request, 'index.html')
```
```python
{
    'method': 'GET',  # So'rovning HTTP metodi (GET, POST, va hokazo)
    'path': '/sandbox/',  # So'rov qilingan URL yo'li
    'GET': {            # URL parametrlarini o'z ichiga oladi
        'param1': 'value1',
        'param2': 'value2',
    },
    'POST': {           # Form ma'lumotlarini o'z ichiga oladi
        'input_field': 'user_input_value',
    },
    'COOKIES': {        # Foydalanuvchi cookie ma'lumotlari
        'cookie_name': 'cookie_value',
    },
    'session': {        # Foydalanuvchi sessiya ma'lumotlari
        'session_key': 'session_value',
    },
    'user': <User object>,  # Foydalanuvchi obyekti (agar autentifikatsiya qilingan bo'lsa)
    'is_ajax': False,  # So'rov AJAX orqali yuborilganmi yoki yo'q
    'headers': {        # So'rov sarlavhalari
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/json',
    },
}
```

### 26. from django.http import HttpResponse nima uchun kerak?

>```HTTP``` javoblarini yaratish uchun ishlatiladi. Bu funksiya, serverdan foydalanuvchiga ma'lumotlarni yuborish jarayonini osonlashtiradi.


<ul>
    <li> <b>Javob yaratish:</b>  Siz foydalanuvchiga yuboriladigan HTTP javobini yaratishingiz mumkin. Bu javob, HTML, JSON, yoki boshqa formatlarda bo'lishi mumkin. </li>
    <li> <b>Kontentni belgilash:</b> Siz javobning kontentini va uning turini (masalan, text/html, application/json) belgilashingiz mumkin.</li>
    <li> <b>Status kodini belgilash: </b> Siz javobning HTTP status kodini (masalan, 200, 404, 500) belgilashingiz mumkin.</li>
</ul>  

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Salom, Dunyo!", status=201)  # 201 Created
```

### 27. MVT (Model-View-Template) nima va nima uchun kerak?

> __Django__ da web ilovalarini yaratish uchun ishlatiladigan arxitektura tamoyilidir. 

<ul>
    <li> <b>Model:</b>Model ma'lumotlar tuzilishini belgilaydi. Bu yerda siz ma'lumotlar bazasida qanday ma'lumotlar saqlanadi va ularning qanday bog'lanishi kerakligini aniqlaysiz.  Model yordamida siz ma'lumotlar bazasiga so'rovlar yuborishingiz va ma'lumotlarni olish yoki saqlashingiz mumkin. Django ORM (Object-Relational Mapping) orqali bu jarayonni osonlashtiradi. </li>
    <li> <b>View:</b> Bu yerda siz ilovangizning biznes mantiqini belgilaysiz. Foydalanuvchidan kelgan so'rovni qabul qiladi, kerakli ma'lumotlarni modeldan oladi va bu ma'lumotlarni shablonga uzatadi. Views da foydalanuvchiga ko'rsatiladigan ma'lumotlarni tayyorlaydi.</li>
    <li> <b>Template:</b> Shablon foydalanuvchiga ko'rsatiladigan ma'lumotlarni taqdim etadi. Views tomonidan uzatilgan ma'lumotlar shablon ichida ko'rsatiladi. </li>
</ul>  

### 28. MVT jarayoni ketma-ketligi qanday amalga oshiriladi

<ul>
    <li> <b>Foydalanuvchi so'rovi:</b> Foydalanuvchi brauzerda URL manzilini kiritadi.</li>
    <li> <b>URL Dispatcher:</b> Django URL dispatcher'i so'rovni qabul qiladi va mos keladigan vista'ni aniqlaydi.</li>
    <li> <b>Views:</b> Views modeldan ma'lumotlarni oladi va shablonni tanlaydi.</li>
    <li> <b>Model: </b> Model ma'lumotlar bazasidan kerakli ma'lumotlarni olish uchun ishlatiladi.</li>
    <li> <b>Taplate:</b> Shablon ma'lumotlarni ko'rsatish uchun tayyorlanadi.</li>
    <li> <b>Respose: </b> Tayyorlangan HTML foydalanuvchiga qaytariladi.</li>
</ul>

![Bu rasm tavsifi](static/images/mvt.png)

### 29. `choise()` funksiyasi nima vazifani bajardi?

> `choice()` funksiyasi Python dasturlash tilida tasodifiy elementni tanlash uchun ishlatiladi. Bu funksiya random modulidan keladi va berilgan ro'yxatdan (yoki ketma-ketlikdan) tasodifiy bir elementni qaytaradi.
```python
from random import choice
fruits = ['olma', 'banan', 'mango', 'apelsin']
random_fruit = choice(fruits)
print(random_fruit)
```
### 30. URL dispatcher nima uchun kerak?

> Bu __veb-ilovalar__ uchun muhim komponent bo'lib, u foydalanuvchi so'rovlarini qabul qiladi va ularni to'g'ri ko'rinishga __(view)__ yo'naltiradi. 

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

### 31. Djangoda  `wievs.py` nima uchun kerak?

> __Django__ da `views.py` fayli muhim rol o'ynaydi, chunki u ma'lumotlarni ko'rsatish va mijoz so'rovlariga javob berish uchun zarur bo'lgan logikani o'z ichiga oladi. views.py faylida quyidagi asosiy vazifalar bajariladi:

<ul>
    <li> <b>So'rovlarni qabul qilish:</b> Mijozdan kelgan so'rovlarni qabul qiladi.</li>
    <li> <b>Ma'lumotlarni olish:</b> Agar kerak bo'lsa, ma'lumotlarni modeldan olish uchun bog'lanadi.</li>
    <li> <b>Javobni tayyorlash:</b> Olingan ma'lumotlarni shablon (template) bilan birlashtirib, foydalanuvchiga ko'rsatish uchun tayyorlaydi.</li>
    <li> <b>Javobni yuborish:</b>  Tayyorlangan javobni foydalanuvchiga qaytaradi.</li>
</ul>  

> Bu jarayon Django'ning __Model-View-Template (MVT) arxitekturasining__ bir qismi sifatida ishlaydi. 

![Bu rasm tavsifi](static/images/views-mvt.png)

![Bu rasm tavsifi](static/images/views-function.png)

### 32. DTL nima ?

> Bu __Django__ web ramkasida dinamik ma'lumotlarni ko'rsatish uchun ishlatiladigan shablon tilidir. __DTL__ yordamida __HTML__ shablonlarida o'zgaruvchilar va __Teg__ lar yaratish mumkin. 

### 33. `Teg` lar deb nimaga aytiladi? 

> Teglar (tags) __DTL (Django Template Language)__ da ma'lum bir funktsiyani bajarish uchun ishlatiladigan buyruqlardir. Ular shablon ichida dinamik mantiqiy operatsiyalarni amalga oshirishga yordam beradi. Teglar, odatda, `{% %}` qavslar ichida yoziladi. 
 
### Misol uchun:
1. Shartli ifoda (if tag):

```python
{% if user.is_authenticated %}
    <p>Salom, {{ user.username }}!</p>
{% else %}
    <p>Salom, mehmon!</p>
{% endif %}
```
2. Sikl (for tag):

```python
<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```
3. Blok (block tag):

```python
{% block content %}
    <h1>Bu asosiy kontent</h1>
{% endblock %}
```

### 34. `backticks`  nima ?
>  (`) - bu kodni formatlash uchun ishlatiladigan maxsus belgilardir.

### 35. Django loyhasida standart papkalar struktusi qanday bo'ladi?

```
myproject/
│
├── myapp/                  # Django ilovasi (app)
│   ├── migrations/         # Ma'lumotlar bazasi migratsiyalari
│   ├── templates/          # Shablonlar
│   │   └── myapp/         # Ilovaga tegishli shablonlar
│   ├── static/             # Statik fayllar (CSS, JavaScript, rasmlar)
│   ├── __init__.py
│   ├── admin.py            # Admin interfeysi konfiguratsiyasi
│   ├── apps.py             # Ilova konfiguratsiyasi
│   ├── models.py           # Ma'lumotlar bazasi modellari
│   ├── tests.py            # Testlar
│   └── views.py            # Ko'rinishlar (views)
│
├── myproject/              # Loyihaning asosiy papkasi
│   ├── __init__.py
│   ├── settings.py         # Loyihaning sozlamalari
│   ├── urls.py             # URL marshrutlari
│   └── wsgi.py             # WSGI interfeysi
│
├── manage.py                # Loyihani boshqarish uchun skript
│
└── requirements.txt         # Loyihada foydalaniladigan kutubxonalar ro'yxati
```

### 36. `Django` da shablon orqali ma'lumotlarni o'tkazish qanday amalga oshiriladi? 

### `views.py`
```python
from django.shortcuts import render

def my_view(request):
    data = {
    'name': 'Paulo',
    'age': 123
}

    return render(request, 'index.html', {"data_test":data})
```
####  Ushbu shakilda ma'lumot berish standart. Bu yerda `return render(request, 'index.html', {"data_test":data})` ning juda muhim joyi bor ya'ni `{"data_test":data}` bu standart, shunday yozish orqali yartailga ma'lumotlarni `data_test` ga o'rab keyin shablonga uzatamiz.
#### `index.html`
```html
<h1>Salom, {{ data_test.name }}</h1>
<p>Yoshingiz {{ data_test.age }}.</p>
```

### 37. Asosiy `base.html` shablonni yaratish va uni kengaytirish djangoda, bu qanday amalga oshiriladi batafsil ko'rsating.

1. `base.html` fayli __Django__ loyihasining shablonlar `(templates)` papkasida joylashishi kerak.
```
myproject/
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   └── myapp/
│   │       └── base.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```
2. `{% block content %}`: Asosiy shablonda, boshqa shablonlar ushbu blokni kengaytirishi uchun joy ajratish kerak. 

`base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Asosiy Shablon</title>
</head>
<body>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
```
3. `base.html` aosida yangi `index.html` ni yaratamiz.

> Yaratish sintaksisi: `index.html` faylida quyidagi kodni qo'shing:

`index.html`

```html
{% extends "base.html" %}

{% block content %}
    <h1>Salom, Django!</h1>
    <p>Bu mening birinchi sahifam.</p>
{% endblock %}
```

### 38. `Django` da modellari va ma'lumotlar bazalari haqida nimalar bilasiz?

> `Django` da modellar ma'lumotlarni qanday saqlash va boshqarish uchun ishlatiladi. Ular ma'lumotlar bazasidagi jadvallarni ifodalaydi va ma'lumotlar bilan ishlashni osonlashtiradi.
- `Model`: __Django__ da har bir model bir sinf sifatida yaratiladi va bu sinf ma'lumotlar bazasidagi jadvalni ifodalaydi.
- `ORM` (Object-Relational Mapping): `Django` `ORM` ma'lumotlar bazasi bilan ishlashni osonlashtiradi, bu orqali `SQL` so'rovlarini yozmasdan ma'lumotlarni qo'shish, o'chirish va yangilash mumkin.

### 39. `django` da yangi `app` ichidagi `urls.py` ichida `app_name` nima uchun kerak?

> `Django` da `urls.py` faylida `app_name` ni belgilashning maqsadi, `URL` nomlarini o'zaro farqlash va `namespacing` (nomlar maydoni) yaratishdir. Bu, bir nechta ilovalar `(apps)` bo'lgan loyihalarda `URL` larni boshqarishni osonlashtiradi. 

- `Nomlar to'qnashuvini oldini olish:` Agar bir xil nomli `URL` lar bo'lsa, `app_name` yordamida ularni farqlash mumkin.
- 
- __`URL` larni chaqirishda qulaylik:__ `app_name` yordamida `URL` larni chaqirishda to'g'ri ilovaga murojaat qilish osonlashadi.

#### Misol uchun:

> Agar sizda `blog` va `shop` ilovalari bo'lsa, har birining `urls.py` faylida `app_name` ni belgilash orqali, siz `blog:index` va `shop:index` kabi `URL` larni chaqirishingiz mumkin.

` Blog ilovasi` da  `urls.py` faylida `app_name` ni belgilash:

```python
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.detail, name='detail'),
]
```

`Shop ilovasi` da `urls.py` faylida `app_name` ni belgilash:

```python
# shop/urls.py
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/', views.detail, name='detail'),
]
```
Endi, agar siz `blog` ilovasidagi `index` `URL` ni chaqirmoqchi bo'lsangiz, siz quyidagicha yozasiz:

```html
# templates/blog/index.html
<a href="{% url 'blog:index' %}">Blog Bosh Sahifasi</a>
```
Agar `shop` ilovasidagi `index` `URL` ni chaqirmoqchi bo'lsangiz, siz quyidagicha yozasiz.

```html
# templates/shop/index.html
<a href="{% url 'shop:index' %}">Do'kon Bosh Sahifasi</a>
```

### 40. `Django` da `Shablonlar(templates)` katalogini loyiha darajasida qayta tashkil etish?

- Loyihangizning asosiy papkasida yangi `templates` papkasini yarating. Ushbu papkada umumiy shablonlar, masalan, `base.html` faylini joylashtiring.

- Django loyihangizning `settings.py` faylida shablonlar katalogini ko'rsatishingiz kerak. Buning uchun `TEMPLATES` bo'limida `DIRS` ro'yxatiga yangi shablonlar papkasini qo'shing.

`settings.py`

```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 41. `Django` dagi `migrations` lar haqida nima bilasiz?

>  `Migrations` — bu ma'lumotlar bazasi sxemasini modellarga moslashtirish uchun ishlatiladigan mexanizmdir. 

- `Ta'rif`: `Migrations` — bu `Django` ilovangizning ma'lumotlar bazasi sxemasidagi o'zgarishlarni kuzatib boradigan fayllardir. Ushbu fayllar ma'lumotlar bazasi jadvallarini yaratish, yangilash yoki o'chirish kabi jarayonlarni o'z ichiga oladi.
- `Migrations papkasi`: Har bir `Django` ilovasi yaratilganda, avtomatik ravishda migrations papkasi yaratiladi. Ushbu papka, ilovangizning ma'lumotlar bazasi o'zgarishlarini o'z ichiga olgan `migration` fayllarini saqlaydi.
- `Qo'llash`: `Migrations` ni qo'llash uchun terminalda `python manage.py migrate` buyrug'ini ishlatasiz. Ushbu buyruq, barcha `migration` fayllarini bajarib, ma'lumotlar bazangizni yangilaydi.

### 42. `Migratsiya` fayllari qanday yaratiladi?

> `Django` da `migratsiya` fayllarini yaratish uchun quyidagi qadamlarni bajarishingiz kerak:

1. `Modelni yaratish`: Avval, `Django` ilovangizda modelni aniqlang. `Model` — bu ma'lumotlar bazasidagi jadvalni ifodalovchi `Python` klassidir.
2.  `Migratsiya yaratish`: `Modelni` yaratgandan so'ng, terminalda quyidagi buyruqni bajarishingiz kerak: `python manage.py makemigrations` Bu buyruq, `Django` ga modeldagi o'zgarishlarni aniqlash va ularga mos keladigan migratsiya faylini yaratish uchun ko'rsatma beradi.
3. `Migratsiya` faylini tekshirish: `makemigrations` buyrug'ini bajarganingizdan so'ng, `migrations` papkasida yangi migratsiya fayli paydo bo'ladi. Ushbu fayl, modeldagi o'zgarishlarni aks ettiradi.
4. `Migratsiyani qo'llash`: Yaratilgan migratsiya faylini ma'lumotlar bazasiga qo'llash uchun quyidagi buyruqni bajarishingiz kerak: `python manage.py migrate`

### 43. `python manage.py shell`  buyrug'i nima uchun ishlatilinadi?

> Bu buyruq `Django` loyihangizning interaktiv `Python shell` ini ochadi, bu orqali siz `Django` modellariga va ma'lumotlar bazasiga murojaat qilishingiz mumkin. 

`Django shell`ida qilishingiz mumkin bo'lgan ba'zi ishlar:

- `Ma'lumotlar bazasini so'rov qilish`: `Modellarni` import qilib, ma'lumotlar bazasidan ma'lumotlarni olish yoki o'zgartirish uchun so'rovlar yuborishingiz mumkin.
- `Obyektlar yaratish`: `Modellarni` yangi `instansiyalarini` yaratib, ularni ma'lumotlar bazasiga saqlashingiz mumkin."`Instansiya(obyekt)`  `modelga` mos keladigan ma'lumotlar to'plamini ifodalaydi. Masalan, agar sizda "Kategoriyalar" modeli bo'lsa, unda har bir kategoriya (masalan, "Desert" yoki "Salat") `modelning` bir `instansiya`si hisoblanadi. Umman olganda `instansiya` bu `obyekt` desak ham bo'ladi"
- Kod qismlarini sinab ko'rish: `Python` kodini bajarib, funksiyalarni sinab ko'rish yoki muammolarni hal qilish uchun foydalanishingiz mumkin.

### 44. `Category.objects.all()` ushbu buyruq nima vazifani bajaradi?

> `Django ORM (Object-Relational Mapping)` da ishlatiladigan bir buyruqdir. Bu buyruq, `Category modeli` orqali ma'lumotlar bazasidagi barcha kategoriya obyektlarini olish uchun ishlatiladi.

`Tushuntirish:`
- `Category`: Bu sizning `Django` modelingiz. Masalan, agar sizda `Kategoriyalar` nomli model bo'lsa, u `Category` deb ataladi.
- `objects`: Bu `Django` modelining standart manageridir. U orqali siz ma'lumotlar bazasidagi obyektlar bilan ishlashingiz mumkin. `objects` manageri yordamida siz ma'lumotlarni __olish__, __yaratish__, __yangilash__ va __o'chirish__ kabi operatsiyalarni bajarishingiz mumkin.
- `all()`: Bu metod, ma'lumotlar bazasidagi barcha obyektlarni olish uchun ishlatiladi.

> `Obyekt yartaishi`: `cat = Category.objects.create(name="Paulo")`

### 45. `Django` loyihasida super user yaratish  buyruqi qanday?

> `python manage.py createsuperuser` ushbu buyruq kiritilgandan keyin `username`, `mail` va `password` kiritasiz. `User` yartailgandan so'ng `http://127.0.0.1:8000/admin` manzilig o'ting.

### 46.  `Django` app ichidagi `admin.py` ichidagi `admin.site.register()` funksiyasi qanday vazifani bajaradi?

> `Modelni ro'yxatdan o'tkazish`: `admin.site.register()` funksiyasi yordamida siz `Django admin` panelida ko'rsatmoqchi bo'lgan modelni ro'yxatdan o'tkazasiz. Bu `model` sizning ma'lumotlar bazangizda mavjud bo'lgan ma'lumotlarni ifodalaydi.
> `Admin` interfeysini yaratish: `Model`  ro'yxatdan o'tgach, `admin` panelida ushbu `modelga` tegishli bo'lgan barcha ma'lumotlarni `ko'rish`, `qo'shish`, `o'zgartirish` va `o'chirish` imkoniyatiga ega bo'lasiz. Bu, masalan, yangi kategoriya qo'shish yoki mavjud kategoriyalarni tahrirlash uchun qulay interfeysni taqdim etadi.
>  Misol uchun, agar siz  `modelni` ro'yxatdan o'tkazmasangiz, `admin` panelida ushbu `modelga` oid ma'lumotlarni `ko'rish` yoki `boshqarish` imkoniyatingiz bo'lmaydi.

### 47. `timezone.now()`  funksiyani tushuntiring?

> `timezone.now()` funksiyasi  hozirgi vaqtini qaytaradi. Format: `2023-10-05 14:30:45+00:00`

### 48. `Administrator` interfeysini sozlash va `modellarda` koʻproq maydonlarni koʻrsatish.

> `ModelAdmin` klassidan foydalanishingiz mumkin. Quyidagi qadamlar orqali buni amalga oshirishingiz mumkin:

1. `ModelAdmin klassini yaratish`: Siz `ModelAdmin` `class` idan meros olgan yangi `class` yaratasiz.
```python
from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added')  # Ko'rsatmoqchi bo'lgan maydonlar
```
2. `Modelni` ro'yxatdan o'tkazish: Yangi `CategoryAdmin` `class` ini o'z modelingiz bilan ro'yxatdan o'tkazing.
```python
admin.site.register(Category, CategoryAdmin)
```

### 49. `Django` da `admin` interfeysini boshqarish uchun ishlatiladi. Keling, uning ba'zi muhim xususiyatlarini ko'rib chiqamiz:

1. `list_display`: Bu xususiyat `admin` panelida ko'rsatiladigan maydonlarni belgilaydi. `id`, `name`, va `date_added` maydonlari `admin` panelida ko'rsatiladi.

`app/admin.py`

```python
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added')
```

2. `list_filter`: Bu xususiyat admin interfeysida filtrlar qo'shish imkonini beradi. Foydalanuvchilar `date_added` bo'yicha `filtrlar` qo'shishlari mumkin.

`app/admin.py`

```python
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('date_added',)
```

3. `search_fields`: Bu xususiyat qidiruv maydonlarini belgilaydi. Foydalanuvchilar `name` maydoni bo'yicha qidiruv o'tkazishlari mumkin.

`app/admin.py`

```python
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
```
4.  `actions`: Bu xususiyat `admin` interfeysida bajarilishi mumkin bo'lgan harakatlar ro'yxatini belgilaydi. Foydalanuvchilar bir nechta kategoriyalarni tanlab, ularni `featured` deb belgilashlari mumkin.

`app/admin.py`

```python
class CategoryAdmin(admin.ModelAdmin):
    actions = ['mark_as_featured']

    def mark_as_featured(self, request, queryset):
        queryset.update(is_featured=True)
```
5. `inlines`: Bu xususiyat boshqa modellarga bog'langan ma'lumotlarni ko'rsatish uchun ishlatiladi. `Category` modeliga bog'langan `Item` yozuvlarini ko'rsatish imkonini beradi.

```python
class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
```

### 50. `on_delete=models.CASCADE` qayerda va nima uchun ishlatilinadi?

> `Django` da `ForeignKey` maydonida ishlatiladigan parametrdir. Bu parametr, bog'langan ob'ekt (masalan, `Category modeli`) o'chirilganda, unga bog'langan barcha ob'ektlar (masalan, `Recipe modeli`) ham avtomatik ravishda o'chirilishini ta'minlaydi.

`Misol uchun:`

> Agar sizda `Desserts` nomli kategoriya bo'lsa va bu kategoriya ostida `Chocolate Cake` va `Ice Cream` retseptlari bo'lsa, `Desserts` kategoriya o'chirilganda, `Chocolate Cake` va `Ice Cream` retseptlari ham o'chiriladi.

### 51.  `Django QuerySet API` haqia nimalar bilasiz?

> `Django ORM (Object-Relational Mapping)` orqali ma'lumotlar bazasidan ma'lumotlarni olish va `manipulyatsiya` qilish uchun ishlatiladigan kuchli vositadir. Quyida asosiy tushunchalar keltirilgan:

- Bu ma'lumotlar bazasidagi so'rovlar to'plamidir. `QuerySetlar` `lazy evaluation` (sekin baholash) tamoyiliga asoslangan, ya'ni ma'lumotlar bazasidan ma'lumotlar faqat kerak bo'lganda olinadi.

`Asosiy metodlar`

1. `all()`: Barcha ob'ektlarni olish uchun ishlatiladi: 
    
    > Misol: "vegetarian" bo'lgan retseptlarni olish. `recipes = Recipe.objects.all()`


2. `filter()`: Berilgan shartlarga mos keladigan ob'ektlarni olish uchun ishlatiladi. 

    >Misol: "vegetarian" bo'lmagan retseptlarni olish.`vegetarian_recipes = Recipe.objects.filter(is_vegetarian=True)`
    

3. `exclude()`: Berilgan shartlarga mos kelmaydigan ob'ektlarni olish uchun ishlatiladi. 

    > Misol: "vegetarian" bo'lmagan retseptlarni olish. `non_vegetarian_recipes = Recipe.objects.exclude(is_vegetarian=True)`


4. `get()`: Berilgan shartlarga mos keladigan bitta ob'ektni olish uchun ishlatiladi. 

    > Misol: IDsi 1 bo'lgan retseptni olish. `recipe = Recipe.objects.get(id=1)`

5. `first()`: Birinchi ob'ektni olish. 

    > `recipe = Recipe.objects.get(id=1)`

6. `last():` Oxirgi ob'ektni olish. 

    >`last_recipe = Recipe.objects.all().last()`

7. `order_by()`: Natijalarni tartiblash. Misol: Retseptlarni nomi bo'yicha tartiblash. 

    > Misol: Retseptlarni nomi bo'yicha tartiblash. `ordered_recipes = Recipe.objects.all().order_by('name')`

8. `count()`: Ob'ektlar sonini hisoblash. `total_recipes = Recipe.objects.count()`


9. `distinct()`: Takrorlanuvchi ob'ektlarni olib tashlash. 

    > `unique_ingredients = Recipe.objects.values('ingredient').distinct()`

10. `values()`: Faqat kerakli maydonlarni olish. 

    > Misol: Faqat retsept nomlarini olish. `recipe_names = Recipe.objects.values('name')`

### 52.`Recipe.objects.filter(category__name__exact='salad')` ushbu kod sintaksisini tushuntirib bering!

`Sintaksis Tushuntirishi:`
1. `Recipe:`
    > Bu sizning modelingiz nomi. `Django` da har bir model ma'lumotlar bazasidagi bir jadvalni ifodalaydi. `Recipe` modeli retseptlar haqidagi ma'lumotlarni saqlaydi.
2. `objects:`
    > Har bir `Django` modeli `objects` manageriga ega. Bu manager yordamida siz modelga tegishli so'rovlarni amalga oshirishingiz mumkin.
   
3. `filter():`
    >Bu metod ma'lum shartlarga mos keladigan ob'ektlarni olish uchun ishlatiladi. 

4. `category__name:`
    - Bu yerda category - `Recipe` modelidagi `ForeignKey` maydoni. `__` (ikki pastki chiziq) yordamida siz bog'langan modelning maydonlariga murojaat qilishingiz mumkin.
    - `name` - `category` modelidagi maydon. Bu maydon categoryning nomini ifodalaydi.

5. `exact:`
    - Bu parametr `filter()` metodiga berilgan shartni belgilaydi. `exact` yordamida siz aniq mos keladigan qiymatni qidirasiz.
    - Agar siz `iexact` ishlatsangiz, bu katta-kichik harflarga e'tibor bermaslikni anglatadi.
6. `'salad':`
   - Bu qidirilayotgan aniq qiymat. `filter()` metodi `category` modelidagi name maydoni `salad` ga teng bo'lgan barcha Recipe ob'ektlarini qaytaradi.
   
> Bu kod yordamida siz `Recipe` modelidan category maydoni salad bo'lgan barcha retseptlarni olish uchun so'rov yuborayapsiz.

### 53. `Django QuerySet API` da filtrlar va aniq maydonlarni qidirish haqida qanday tushunchalarga egasiz?

1. __Aniq maydonlar bilan qidirish:__
   - Agar siz ma'lum bir maydonning aniq qiymatini qidirayotgan bo'lsangiz, `exact` yoki `iexact` (katta-kichik harflarga e'tibor bermaslik uchun) parametrlaridan foydalanishingiz mumkin.
      __Misol uchun:__ `Recipe.objects.filter(category__name__exact='salad')`

2. __O'z ichiga olgan qidirish:__
   - Agar siz ma'lum bir qiymatni o'z ichiga olgan maydonlarni qidirayotgan bo'lsangiz, `contains` yoki `icontains` (katta-kichik harflarga e'tibor bermaslik uchun) parametrlaridan foydalanishingiz mumkin.
   - __Misol:__
      `Recipe.objects.filter(category__name__contains='salad')`
   
__Misollar:__
- __Aniq maydon bilan qidirish:__
   > recipes = Recipe.objects.filter(category__name__exact='Greek Salad')
- __O'z ichiga olgan maydon bilan qidirish:__
   > recipes = Recipe.objects.filter(category__name__contains='salad')

### 54. Istisno `(Exclude)` Filtri haqida nima bilasiz va ishlatish bo'yicha misol keltiring:

- Django'da `exclude()` metodi yordamida ma'lum shartlarga mos kelmaydigan obyektlarni olish mumkin.
- Masalan, agar siz `soup` so'zini o'z ichiga olgan barcha retseptlarni chiqarib tashlamoqchi bo'lsangiz, `exclude()` metodidan foydalanasiz.

`Misol:`

 ```python 
     # Retseptlar modelidan "soup" so'zini o'z ichiga olganlarni chiqarib tashlash
     recipes = Recipe.objects.exclude(name__contains='soup')
```
> Bu kodda `name__contains='soup'` sharti yordamida `soup` so'zini o'z ichiga olgan barcha retseptlar chiqarib tashlanadi.

### 55. __Django__ da `filter()` va `exclude()` metodlarida ishlatiladigan sintaksislar 

1. __Exact Match:__
   - __Sintaksis:__ `field_name='value'`
   - __Tushuntirish:__ Bu sintaksis ma'lum bir maydon `(field)` uchun aniq mos keladigan qiymatni qidiradi.
   - __Misol:__ `Recipe.objects.filter(name='Chicken Soup')`
     - Bu kod "Chicken Soup" nomli retseptlarni qaytaradi.

2. __Contains:__
   - __Sintaksis:__ `field_name__contains='value'`
   - __Tushuntirish:__ Bu sintaksis maydon ichida berilgan qiymatni o'z ichiga olgan obyektlarni qidiradi.
   - __Misol:__ `Recipe.objects.filter(name__contains='soup')`
     - Bu kod `soup` so'zini o'z ichiga olgan barcha retseptlarni qaytaradi.
   
3. __Starts With:__
   - __Sintaksis:__ `field_name__startswith='value'`
   - __Tushuntirish:__ Bu sintaksis maydonning qiymati berilgan qiymat bilan boshlanadigan obyektlarni qidiradi.
   - __Misol:__ `Recipe.objects.filter(name__startswith='Ch')`
     - Bu kod `Ch` bilan boshlanadigan barcha retseptlarni qaytaradi.

4. __Ends With:__
   - __Sintaksis:__ `field_name__endswith='value'`
   - __Tushuntirish:__ Bu sintaksis maydonning qiymati berilgan qiymat bilan tugaydigan obyektlarni qidiradi.
   - __Misol:__ `Recipe.objects.filter(name__endswith='soup')`
     - Bu kod `soup` bilan tugaydigan barcha retseptlarni qaytaradi.

5. __Greater Than / Less Than__
   - __Sintaksis:__
   - `field_name__gt=value (greater than)`, `field_name__lt=value (less than)`
   - __Tushuntirish:__ Bu sintaksis maydonning qiymati berilgan qiymatdan katta yoki kichik bo'lgan obyektlarni qidiradi.
   - __Misol:__ `Recipe.objects.filter(price__gt=10)`
     - Bu kod narxi 10 dan katta bo'lgan barcha retseptlarni qaytaradi.

6. __In__
   - __Sintaksis:__ `field_name__in=[value1, value2, ...]`
   - __Tushuntirish:__ Bu sintaksis maydonning qiymati berilgan ro'yxatdagi qiymatlardan biriga mos keladigan obyektlarni qidiradi.
   - __Misol:__ `Recipe.objects.filter(id__in=[1, 2, 3])`
     - Bu kod IDsi 1, 2 yoki 3 bo'lgan retseptlarni qaytaradi.

7. __Is Null:__
   - __Sintaksis:__ `field_name__isnull=True (or False) `
   - __Tushuntirish:__ Bu sintaksis maydonning qiymati `null` (bo'sh) yoki `null` emasligini tekshiradi.
   - __Misol:__ `Recipe.objects.filter(description__isnull=True)`
     - Bu kod tavsifi bo'lmagan `(null)` retseptlarni qaytaradi.
### 56. Chaining (zanjirli) Filtrlar:
   > `Django` da siz bir nechta filtrlarni birlashtirib ishlatishingiz mumkin. Bu sizga yanada aniqroq natijalarni olish imkonini beradi.
   - __Masalan:__
      - `Recipe.objects.filter(category__name='soup').exclude(name__contains='chocolate').order_by('-date_added')`
      > Bu kod `soup` kategoriyasidagi retseptlarni olib, `chocolate` nomini o'z ichiga olganlarini chiqarib tashlaydi va natijalarni `date_added` sanasi bo'yicha kamayish tartibida tartiblaydi.
     
### 57. Bir nechta filtrlarni yozish uchun `Django` da qanday usullar mavjud
   Django'da `filter()` metodini bir necha marta chaqirishingiz yoki bir nechta shartlarni bitta `filter()` metodida birlashtirishingiz mumkin. Keling, har ikkala usulni ko'rib chiqamiz:

1. Bir nechta `filter()` chaqirishi
   - Siz bir nechta `filter()` chaqiruvlarini `zanjir` qilib yozishingiz mumkin. Har bir chaqiruv natijani yanada toraytiradi:
      - `Recipe.objects.filter(category__name='soup').filter(ingredients__contains='chicken')`
      - Bu kod `soup` kategoriyasidagi va `chicken` ingredientini o'z ichiga olgan retseptlarni qaytaradi.

   2. Bir nechta shartlarni bitta `filter()` ichida birlashtirish
      - Siz bir nechta shartlarni bitta `filter()` chaqiruvida `&` (va) yoki `|` (yoki) operatorlari yordamida birlashtirishingiz mumkin:

      ```python
      from django.db.models import Q
      Recipe.objects.filter(Q(category__name='soup') & Q(ingredients__contains='chicken'))
      ```
      Bu kod ham `soup` kategoriyasidagi va `chicken` ingredientini o'z ichiga olgan retseptlarni qaytaradi.

### 58. QuerySet API - Slicing QuerySets and Aggregation.
   - __Kesish sintaksisi:__ `queryset = Model.objects.all()[start:end]`
      - `start`: Qaysi indeksdan boshlash kerakligini ko'rsatadi.
      - `end`: Qaysi indeksgacha olish kerakligini ko'rsatadi.

     #### Misol:
      ```python
      # 0 dan 3 gacha bo'lgan yozuvlarni olish
      recipes = Recipe.objects.all()[:3]
      ```
   - __QuerySetlarni yig'ish:__
      - Django'da QuerySet'larni yig'ish, ma'lumotlar ustida hisob-kitoblar o'tkazish imkonini beradi. Buning uchun Django'da agregatsiya funksiyalari mavjud, masalan, count, sum, average, min, va max.
      - __Agregatsiya sintaksisi:__

      ```python
      from django.db.models import Count, Avg
      
      # Yozuvlar sonini hisoblash
      total_recipes = Recipe.objects.aggregate(Count('id'))
      
      # O'rtacha qiymatni hisoblash
      average_price = Recipe.objects.aggregate(Avg('price'))
      ```

      #### Misol:
      ```python
      # Yozuvlar sonini olish
      total_recipes = Recipe.objects.aggregate(Count('id'))  # Natija: {'id__count': 5}
      
      # O'rtacha narxni olish
      average_price = Recipe.objects.aggregate(Avg('price'))  # Natija: {'price__avg': 20.5}
      ```
      #### Quyida eng ko'p ishlatiladigan `agregatsiya` metodlari keltirilgan:
      1. __Count:__
         - __Tavsifi:__ Yozuvlar sonini hisoblaydi.
         - __Sintaksisi:__
            ```python
              from django.db.models import Count
              total = Model.objects.aggregate(Count('field_name'))
            ``` 
      2. __Sum:__ 
         - __Tavsifi:__ Berilgan maydon bo'yicha qiymatlarning yig'indisini hisoblaydi.
         - __Sintaksisi:__
             ```python                                             
               from django.db.models import Sum
               total_sum = Model.objects.aggregate(Sum('field_name'))
             ```                                                   
      3. __Avg:__
         - __Tavsifi:__ Berilgan maydon bo'yicha o'rtacha qiymatni hisoblaydi.
         - __Sintaksisi:__
             ```python                                                 
               from django.db.models import Avg  
               average = Model.objects.aggregate(Avg('field_name'))
             ```                                                     
     4. __Min:__                                                                   
         - __Tavsifi:__ Berilgan maydon bo'yicha eng kichik qiymatni topadi.      
         - __Sintaksisi:__                                                          
             ```python                                                              
               import Min                 
               minimum = Model.objects.aggregate(Min('field_name'))                 
             ```                                                                    
     5. __Max:__                                                                                                                                           
         - __Tavsifi:__ Berilgan maydon bo'yicha eng katta qiymatni topadi.
         - __Sintaksisi:__                                                  
             ```python                                                      
               from django.db.models import Max     
               maximum = Model.objects.aggregate(Max('field_name'))     
             ```                                                            

### 59.  [Django queryset](https://docs.djangoproject.com/en/5.1/ref/models/querysets/) ushbu sahifadagi ma'lumotlarni yaxshilab o'rganish kerak. Juda muhim!

### 60. `QuerySet` da `Q` obyekti nima uchun kerak ?

> `Q` obyekti `Django` da murakkab so'rovlarni yaratish uchun ishlatiladi. U quyidagi asosiy xususiyatlarga ega:

1. **Shartlarni birlashtirish:** `Q` obyekti yordamida siz bir nechta shartlarni birlashtirishingiz mumkin.
    - **Masalan:** 
   ```python
    from django.db.models import Q
    queryset = Recipe.objects.filter(Q(name='Mojito') | Q(category='Cocktail'))
    ```
   > Bu yerda name `Mojito` yoki category '`Cocktail'` bo'lgan barcha retseptlarni olish uchun so'rov yaratiladi.

2. **NOT operatori:** `Q` obyekti yordamida shartlarni inkor qilish ham mumkin:
    ```python
      queryset = Recipe.objects.filter(~Q(name='Mojito'))
    ```
   > Bu yerda name `Mojito` bo'lmagan barcha retseptlar olinadi.

3. **Murakkab shartlar:** Siz `Q` obyekti yordamida murakkab shartlarni yaratishingiz mumkin:
    ```python
     queryset = Recipe.objects.filter(Q(name='Mojito') & ~Q(category='Non-Alcoholic'))
   ```
   > Bu yerda name `Mojito` bo'lgan va category `Non-Alcoholic` bo'lmagan retseptlar olinadi.

### 61. `<a href="{% url 'recipes:recipe_url' recipe.id %}"> View recipe detail</a>` ushbu kodening sintasksini tushuntiring 
> Bu sintaksis `Django` shablonida `URL` manzilini yaratish uchun ishlatiladi. Keling, uni qismlarga bo'lib tushuntiraman.
- `<a href="...">`: Bu HTML da havola (link) yaratish uchun ishlatiladi. `href` atributi havolaning manzilini belgilaydi.
- `{% url 'recipes:recipe_url' recipe.id %}`: Bu Django shablon tilida URL yaratish uchun ishlatiladigan maxsus sintaksis.
    - `{% url ... %}:` Django shablonida `URL` yaratish uchun ishlatiladigan tegi.
    - `'recipes:recipe_url':` Bu yerda recipes - ilova nomi (app name), `recipe_url` esa `URL` yo'li nomi (URL pattern name). Bu nomlar `urls.py` faylida belgilangan bo'lishi kerak.
    - `recipe.id`: Bu recipe obyekti uchun `ID` ni olishni anglatadi. Bu `ID` `URL` manziliga qo'shiladi, shunda havola bosilganda to'g'ri retsept tafsilotlariga o'tadi.

### 62. `{% url 'recipes:recipe_url'  %}` orqli bir nechta parametrarni yuborish
> `Django` shablonida `URL` orqali bir nechta parametrlarni yuborish uchun siz quyidagi sintaksisni ishlatishingiz mumkin:
```python
<a href="{% url 'recipes:recipe_url' recipe.id another_param %}">View recipe detail</a>
```
> Bu yerda `another_param` - bu siz yubormoqchi bo'lgan qo'shimcha parametr. Agar siz bir nechta parametrlarni yuborayotgan bo'lsangiz, ularni `URL` yo'lida belgilangan tartibda kiritishingiz kerak. 

`Masalan`: agar sizda recipe.id va user.id kabi ikkita parametr bo'lsa, sintaksis quyidagicha bo'ladi:
```python
<a href="{% url 'recipes:recipe_url' recipe.id user.id %}">View recipe detail</a>
```
Shuningdek, `urls.py` faylida `URL` yo'lini quyidagicha belgilashingiz kerak:

```python
path('recipe/<int:recipe_id>/<int:user_id>/', views.recipe_detail, name='recipe_url'),
```
> Bu yerda `<int:recipe_id>` va `<int:user_id>` - bu `URL` orqali qabul qilinadigan parametrlar. `Django` avtomatik ravishda bu parametrlarni `recipe_detail` funksiyasiga uzatadi.

### 63. `Meta class` deb nimaga aytiladi?

> `Meta class` `Django` da modelning ichida joylashgan maxsus klassdir. U modelga oid qo'shimcha ma'lumotlarni va konfiguratsiyalarni saqlaydi. `Meta` `class` yordamida modelning xulq-atvorini va ko'rsatmalarini belgilash mumkin. 

- `Meta` so'zi `metadata` dan kelib chiqadi, bu esa `ma'lumotlar haqida ma'lumot` degan ma'noni anglatadi.

- `Meta` class modelga oid qo'shimcha ma'lumotlarni (masalan, `tartib`, `nomlar`, va boshqalar) saqlaydi, shuning uchun u `meta` deb ataladi.

`Misol`:

```python
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Kategoriyalar'
        verbose_name_plural = 'Kategoriyalar'
```

> Bu misolda, `Meta` class `Category` modelining xulq-atvorini belgilaydi, masalan, ma'lumotlar qanday tartibda ko'rsatilishi va `admin` panelida qanday nomlar ko'rsatilishi.

1. `ordering = ['name']`
- **Ma'nosi:** Bu parametr modeldan olingan ma'lumotlar qanday tartibda ko'rsatilishini belgilaydi.
- **Tushuntirish:** `['name']` deb belgilangan bo'lsa, ma'lumotlar `name` maydoni bo'yicha `ascending` (o'suvchi) tartibda ko'rsatiladi. Ya'ni, `name` maydonidagi qiymatlar `A` dan `Z` gacha tartiblanadi.

2. `verbose_name = 'Kategoriyalar'`
    - **Ma'nosi:** Bu parametr modelning bitta nusxasi uchun ko'rsatiladigan inson o'qishi mumkin bo'lgan nomni belgilaydi.
    - **Tushuntirish:** Admin panelida yoki boshqa joylarda bitta kategoriya ko'rsatilganda, u "Kategoriyalar" deb nomlanadi. Bu foydalanuvchilarga ma'lumotni tushunishda yordam beradi.

3. `verbose_name_plural = 'Kategoriyalar'`
    - **Ma'nosi:** Bu parametr modelning ko'p nusxasi uchun ko'rsatiladigan inson o'qishi mumkin bo'lgan nomni belgilaydi.
    - **Tushuntirish:** `Admin` panelida yoki boshqa joylarda ko'p kategoriya ko'rsatilganda, u `Kategoriyalar` deb nomlanadi. Bu ko'p ma'lumotlarni ko'rsatishda foydalanuvchilarga qulaylik yaratadi.
   
### 64. `Class-Based Views`  nima va nima uchun kerak batafsil tushuntirib bering.

> `Class-Based Views`(Sinfga asoslangan ko'rinishlar ) Django web frameworkida ishlatiladigan `views` turidir. Ular F`unction-Based Views`(funktsiyalarga asoslangan ko'rinishlar) ga nisbatan bir qator afzalliklarga ega. 

- `Class-Based Views` - Django'da ko'rinishlarni yaratish uchun `class` dan foydalanishdir. Har bir `class` `views` ning xususiyatlarini va metodlarini o'z ichiga oladi. 
- Ular ko'pincha `Django` da oldindan belgilangan `class` dan (masalan, `ListView`, `DetailView`) foydalanadi, bu esa kodni qayta ishlatishni va tuzilishini osonlashtiradi.

`Nima uchun kerak?`

1. **Qayta ishlatish:** `class` ga asoslangan `views`  kodni qayta ishlatishni osonlashtiradi. Siz bir marta `class` ni yaratib, uni bir nechta joylarda ishlatishingiz mumkin.
2. **Kengaytirilish:** `class` lar yordamida siz o'z `views` ingizni osonlik bilan kengaytirishingiz va mavjud funksiyalarni o'zgartirishingiz mumkin.
3. **Tashkiliy tuzilma:** `class` ga asoslangan `views` kodni yanada tartibli va tushunarli qiladi, bu esa loyihani boshqarishni osonlashtiradi.
4. **Oson foydalanish:** `Django` da oldindan belgilangan `class` yordamida `views` tezda yaratish mumkin, bu esa dasturchilar uchun vaqtni tejaydi.

Misol tariqasida `ListViews` dan qanday foydalanishni ko'rib chiqamiz.

**Misol 1:** Oddiy `ListView`
1. **Model yaratish:**
    ```python
    from django.db import models
    
    class Recipe(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
    
        def __str__(self):
            return self.name
    ```
2. `ListView` yaratish:

    ```python
    from django.views.generic import ListView
    from .models import Recipe
    
    class RecipeListView(ListView):
        model = Recipe
        template_name = 'recipes/recipe_list.html'  # HTML shablon
        context_object_name = 'recipes'  # Kontekst obyekti nomi
    ```
3. `URL` konfiguratsiyasi:

    ```python
    from django.urls import path
    from .views import RecipeListView
    
    urlpatterns = [
        path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    ]
    ```
4. `HTML` shablon `recipe_list.html`:

    ```html
    <h1>Retseptlar ro'yxati</h1>
    <ul>
        {% for recipe in recipes %}
            <li>{{ recipe.name }}: {{ recipe.description }}</li>
        {% empty %}
            <li>Hech qanday retsept topilmadi.</li>
        {% endfor %}
    </ul>
    ```
Misol 2: Filtrlangan ListView

1. **Model yaratish** (avvalgi kabi)
2. Filtrlangan `ListView` yaratish:
    ```python
    from django.views.generic import ListView
    from .models import Recipe
    
    class VegetarianRecipeListView(ListView):
        model = Recipe
        template_name = 'recipes/vegetarian_recipe_list.html'
        context_object_name = 'vegetarian_recipes'
    
        def get_queryset(self):
            return Recipe.objects.filter(is_vegetarian=True)  # Vegetarian retseptlar
    ```
3. `URL` konfiguratsiyasi:

    ```python
    from django.urls import path
    from .views import VegetarianRecipeListView
    
    urlpatterns = [
        path('vegetarian-recipes/', VegetarianRecipeListView.as_view(), name='vegetarian-recipe-list'),
    ]
    ```
4. `HTML` shablon `vegetarian_recipe_list.html`:

`Xulosa`
- **Oddiy ListView:** Barcha retseptlarni ko'rsatadi.
- **Filtrlangan ListView:** Faqat vegetarian retseptlarni ko'rsatadi.

### 65. `Class-Based Views` da foydalanganigizda `context_object_name` nima bo'ladi.

> Agar siz Django'da `view` da  `context_object_name` berilmasa, `Django` avtomatik ravishda `object_list` o'zgaruvchisini standart nom sifatida ishlatadi.

**Bu shuni anglatadiki:**
- `context_object_name` berilmasa: `Django` `object_list` o'zgaruvchisini yaratadi va bu o'zgaruvchi shablonlarda barcha ob'ektlar ro'yxatini ifodalaydi.
- `context_object_name` berilganda: Siz o'zgaruvchining nomini o'zgartirishingiz mumkin. Masalan, agar siz `context_object_name='recipes'` deb belgilasangiz, shablonda `recipes` o'zgaruvchisini ishlatishingiz kerak bo'ladi.

### 66. `Class-based Views` da `dynamic` filtirlash.

> `Dinamik filtrlash` - bu foydalanuvchilarga ma'lum shartlarga asoslangan holda ma'lumotlarni ko'rish imkonini beruvchi jarayon. `Django` da bu jarayonni amalga oshirish uchun `get_queryset` metodini o'zgartirish mumkin. Bu metod, ma'lumotlar bazasidan qaysi ma'lumotlarni olish kerakligini belgilaydi.

`Qanday ishlaydi:`
1. `get_queryset` metodini o'zgartirish:
    - Siz `get_queryset` metodini o'zgartirib, foydalanuvchi tomonidan kiritilgan filtrlash shartlariga asoslangan holda ma'lumotlarni olish imkonini berasiz.
2. **Filtrlash misoli:**
    ```python
    def get_queryset(self):
        category_name = self.request.GET.get('category')
        return Recipe.objects.filter(category__name__iexact=category_name)
    ```
   Yuqoridagi kodda, `category_name` o'zgaruvchisi foydalanuvchidan olingan kategoriya nomini saqlaydi va `Recipe` modelidan faqat ushbu kategoriya bilan bog'liq retseptlarni qaytaradi.

### 67. `Class-based-views` da foydaluchi tomonidan yuborilgan ma'lumotlarga qanday kiriladi.

> `Django` da foydalanuvchi tomonidan yuborilgan ma'lumotlarga kirish uchun `self.request` ob'ektidan foydalanasiz. Bu ob'ekt `HTTP` so'rovini ifodalaydi va foydalanuvchi yuborgan ma'lumotlarni olish imkonini beradi.

1. `GET` Ma'lumotlari
   Agar foydalanuvchi ma'lumotlarni `URL` orqali yuborsa (masalan, `forma` orqali), siz `GET` parametrlarini quyidagi tarzda olishingiz mumkin
   ```python
    def get(self, request, *args, **kwargs):
        category_name = request.GET.get('category')
        # Boshqa kodlar...
    ```
2. `POST` Ma'lumotlari
    Agar foydalanuvchi ma'lumotlarni `forma` orqali yuborsa (masalan, `POST` so'rovi), siz `POST` parametrlarini quyidagi tarzda olishingiz mumkin:

    ```python
    def post(self, request, *args, **kwargs):
        recipe_name = request.POST.get('recipe_name')
        # Boshqa kodlar...
    ```

### 68. Ushbu kode `terminal` da qanday natija chiqaradi?

```python
def get(self, request, *args, **kwargs):
     print(vars(request))
```
`Terminal` da quydagicha bo'ladi:

```python
{
    'method': 'POST',
    'GET': <QueryDict: {}>,
    'POST': <QueryDict: {'name': ['John Doe']}>,
    'COOKIES': {'sessionid': 'abc123'},
    'META': {
        'HTTP_USER_AGENT': 'Mozilla/5.0',
        'REMOTE_ADDR': '192.168.1.1',
        ...
    },
    'FILES': <MultiValueDict: {}>,
    'path': '/my-view/',
    'user': <User: John Doe>
}
```
- `method:` So'rov usuli (masalan, `GET`, `POST`).
- `GET`: `URL` orqali yuborilgan `GET` parametrlarini o'z ichiga oladi.
- `POST`: Forma orqali yuborilgan `POST` parametrlarini o'z ichiga oladi.
- `COOKIES`: Foydalanuvchining brauzerida saqlangan `cookie` fayllarini o'z ichiga oladi.
- `META`: `HTTP` so'rovining meta ma'lumotlarini o'z ichiga oladi.
- `FILES`: Foydalanuvchi tomonidan yuklangan fayllarni o'z ichiga oladi.
- `path`: So'rov qilingan `URL` yo'lini o'z ichiga oladi.
- `user`: Foydalanuvchi `autentifikatsiya` qilingan bo'lsa, foydalanuvchi ob'ektini qaytaradi.

### 69. Belgilanmagan nomdan foydalanib `URL` manzilini o'zgartirishga urinsangiz nima bo'ladi?
> Agar siz `Django` da aniqlanmagan nomdan foydalanib `URL` ni teskari aylantirishga harakat qilsangiz, `NoReverseMatch` istisnosi yuzaga keladi. Bu xato `Django` siz bergan nomga mos keladigan `URL` shablonini topa olmasligini bildiradi.

- Teskari aylantirmoqchi bo'lgan `URL` nomi `urls.py` faylida to'g'ri aniqlanganligiga ishonch hosil qiling.
- `reverse()` funksiyasini yoki `{% url %}` shablon tegi yordamida to'g'ri nomdan foydalanayotganingizni tekshiring.

### 70. `Django` `form` lariga foydalnuvchilar tamonida ma'lumot kiritish uchun qanday ishlarni amalga oshirish kerak.

> `Django` shakllari va foydalanuvchi kiritishlarini amalga oshirish jarayoni quyidagi bosqichlardan iborat:

1. **Modelni yaratish**
    > Avval, ma'lumotlar bazasida saqlanadigan ma'lumotlar uchun `model` yarating. Masalan, `Category` modeli:
    
    `models.py`:
    ```python
    from django.db import models
    
    class Category(models.Model):
        name = models.CharField(max_length=100)
        date_added = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return self.name
    ```
2. **Formani aniqlash**

    > Shaklni yaratish uchun `forms.py` faylida `ModelForm` sinfini aniqlang:
    
    `forms.py`:
    ```python
    from django import forms
    from .models import Category
    
    class CategoryForm(forms.ModelForm):
        class Meta:
            model = Category
            fields = ['name']
            labels = {'name': 'Category Name'}
    ```
3. `View` yaratish

    > Foydalanuvchi kiritgan ma'lumotlarni qabul qilish va shaklni ko'rsatish uchun view yarating:
    
    `views.py`:
    ```python
    from django.shortcuts import render, redirect
    from .forms import CategoryForm
    
    def add_category(request):
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()  # Ma'lumotlarni saqlash
                return redirect('add_category_url')  # Yana shaklni ko'rsatish
        else:
            form = CategoryForm()
        return render(request, 'add_category.html', {'form': form})
    ```

4. `HTML` shablonini yaratish

    > Shaklni ko'rsatish uchun `HTML` shablonini yarating `add_category.html`:
    
    `add_category.html`:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Add Category</title>
    </head>
    <body>
        <h1>Add a New Category</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}  <!-- Shaklni ko'rsatish -->
            <button type="submit">Add Category</button>
        </form>
    </body>
    </html>
    ```

5. `URL` ni belgilash

    > `urls.py` faylida `URL` ni qo'shing:
    
    `urls.py`
    ```python
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('add-category/', views.add_category, name='add_category_url'),
    ]
    ```
6. **Foydalanuvchi kiritishlari**
    
    `Google Chrome`:
    > Foydalanuvchi [http://localhost:8000/add-category/](http://localhost:8000/add-category/) `URL` manziliga o'tib, shaklni to'ldirishi va `Add Category` tugmasini bosishi mumkin. Agar shakl to'g'ri to'ldirilsa, ma'lumotlar bazasiga saqlanadi. Bu jarayonlar orqali `Django` shakllari va foydalanuvchi kiritishlari amalga oshiriladi. 

### 71. Ushbu forms.py ichidagi kode parchasini tushuntirib bering:

```python
from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': 'Category Name'}
```
Keling, berilgan kodni batafsil tushuntirib beraman:

1. **Importlar**
    ```python
    from django import forms
    from .models import Category
    ```
   - `from django import forms`: Django dan `forms` modulini import qiladi. Bu modul shakllarni yaratish va boshqarish uchun kerak.
   - `from .models import Category`: Hozirgi ilova ichidagi `models.py` faylidan `Category` modelini import qiladi. Bu model foydalanuvchi kiritgan ma'lumotlarni saqlash uchun ishlatiladi.
2. **Formani aniqlash**
   - `class CategoryForm(forms.ModelForm)`: `CategoryForm` nomli yangi class yaratilmoqda, bu `forms.ModelForm` `class` idan meros oladi. `ModelForm` sinfi `Django` da ma'lumotlar bazasidagi modelga asoslangan shakllarni yaratish uchun qulayliklar taqdim etadi.

3. **Meta sinfi**

    ```python
    class Meta:
        model = Category
        fields = ['name']
    ```
   - `class Meta`: Bu ichki `class` bo'lib, shaklga oid qo'shimcha ma'lumotlarni belgilash uchun ishlatiladi.
   - `model = Category`: Bu yerda shakl `Category` modeliga bog'langanligini ko'rsatadi. Shakl foydalanuvchi kiritgan ma'lumotlarni ushbu modelga asoslangan ma'lumotlar bazasiga saqlaydi.
   - `fields = ['name']`: Bu ro'yxat shaklda ko'rsatiladigan `model` maydonlarini belgilaydi. Bu holatda, faqat `name` maydoni shaklda ko'rsatiladi.

4. **Labels**

    `labels = {'name': 'Category Name'}`
    
    - `labels = {'name': 'Category Name'}`: Bu yerda shakldagi `name` maydoni uchun ko'rsatiladigan `label` (nom) belgilangan. Foydalanuvchi shaklni to'ldirayotganda, `name` maydoni yonida `Category Name` deb ko'rsatiladi. Bu foydalanuvchilarga maydonning maqsadini tushunishga yordam beradi.

**Umumiy tushuncha**

> Ushbu kod parchasida `CategoryForm` `class Category` modeliga asoslangan shaklni yaratadi. Foydalanuvchilar faqat `name` maydonini to'ldirishlari kerak va bu maydon uchun `Category Name` deb nomlangan `label` ko'rsatiladi. Bu shakl foydalanuvchi kiritgan ma'lumotlarni to'g'ridan-to'g'ri `Category` modeliga saqlash imkonini beradi.

### 72. Quyida `views.py` fayli ichida keltirilgan kode parchasini tushuntiring.

`views.py`:

```python
 from .forms import CategoryForm
 
 def add_category(request):
     if request.method == 'POST':
         form = CategoryForm(request.POST)
         if form.is_valid():
             form.save()  # Ma'lumotlarni saqlash
             return redirect('add_category_url')  # Yana shaklni ko'rsatish
     else:
         form = CategoryForm()
     return render(request, 'add_category.html', {'form': form})``` ushbu kode parchasini batafsil tushuntirib ber
```

**Keling, berilgan kod parchasini batafsil tushuntirib beraman:**

1. **Importlar**

    ```python
    from django.shortcuts import render, redirect
    from .forms import CategoryForm
    ```
    - `from django.shortcuts import render`, `redirect`: Django dan `render` va `redirect` funksiyalarini import qiladi.
   
        - `render`: Bu funksiya `HTML` shablonini `render` qilish va foydalanuvchiga ko'rsatish uchun ishlatiladi.
        - `redirect`: Bu funksiya foydalanuvchini boshqa `URL` manziliga yo'naltirish uchun ishlatiladi.
    
    - `from .forms import CategoryForm`: Hozirgi ilova ichidagi `forms.py` faylidan `CategoryForm` class ini import qiladi. Bu shakl foydalanuvchi kiritgan ma'lumotlarni qabul qilish uchun ishlatiladi.

2. `View` funksiyasi
 
    `def add_category(request):`

    - `def add_category(request)`: `add_category` nomli `view funksiyasi` yaratilmoqda. Bu funksiya foydalanuvchidan kelgan so'rovni `request` qabul qiladi.
3. `POST` so'rovi
    
    ```python
    if request.method == 'POST':
        form = CategoryForm(request.POST)
    ```    
   - `if request.method == 'POST'`: Agar foydalanuvchi shaklni to'ldirib yuborgan bo'lsa, bu yerda `POST` so'rovi keladi.
   - `form = CategoryForm(request.POST)`: Foydalanuvchi kiritgan ma'lumotlar `request.POST` orqali olinadi va `CategoryForm` shakliga uzatiladi. Bu shakl foydalanuvchi kiritgan ma'lumotlarni tekshirish va saqlash uchun ishlatiladi.
4. **Shaklni tekshirish**

    ```python
    if form.is_valid():
        form.save()  # Ma'lumotlarni saqlash
        return redirect('add_category')  # Yana shaklni ko'rsatish
    ```
  - `if form.is_valid()`: Agar shakl to'g'ri to'ldirilgan bo'lsa (ya'ni, barcha talablar bajarilgan bo'lsa), bu kod bajariladi. 
  - `form.save()`: Foydalanuvchi kiritgan ma'lumotlar ma'lumotlar bazasiga saqlanadi.
  - `return redirect('add_category_url')`: Foydalanuvchini `add_category_url` `URL` manziliga yo'naltiradi. Bu, foydalanuvchiga yangi kategoriya qo'shilgandan so'ng, yana shaklni ko'rsatish imkonini beradi.

5. `GET` so'rovi

    ```python
    else:
        form = CategoryForm()
    ```
   
    - `else`: Agar foydalanuvchi shaklni to'ldirmagan bo'lsa (ya'ni, `GET` so'rovi), bu kod bajariladi.
    - `form = CategoryForm()`: Yangi bo'sh shakl yaratiladi, bu foydalanuvchiga ko'rsatiladi.

6. Shaklni `render` qilish

    ```python
    return render(request, 'add_category.html', {'form': form})
    ```
   
    - `return render(request, 'add_category.html', {'form': form})`: `add_category.html` shablonini `render` qiladi va form o'zgaruvchisini kontekst sifatida uzatadi. Bu shablonda shakl ko'rsatiladi.

**Umumiy tushuncha**

> Ushbu kod parchasida `add_category` nomli `view` funksiyasi foydalanuvchidan kategoriya qo'shish uchun shaklni qabul qiladi. Agar foydalanuvchi shaklni to'ldirib yuborsa, ma'lumotlar saqlanadi va foydalanuvchi yana shaklni ko'rishi uchun yo'naltiriladi. Agar shakl to'ldirilmagan bo'lsa, bo'sh shakl ko'rsatiladi.









































































































