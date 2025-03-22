### Kod Yozish Vositasi
1. Autocompletion (Avtomatik to'ldirish)
    - `IDE` yoki kod muharriri siz yozayotgan kodni avtomatik to'ldirishni taklif etadi, bu esa harfni uchtadan kam yozmaslikka yordam beradi.
2. Code Snippets (Kod parchasi)
    - Kod parchasi - bu `funksiyalar`, `klasslar` yoki shartlar kabi tez-tez ishlatiladigan kod qismlarini tezda qo'shishga imkon beradigan qisqa kod shakllari.
    - Misol: def va class uchun tayyor shablonlar.
3. Linting (Kod tekshirish)
    - `Linter` dasturiy ta'minotdagi xatolarni, sintaksis xatolarini va keng tarqalgan muammolarni aniqlashda yordam beradi.
    - Misol: `Pylint`, `Flake8` yoki `Black`.
4. Dokumentatsiya Ko'rsatmalari
    - Foydalanayotgan funksiyalar yoki metodlar haqida tezda ma'lumot olish imkonini beruvchi vositalar.
    - IDE yordamida hover qilish orqali chiqariladi.
5. Code Navigation (Kod bilan navigatsiya qilish)
    - Kodni tezda navigatsiya qilish imkoniyatini yaratadi, masalan, `funksiya` yoki `klass` joylashuviga tezda borish.
    - IDE-lar odatda "Go to definition" yoki "Find references" imkoniyatlarini taklif etadi.
6. Debugging (Xatolarni aniqlash)
    - Kodni qadam-baqadam bajarish va xatolarni aniqlash uchun qulay vositalar.
    - Breakpoints, variable watches va avto-bug'lanish uchun grafik interfeys.
7. Unit Testing (Birlikni tekshirish)
        - Kod sifatini ta'minlash uchun test yozish imkoniyatlari, masalan unittest yoki pytest.
### `Pycharm` ning qanday turlari bor

1. **PyCharm Professional**
   - Tavsif: Bu versiya to'liq funktsional va ko'plab xavfsiz va zamonaviy xususiyatlarni o'z ichiga oladi.
   - Xususiyatlari:
      - Django, Flask kabi veb-ramkalarni qo'llab-quvvatlash.
      - Ma'lumotlar bazalari bilan ishlash uchun kuchli vositalar.
      - HTML, CSS va JavaScript kodlarini qo'llab-quvvatlash, shu jumladan templatelar bilan yaxshi integratsiya.
      - Tashqi kutubxonalar va modullar bilan ishlashda qulayliklar.
      - Test va muammolarni aniqlash vositalari.

2. **PyCharm Community**
   - Tavsif: Bu versiya ochiq manba va bepul bo'lib, asosiy xususiyatlarni taqdim etadi. Ushbu versiya oddiy Python dasturlash uchun etarli.
   - Xususiyatlari:
      - Python va JavaScript dasturlash tillarini qo'llab-quvvatlaydi.
      - Asosiy sintaksis tekshirish, kodni avtomatik to'ldirish, kodni formatlash kabi funktsiyalar.
      - Mahalliy va virtual muhitlarda ish yuritish.
      - Versiyani boshqarish tizimlari (Git, Mercurial) bilan integratsiya.

### Agar sizning `Django` templatelaringizda `autocompletion` (avtomatik to'ldirish) funksiyalari ishlamasa, iltimos, quyidagi qadamlarni tekshirib ko'ring

1. Django Plaginini Omiynlashtirish
    - Agar siz PyCharm Professional versiyasidan foydalansangiz, loyiha Django loyihasi sifatida to'g'ri aniqlanganligini tekshirib ko'ring.
    - File -> Settings `(yoki Ctrl + Alt + S)` ga o'ting, so'ng `Languages & Frameworks` bo'limini tanlang, `Django` ni tanlang va `Enable Django Support` opsiyasini yoqing.
    > `Django support` (Django qo'llab-quvvatlash) bo'limida boshqa muhim sozlamalarni ham ko'rib chiqishingiz mumkin. Quyida asosiy sozlamalar va ularning nima uchun muhim ekanligini xususiyatlari bilan bir qatorda ko'rsatib beraman:
    - **Django Support Sozlamalari**
      1. **Enable Django Support:**
            - Bu opsiyani yoqish Django loyihangizni to'g'ri aniqlashga yordam beradi va autocompletion imkoniyatlarini oshiradi.
      2. **Django Settings**
        - **Settings file:** `Django` loyihangizning `settings.py` faylini to'g'ri ko'rsatganingizga ishonch hosil qiling. Bu `PyCharmga` sizning loyiha parametrlaringizni tushunishga yordam beradi.
        - **Templates directory:** Templateni joylashgan joyni ko'rsatish ham foydali. Bu PyCharmga sizning shablonlaringizni to'g'ri tanib olishiga yordam beradi.
      3. **URL Patterns**
        - URL routing bilan bog'liq shablonlar va manzillarni keltirish uchun urls.py faylingizni kiritish. Bu sizning Django loyihangizda URL manzillarini to'g'ri yozishda yordam beradi.
      4. **Static files:**
        - Agar siz statik fayllarni (CSS, JavaScript, rasm) qo'llangan bo'lsangiz, ularni ham to'g'ri yo'lga ko'rsatishingiz mumkin.
      5. **Database**
        - Agar sizning loyihangizda ma'lumotlar bazasi bilan bog'liq bo'lsa, db fayllarini va boshqa parametrlarni ham ko'rsatishingiz kerak.

2.  Caching va PyCharmning Ishini Yangilash
    - Ba'zan IDE caching muammolari tufayli autocompletion ishlamasligi mumkin. File -> Invalidate Caches / Restart ga o'ting va keshni tozalang.
    - Keyin, yangi va toza muhitda ishga tushirish uchun IDE'ni qayta ishga tushiring.

3. Yordamchi Tizimlar o'rnatilganligini Tekshirish
    - PyCharmning yordamchi plaginlari ham bo'lishi mumkin, masalan, Django Template plaginini o'rnatilganligini tekshirib ko'ring.
    - `File -> Settings -> Plugins` ga o'ting va Django Template ni qidirib ko'ring.




















