
### 1.  `Django QuerySet API` haqia nimalar bilasiz?

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

### 2. `Django QuerySet API` da filtrlar va aniq maydonlarni qidirish haqida qanday tushunchalarga egasiz?

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

### 3. Istisno `(Exclude)` Filtri haqida nima bilasiz va ishlatish bo'yicha misol keltiring:

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
### 4. Chaining (zanjirli) Filtrlar:
   > `Django` da siz bir nechta filtrlarni birlashtirib ishlatishingiz mumkin. Bu sizga yanada aniqroq natijalarni olish imkonini beradi.
   - __Masalan:__
      - `Recipe.objects.filter(category__name='soup').exclude(name__contains='chocolate').order_by('-date_added')`
      > Bu kod `soup` kategoriyasidagi retseptlarni olib, `chocolate` nomini o'z ichiga olganlarini chiqarib tashlaydi va natijalarni `date_added` sanasi bo'yicha kamayish tartibida tartiblaydi.
     
### 5. Bir nechta filtrlarni yozish uchun `Django` da qanday usullar mavjud
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

### 6. QuerySet API - Slicing QuerySets and Aggregation.
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

### 7.  [Django queryset](https://docs.djangoproject.com/en/5.1/ref/models/querysets/) ushbu sahifadagi ma'lumotlarni yaxshilab o'rganish kerak. Juda muhim!

### 8. `QuerySet` da `Q` obyekti nima uchun kerak ?

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
