
### 116. FontAwesome nima va nima uchun kerka.

> `FontAwesome` — bu veb loyihalaringizda ishlatishingiz mumkin bo'lgan chiroyli ikonlar to'plami. Oddiy tugmalar o'rniga, ushbu ikonlarni qo'shib, ilovangizni yanada jozibador va foydalanuvchilar uchun qulayroq qilishingiz mumkin.


### 117. `Django` loyihasiga `FontAwesome` ni o'rnatish ketma-ketligi. 

1. **Terminalda quydagi kutubxonani o'rnating:**

    `pip install fontawesomefree`


2. `settings.py` faylini tahrirlash

    ```python
    INSTALLED_APPS = [
         ...
         'fontawesomefree',
         ...
     ]
    ```
3. `base.html` shabloniga ushbu kode ni qo'shing:
    
    ```html
    <head>
       <!-- Our project just needs Font Awesome Free's Solid and Brand files -->
       <!-- Link tags cause URI malformed error  -->
       <link href="{% static 'fontawesomefree/css/fontawesome.css' %}" rel="stylesheet" type="text/css">
       <link href="{% static 'fontawesomefree/css/brands.css' %}" rel="stylesheet" type="text/css">
       <link href="{% static 'fontawesomefree/css/solid.css' %}" rel="stylesheet" type="text/css">
    </head>
       ...
    ```  