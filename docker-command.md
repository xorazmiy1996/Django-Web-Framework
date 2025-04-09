### 1.  Asosiy Buyruqlar.

----
1. **Loyihani Ishga Tushirish**
    ```bash
    docker compose up -d  # Orqa fonda ishga tushirish
    ```
      `docker compose up -d` buyrug'i orqa fonda (detached mode) konteynerlarni ishga tushirishni anglatadi. Bu quyidagilarni bildiradi:
  - > Konteynerlar terminalga bogʻlanmaydi. Terminalni yopishingiz mumkin, lekin konteynerlar ishlashda davom etadi.  
  - > Siz terminalda boshqa buyruqlarni kiritishingiz mumkin (konteynerlar ishlaganda).

2.  **Agar `-d` flag ishlatilmasa**
   - Terminalni yopish konteynerlarni toʻxtatadi.
   - Barcha loglar va chiqishlar (stdout/stderr) terminalda koʻrinadi.
   - Konteynerlar `foreground` modeda ishga tushadi (terminalga bogʻlanadi).

      `Misol`:

     ```bash
      docker compose up -d  # Konteynerlar orqa fonda ishga tushadi
      docker compose up     # Konteynerlar terminalga bogʻlanadi (loglar koʻrinadi)
     ```
3. **Orqa fonda ishlaganda nima qilish kerak?**  
- Konteynerlarni koʻrish:
  ```bash
  docker compose ps
  ```
- Loglarni koʻrish:
  ```bash
  docker compose logs  # Barcha loglar
  docker compose logs -f web  # "web" servisining real vaqt loglari
  ```
- Konteynerga kirish:
  ```bash
  docker compose exec web bash  # "web" konteyneriga kirish
  ```
- Konteynerlarni toʻxtatish:
  ```bash
  docker compose down
  ```
4. **Qachon `-d` flag ishlatiladi?**
- Loyihani **serverda** doimiy ishlashi uchun.
- Terminalni boshqarishni davom ettirish uchun.
- Loyihani **test qilgandan soʻng** ishga tushirishda.

  > Tasavvur qiling, sizda `web` (nginx) va `db` (PostgreSQL) servislari bor.
  `docker compose up -d` buyrugʻi bilan ikkala konteyner ham orqa fonda ishga tushadi.
  Brauzer orqali [http://localhost:80](http://localhost:80) manziliga kirib, web sahifasini koʻrishingiz mumkin,
  terminal esa bepul boʻladi (yangi buyruqlar kiritish mumkin).

2. **Loyihani Toʻxtatish va Oʻchirish**
    ```bash
    docker compose down  # Konteyner, tarmoq va (agar belgilangan boʻlsa) volumeni oʻchirish
    docker compose down --volumes  # Volumelarni ham oʻchirish
    ```
3.  **Imagelarni Qayta Yaratish (Dockerfile asosida)**

    ```bash
    docker compose build  # Barcha servislarni qayta yaratish
    docker compose build web  # Faqat "web" servisini qayta yaratish
    ```
4. **Konteynerlarni Koʻrish**
    ```bash
    docker compose ps  # Faqat ishlayotgan konteynerlarni koʻrsatadi
    docker compose ps -a  # Barcha konteynerlarni koʻrsatadi (toʻxtatilganlar ham)
    ```
5. **Loglarni Koʻrish**
    ```bash
    docker compose logs  # Barcha servislarning loglari
    docker compose logs web  # Faqat "web" servisi loglari
    docker compose logs -f  # Real vaqtda loglarni kuzatish
    ```
6.  **Servisga Kirish (exec)**

    ```bash
    docker compose exec web sh  # "web" konteyneriga shell orqali kirish
    ```











































































































































































































