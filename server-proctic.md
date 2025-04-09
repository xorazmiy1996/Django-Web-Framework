### 1. virtual serverdagi barcha foydalanuvchilarni ko'rish:
- /etc/passwd faylini ko'rish
    ```bash
    cat /etc/passwd
    ```
   > Bu buyruq foydalanuvchilar va ularning ma'lumotlari (masalan, `UID`, `GID` va `uy` papkasi) joylashgan.
   
   > `/etc` - bu `Linux` va `Unix` kabi operatsion tizimlarida muhim konfiguratsiya fayllarini saqlash uchun mo'ljallangan katalog. `etc` so'zining qisqartmasi `et cetera` dan kelib chiqadi, lekin bu yerda u `configuration` (konfiguratsiya) ma'nosida ishlatiladi.

`Misol`:

Fayldagi bir qator quyidagi ko'rinishda bo'lishi mumkin:

```ini
username:x:1001:1001::/home/username:/bin/bash
```
Bu yerda:

- username — foydalanuvchi nomi
- x — parol o'rnida joylashgan belgi
- 1001 — UID
- 1001 — GID
- :: — qisqacha ma'lumot (bo'sh)
- /home/username — uy papkasi
- /bin/bash — shell


### 2. `cat` buyrug'i nimalarga ishlatilinadi?

1. **Faylni ko'rsatish:** `cat` yordamida faylning mazmunini terminaldan ko'rsatishingiz mumkin. Masalan, faylni o'qish uchun:
    ```bash
    cat fayl_nomi.txt
    ```
2. **Faylni yaratish:** Agar fayl hali mavjud bo'lmasa, `cat` yordamida yangi fayl yaratish va uning mazmunini kiritish mumkin:
    ```bash
    cat > yangi_fayl.txt
    ```
    > Bu komandani bajarishdan so'ng, terminalda kiritganlaringiz faylga yoziladi. Faylni saqlash uchun `Ctrl + D` tugmasini bosishingiz kerak.
3. **Faylni birlashtirish:** Bir nechta faylni bitta faylga birlashtirish uchun catdan foydalanishingiz mumkin. Misol uchun:
    ```bash
    cat fayl1.txt fayl2.txt > yangi_fayl.txt
    ```
4. **Faylga qo'shish:** Exist faylga yangi mazmun qo'shish uchun `>>` operatoridan foydalanishingiz mumkin:
    ```bash
    cat >> mavjud_fayl.txt
    ```
### 3. `server` dagi `fayl` larni `edit` qilish.

> `Server` dagi `fayl` larni 2 xil usulda `nano` yoki `vim` orqli tahrirlash mumkin.


`Nano`:

```bash
    nano fayl_nomi.txt
``` 
> Fayl ochilgandan so'ng, tahrirlarni olib boring. O'chirish uchun `Ctrl + K`, faylni saqlash va chiqish uchun `Ctrl + O` (saqlash), so'ng Enter tugmasini, keyin `Ctrl + X` (chiqish) tugmalarini bosing.

`Vi/Vim`:
```bash
    vi fayl_nomi.txt
```
- O'zgarishlarni qilish uchun `i` tugmasini bosing (Insert modiga o'tasiz).
- O'zgarishlarni yakunlash uchun `Esc` tugmasini bosing.
- Faylni saqlash uchun `:w`, chiqish uchun `:q`, va saqlash va chiqish uchun `:wq` yoki `:x` yozing.


### 4. Tizimdagi barcha guruhlarni ko'rish:

```bash
    cat /etc/group
```


`cat /etc/group` buyruqni bajarganingizda chiqadigan natija quyidagi kabi bo'lishi mumkin:

```ini
guruh_nomi:x:GID:foydalanuvchi1,foydalanuvchi2,foydalanuvchi3
```
Qismlarni keltirib chiqarish:

1. `Guruh` nomi (guruh_nomi): Guruhning nomi.
2. `Parol` (x): Guruhlar uchun parol o'rniga x belgi bor, bu tizimda parolning saqlanmaganligini ko'rsatadi (odatda guruhlar uchun parol kerak emas).
3. `GID` (Group ID): Har bir guruhning unikal identifikatsiya raqami.
4. `A'zolar` (foydalanuvchi1, foydalanuvchi2, ...): Bu guruhga kiruvchi foydalanuvchilar ro'yxati, agar bo'sh bo'lsa, guruhga hech qanday foydalanuvchi yozilmaganini bildiradi.

`Misol`:

`cat /etc/group` buyruqni bajarganingizda chiqadigan natija quyidagi kabi bo'lishi mumkin:
```ini
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
sudo:x:27:foydalanuvchi
www-data:x:33:
```
1. `root` — Superfoydalanuvchi, tizimdagi barcha operatsiyalarni bajarishga ruxsatga ega.
2. `sudo` — Agar bu guruhda foydalanuvchi bo'lsa, unga administrator huquqlari beriladi. Masalan, yuqoridagi misolda foydalanuvchi nomli foydalanuvchi sudo guruhiga kiritilgan.
3. `A'zolar` — Ma'lum guruhlarga kiruvchi foydalanuvchilar : orqali ajratilgan bo'ladi. Agar guruhda foydalanuvchilar bo'lmasa, bu bo'sh qoldiriladi.

### 5. Foydalanuvchini `sudo` guruhiga qo'shish:

> Avval `terminal` ga kiring va tizim administrator `(root)` huquqlariga ega bo'lishingiz kerak. Agar siz tizimda boshqa foydalanuvchi sifatida kirgan bo'lsangiz, `sudo` yordamida administrator huquqlariga ega bo'lishingiz mumkin.

Foydalanuvchini sudo guruhiga qo'shish

```bash
    sudo usermod -aG sudo foydalanuvchi_nomi
```

`sudo usermod -aG sudo foydalanuvchi_nomi` buyrug'ini sintaksis tahlil qilaylik:

1. **sudo**
   - **Tavsifi:** `sudo` (SuperUser DO) — bu buyruqni administrator (root) huquqlari bilan bajarish uchun ishlatiladi. 
2. **usermod**
   - **Tavsifi:** `usermod` — bu `Linux` tizimida foydalanuvchini o'zgartirish uchun ishlatiladigan buyruq. Bu buyruq yordamida foydalanuvchining ruxsatlarini, guruhini, foydalanuvchi nomini va boshqa parametrlarini o'zgartirishingiz mumkin.
3. `-aG` (flaglar)
   - `-a` ("append")
     - Foydalanuvchini yangi guruhga qoʻshadi, avvalgi guruhlaridan chiqarmaydi.
     - Eslatma: Agar -a ishlatilmasa, foydalanuvchi barcha oldingi guruhlardan chiqariladi.
   - `-G` ("groups"):
     - Foydalanuvchini koʻrsatilgan `guruh`(lar)ga biriktirish uchun.

4. `sudo` (argument)
   - Foydalanuvchi qoʻshiladigan guruh nomi.

> Foydalanuvchi `sudo` guruhiga qo'shilganidan so'ng, foydalanuvchi shartlarni yangilash uchun tizimdan chiqish va qayta kirish kerak bo'lishi mumkin. Shunda foizlar yangi o'zgarishlarga ega bo'ladi.

### 6. Foydalanuvchini `sudo` guruhidan chiqaring.

- `deluser` buyrug'i (Debian/Ubuntu):
    ```bash
    sudo deluser <foydalanuvchi_nomi> sudo
    ```












































































































































































































































