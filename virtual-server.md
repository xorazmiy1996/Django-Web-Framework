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

### 4. `root`(administrator) dan to'g'ri user (foydalanuvchi) hisobi ga o'tish.

1.  `root` dan `user` hisobiga o'tish
    ```shell
      su - muhammad
    ```
    `Eslatma`:
    - `su` - (tire bilan) foydalanuvchi muhitini to'liq yuklaydi
    - `su` (tiresiz) esa faqat hisobga o'tadi, muhitni yangilamaydi

2. **Foydalanuvchi hisobini tekshirish**
















































































































































































