### 1. Nginx - Bu Nima?

> `Nginx` (talaffuzi: "engine-x") - bu ochiq kodli, yuqori tezlikdagi `veb-server` va `reverse proxy` dasturi bo'lib,
> internetdagi eng yirik saytlarning 40% dan ortig'ida ishlatiladi. Uni "veb-serverlar shohi" deb atash mumkin.

1. **Asosiy Ta'rif:**
    - Statik kontentni yetkazuvchi (`HTML`, `CSS`, `JS`, `rasmlar`)
    - Dinamik ilovalar uchun proxy (`Django`, `Flask`, `Node.js`)
    - Xavfsizlik filtri
    - Yuk balanslagichi
2. **Qanday Ishlaydi?**

   **Oddiy misol:**

```
Foydalanuvchi brauzeri
  ↓ HTTP so'rov
Nginx (tezroq javob beradi)
  ├── Agar statik fayl → Darrov yuboradi
  └── Agar dinamik so'rov → Gunicorn/Django ga yo'naltiradi
```
3. **Asosiy Komponentlar:**

| **Modul**       | **Vazifasi**            | **Misol**                |
|-----------------|-------------------------|--------------------------|
| `HTTP Core`     | Asosiy veb-protokol     | `listen 80;`             |
| `Reverse Proxy` | Ilovalarga yo'naltirish | `proxy_pass http://app;` |
| `Load Balancer` | Yukni taqsimlash        | `upstream app_servers`   |
| `SSL/TLS`       | Shifrlangan trafik      | `ssl_certificate`        |

4. **Nima Uchun Kerak?**
- **Tezlik**: 1 soniyada 50,000+ so'rovni boshqaradi
- **Barqarorlik:** 99.9% uptime (Google, Netflix kabi kompaniyalar ishlatadi)
- **Iqtisodiyot:** 1 serverda 10.000 foydalanuvchini ushlab turishi mumkin

5. **Hayotiy Misol:**

**Tasavvur qiling, siz restoranga kirdingiz:**

- `Nginx` - bosh ofitsiant:
  - Menyuni (statik fayllar) darrov olib keladi
  - Maxsus taomlar (dinamik so'rovlar) uchun oshpazga (Gunicorn) yo'naltiradi
  - Xavfli mijozlarni (hujumchilar) qaytaradi

6. **Asosiy Afzalliklar:**
   1. **`CPU/RAM` tejamkor** - 10MB dan boshlanadi
   2. **Asinxron arxitektura** - Bir process ko'p so'rovlarni boshqaradi
   3. **Moslashuvchan** - `Docker`, `Kubernetes` bilan ishlaydi

7. **Oddiy Konfiguratsiya:**

   ```ini
   # /etc/nginx/conf.d/default.conf
   server {
       listen 80;
       
       location / {
           proxy_pass http://127.0.0.1:8000; # Gunicorn manzili
       }
       
       location /static/ {
           alias /var/www/static/; # CSS/JS/rasmlar joyi
       }
   }
   ```

8. **Qiziqarli Statistikalar:**

- Netflix: Kuniga 2 milliard so'rovni Nginx orqali boshqaradi
- WordPress.com: 70% trafikni Nginx bilan optimallashtiradi
- Cloudflare: Butun infratuzilmasida Nginx ishlatadi

9. **O'rnatish (Ubuntu):**

   ```bash
   sudo apt update
   sudo apt install nginx
   sudo systemctl start nginx
   ```
**Xulosa:**
> `Nginx` - bu internetning `ko'prigi` bo'lib, barcha trafikni aqlli boshqaradi. U `Python` ilovalaringiz uchun `tashqi qalqon` vazifasini bajarib, yukni kamaytiradi va tezlikni oshiradi.






























































































