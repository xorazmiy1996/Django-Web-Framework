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
   > Bu buyruqlar sizga `virtual server` da ishlashda yordam beradi. Har bir buyruqni ehtiyotkorlik bilan ishlating va
   muhim fayllarni o'zgartirishdan oldin zaxira olishni unutmang.

### 2. `virtual server` da foydalanuvchi yaratish.

**Foydalanuvchi yaratish uchun qadamlar:**

1. **Terminalga kiring:** Virtual serverga `SSH` orqali kiring. Buning uchun terminaldan foydalaning:

   ```shell
   ssh username@ip_address
   ```
2. **Yangi foydalanuvchini yaratish:**

   > `adduser` yoki `useradd` buyruqlaridan biri yordamida yangi foydalanuvchini yaratishingiz mumkin. adduser ko'proq
   qulay va o'ziga xos bo'lib, interaktiv tarzda o'zgartirish imkonini beradi.

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

   > `adduser` buyruği avtomatik ravishda foydalanuvchining parolini so'raydi. Agar useradd buyruqidan foydalangan
   bo'lsangiz, foydalanuvchining parolini belgilash uchun quyidagi buyruqni bajarishingiz kerak:

   ```shell
   sudo passwd yangi_foydalanuvchi
   ```
   > Yuqoridagi buyruqdagi `passwd` o'rniga o'zingizning yangi passwordingizn yozmang chungi bu hato, bu yerda `passwd `
   kalit so'z hisoblanadi. Bu buyruqda siz `yangi_foydalanuvchi` o'rniga `useradd` orqali yaratilgan foydalanuvchini
   kiritasiz va `enter` tugmasini bosasiz. Shundan so'ng sizdan yangi foydalanuvchi uchun password kiritishni so'raladi.


4. **Foydalanuvchini qo'shimcha guruhlarga kiritish:**

   > Agar foydalanuvchini biror guruhga kiritsangiz (masalan, `sudo` guruhiga, agar uni `administrator` qilishni
   xohlasangiz), quyidagi buyruqni bajarishingiz mumkin:

   ```shell
   sudo usermod -aG sudo yangi_foydalanuvchi
   ```
5. **Foydalanuvchini yaratish jarayonini yakunlash:**

   > Hamma narsa to'g'ri bajarilgandan so'ng, yangi foydalanuvchi serverda o'ziga xos huquqlarga ega bo'ladi. U o'z
   profiliga kirishi mumkin va belgilangan huquqlarga mos ravishda ish olib borish imkoniyatiga ega bo'ladi.

**Misol:**

Agar siz `developer` nomli foydalanuvchini yaratmoqchi bo'lsangiz, quyidagi buyruqlarni bajarishingiz mumkin:

```shell
   sudo adduser developer
   # Parolni kiritish
   sudo usermod -aG sudo developer  # Agar uni administrator qilishni xohlasangiz
```

### 3. `virtual server` ga kiradigan `root foydalanuchisi` bilan va yangi yaratilgan

`yangi_foydalanuvchi` foydalanuvchi o'rtasidagi farqlar ni tushuntirib bering.

1. `Huquqlar` va `Ruxsatlar`
    - **Root foydalanuvchisi:**
        - `Superuser` yoki `administrator` hisoblanadi.
        - Tizimning barcha resurslariga (fayllar, dasturlar, boshqa foydalanuvchi hisoblari va boshqalar) to'liq kirish
          huquqiga ega.
        - Har qanday komanda va operatsiyalarning bajarilishiga ruxsat beriladi, shu jumladan tizim sozlamalarini
          o'zgartirish, foydalanuvchilarni yaratish va o'chirish.
    - **Oddiy foydalanuvchi `yangi_foydalanuvchi`:**
        - Tizimda cheklangan huquqlarga ega.
        - Faqat o'z uy katalogidagi fayllarga kirish va o'zgartirish huquqiga ega.
        - Boshqa foydalanuvchilarning kataloglarini o'zgartira olmaydi va tizim konfigatsiyalarini o'zgartirish uchun
          `sudo` huquqlariga ega bo'lmasa, `root` buyruqlarini bajarish imkoniyatiga ega emas.

### 4. `root`(administrator) dan to'g'ri user (foydalanuvchi) hisobi ga o'tish.

1. `root` dan `user` hisobiga o'tish
   ```shell
     su - muhammad
   ```
   `Eslatma`:
    - `su` - (tire bilan) foydalanuvchi muhitini to'liq yuklaydi
        1. Yangi login shell yaratiladi
        2. Foydalanuvchining `.bashrc`, `.profile` fayllari ishga tushiriladi
        3. `HOME` papkasi yangilanadi (/home/muhammad)
        4. `PATH` o'zgaruvchisi yangilanadi
           ```shell
           root@server:~# su - muhammad
           muhammad@server:~$ echo $HOME
            # To'g'ri yangilangan
           ```
    - `su` (tiresiz) esa faqat hisobga o'tadi, muhitni yangilamaydi
        1. Faqat foydalanuvchi o'zgartiradi
        2. Oldingi foydalanuvchining muhiti saqlanib qoladi
        3. `HOME` papkasi o'zgarmaydi
        4. `.bashrc` ishga tushmaydi
           ```shell
           root@server:~# su - muhammad
           muhammad@server:~$ echo $HOME
            # To'g'ri yangilangan
           ```

        - `echo $HOME`:
            - Bu tizim o'zgaruvchisi (environment variable) bo'lib, har bir foydalanuvchi uchun:
                - Linux/Mac: `/home/foydalanuvchi_nomi` (masalan, /home/muhammad)
                - Windows (WSL): `/home/foydalanuvchi_nomi`
                - Root foydalanuvchi uchun: `/root`

2. **Foydalanuvchi hisobini tekshirish**

   ```shell
   whoami  # Hozirgi foydalanuvchi nomini ko'rsatadi
   pwd     # Joriy ish papkasini ko'rsatadi
   ```

### 5. `echo` nima?

> `echo` — bu `Linux/Mac` terminalida matn yoki o‘zgaruvchilarni ekranga chiqarish uchun ishlatiladigan asosiy buyruq.
> Uning vazifasi siz ko‘rsatgan ma’lumotni terminal oynasida ko‘rsatishdir.

1. **Asosiy ishlatilishi**

   ```shell
   echo "Salom, Dunyo!"  # Tekstni chiqaradi
   ```
   **Natija:**
   ```
   Salom, Dunyo!
   ```
2. **O‘zgaruvchilar bilan ishlash**

    ```shell
    ism="Ali"
    echo "Mening ismim $ism"  # O‘zgaruvchini qiymatini chiqaradi
    ```
   **Natija:**
    ```
    Mening ismim Ali
    ```
3. **Faylga yozish (>> yoki >)**

    ```shell
    echo "Bu yangi matn" > fayl.txt  # Faylga yozadi (eski mazumni o‘chiradi)
    echo "Qo‘shimcha matn" >> fayl.txt  # Fayl oxiriga qo‘shadi
    ```   
4. **Maxsus belgilar**

    ```shell
    echo -e "Birinci qator\nIkkinchi qator"  # \n yangi qator uchun
    ```
   **Natija:**
    ```
    Birinci qator
    Ikkinchi qator
    ```
5. **Foydali misollar**

    - **a) Fayl yaratish:**
      ```shell
      echo "#!/bin/bash" > script.sh  # Skript boshlanishi
      ```
    - **b) O‘zgaruvchilarni tekshirish:**
      ```shell
      echo $PATH  # Tizim yo‘llarini ko‘rsatadi
      ```
    - **c) Matnni boshqa buyruqqa uzatish:**
      ```shell
      echo "123" | wc -c  # Belgilar sonini hisoblaydi
      ```
6. **Qo‘shimcha variantlar**

| Variant | Misol                                     | Tavsif                                   |
|---------|-------------------------------------------|------------------------------------------|
| `-e`    | `echo -e "Tab\tqator"`                    | Maxsus belgilarni talqin qilish (\t, \n) |
| `-n`    | `echo -n "Oxirida yangi qator bo‘lmasin"` | Yangi qator qo‘shmaslik                  |

7. **Nega kerak?**

- **Skriptlarda:** Foydalanuvchiga xabarlarni ko‘rsatish
- **Tezkor tekshirish:** O‘zgaruvchilar qiymatini ko‘rish
- **Fayllar bilan ishlash:** Konfiguratsiya fayllarini yaratish
  **Misol:** Docker container ismini tekshirish:

```shell
echo "Container nomi: $CONTAINER_NAME"
```

> Agar terminalda `echo` ishlamasa (juda kam hollarda), `which echo` buyrug‘i bilan uning joylashuvini tekshiring. Bu
> buyruq har doim `Linux/Mac` tizimlarida mavjud bo‘ladi!

### 7. `ls -la`   nima uchun kerak?

> `ls -la` — bu` Linux/Mac` terminalida papka tarkibidagi barcha fayl va papkalarni detalli ko'rsatish uchun
> ishlatiladigan buyruq ya'ni catalog(papka)  ichidagi har-bir faylning huquqlarini ko'rish. Keling, uni tushunib
> olamiz:

1. **Buyruq tarkibi:**

- `ls` - papka tarkibini ko'rsatish (list)
- `-l` - uzun formatda (huquqlar, egasi, hajmi)
- `-a` - barcha fayllarni (`.bashrc` kabi yashirin fayllar ham)

2. **Chiqish natijasi misoli:**

   ```shell
   drwxr-xr-x 5 user group 4096 Jun 15 10:30 .
   drwxr-xr-x 3 root root 4096 Jun 10 09:15 ..
   -rw-r--r-- 1 user group  220 Jun 10 09:15 .bash_logout
   -rw-r--r-- 1 user group 3771 Jun 10 09:15 .bashrc
   drwx------ 2 user group 4096 Jun 12 14:20 .ssh
   -rwxr-xr-x 1 user group  120 Jun 15 10:30 script.sh
   ```

3. **Qatorlarni tushuntirish:**

   **Har bir qator 7 qismdan iborat:**

    1. **Huquqlar** (masalan, **drwxr-xr-x**):
        - `d` - papka (- oddiy fayl, l link)
        - `rwx` - egasi huquqlari (read/write/execute)
        - `r-x` - guruh huquqlari
        - `r-x` - boshqalar huquqlari
    2. **Havolalar** soni (masalan, `5`)
    3. **Egasi** (masalan, `user`)
    4. **Guruhi** (masalan, `group`)
    5. **Hajmi** (baytlarda, masalan `4096`)
    6. **O'zgartirilgan sana** (masalan, `Jun 15 10:30`)
    7. **Nomi** (masalan, `.bashrc`)

4. **Fayl huquqlari dekodi:**

| Belgilar | Tavsif             |
|----------|--------------------|
| `r`      | O'qish (read)      |
| `w`      | Yozish (write)     |
| `x`      | Bajarish (execute) |
| `-`      | Huquq yo'q         |

**Misol `-rwxr-xr--`:**
- Egasi: o'qiydi, yozadi, bajaradi `rwx`
- Guruhi: o'qiydi, bajaradi `r-x`
- Boshqalar: faqat o'qiydi `r--`

5. **Qachon ishlatiladi?**

   1. **Huquqlarni tekshirish** (Docker/MongoDB fayllari uchun)

   2. **Yashirin fayllarni ko'rish** (`.env`, `.ssh`)

   3. **Fayl egaligini aniqlash** (`root` yoki `user`?)

   4. **Xavfsizlik auditida** (g'ayritabiiy huquqlarni qidirish)

6. **Misol: Docker loyihasida tekshirish**

   ```shell
   cd ~/my-django-project
   ls -la
   ```
   **Nima ko'rasiz?**

   - `.env` fayli mavjudmi?

   - `docker-compose.yml` huquqlari to'g'rimi?

   - `media/` papkasi kimga tegishli?

> Bu buyruqni doimo ishlating — serverda nima bo'layotganini tushunish uchun asosiy vositalardan biri.

### 7. `drwxrwxr-x` ushbu huquqni tushuntirib bering:

> `drwxrwxr-x` — bu Linux fayl tizimidagi **papka huquqlarini** ifodalovchi kod. Keling, uni qismlarga ajratib tushuntiraman:

---

   1. **Birinchi belgi: Fayl turi**
      - `d` — bu **papka** (directory)  
        (Agar `-` bo'lsa — oddiy fayl, `l` bo'lsa — simvolik havola)

---

   2. **Keyingi 9 ta belgi: 3 guruhdagi huquqlar**

   Har bir 3 belgi bir guruh huquqlarini ko'rsatadi:

   #### a) **Egasi (owner) huquqlari** (`rwx`):
   - `r` (read) — papkani ochish va tarkibini ko'rish  
   - `w` (write) — papkada yangi fayl yaratish/o'chirish  
   - `x` (execute) — papkaga kirish (cd qilish)

   #### b) **Guruh (group) huquqlari** (`rwx`):
   - Aynan egasi huquqlari kabi, lekin faqat ushbu guruh a'zolari uchun

   #### c) **Boshqalar (others) huquqlari** (`r-x`):
   - `r` — tarkibni ko'rish  
   - `-` — yozish huquqi yo'q  
   - `x` — papkaga kirish

---

   ### **3. Butun strukturani vizualizatsiya:**
   ```
   d rwx rwx r-x
   │ │││ │││ │││
   │ └┬┘ └┬┘ └┬┘
   │  │   │   └─ Boshqalar (others) huquqlari
   │  │   └───── Guruh (group) huquqlari
   │  └───────── Egasi (owner) huquqlari
   └──────────── Fayl turi (papka)
   ```

---
   
   ### **4. Misol holatlar:**
   1. **Foydalanuvchi (owner)**:
      - Papkaga kirishi (`x`)  
      - Ichida yangi fayl yaratishi (`w`)  
      - `ls` qilishi (`r`)
   
   2. **Guruh a'zosi**:
      - Xuddi shu huquqlar (chunki `rwx`)
   
   3. **Boshqa har kim**:
      - Kirishi va fayllarni ko'rishi (`r-x`), lekin  
      - Yangi fayl yaratolmaydi (`w` yo'q)

---

   ### **5. Bu huquqlar qayerda ko'riladi?**
   - **Docker** loyihalarida: `chmod -R 775 papka_nomi` buyrug'i aynan shu huquqlarni beradi  
   - **Web server** papkalarida (masalan, `/var/www`)  
   - **Foydalanuvchilar** uchun umumiy ishlash papkalarida

---

   ### **6. Xavfsizlik nuqtai nazaridan:**
   - `rwxrwxr-x` (775) — ko'p hollarda xavfsiz, chunki:
   - Boshqalar faqat o'qish/kirish huquqiga ega  
   - Yozish faqat egasi va guruh a'zolariga berilgan

   - **Xavfli holat**: Agar papkada `rwxrwxrwx` (777) ko'rsa — bu hamma uchun to'liq ruxsat berilganligini anglatadi!

---

   ### **7. Huquqlarni o'zgartirish:**
   ```bash
      chmod 775 papka_nomi  # shu huquqlarni qo'llash uchun
      chown user:group papka_nomi  # egasini o'zgartirish
   ```

   Agar loyihangizda permission xatolari bo'lsa, aynan shu huquqlarni `ls -la` bilan tekshiring! 🔍

























































































































































