### 1.Django Loyihasini Productionga Tayyorlash: To'liq Ketma-Ketlik



---


1. Loyihani Serverga Yuklash

   ```bash
   git clone https://github.com/sizning-repo/foodie.git /home/muhammad/foodie
   cd /home/muhammad/foodie
   ```

---

2. Environment Sozlamalari (`.env`)**
    ```bash
    cp .env.example .env
    nano .env
    ```
    **Muhim o'zgaruvchilar:**
    ```ini
    DEBUG=0
    SECRET_KEY=your_production_secret_key
    ALLOWED_HOSTS=example.com,server_ip
    DATABASE_URL=postgres://muhammad:password@db:5432/foodie
    ```



---

4. **Docker Image Yaratish**
    ```bash
    docker-compose build
    ```

---

6. **Docker-da Ishga Tushirish**
    ```bash
     docker-compose up -d
    ```

---

7. **Nginx Sozlash (Reverse Proxy)**
    ```bash
    sudo apt install -y nginx
    sudo nano /etc/nginx/sites-available/foodie
    ```
    **Nginx Konfigi:**
    ```nginx
    server {
        listen 80;
        server_name example.com www.example.com;
    
        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    
        location /static/ {
            alias /home/muhammad/foodie/staticfiles/;
        }
    
        location /media/ {
            alias /home/muhammad/foodie/media/;
        }
    }
    ```
    ```bash
    sudo ln -s /etc/nginx/sites-available/foodie /etc/nginx/sites-enabled
    sudo nginx -t && sudo systemctl restart nginx
    ```

---

8. **SSL Certbot (HTTPS)**
    ```bash
    sudo apt install -y certbot python3-certbot-nginx
    sudo certbot --nginx -d example.com -d www.example.com
    ```

---

9. **Firewall Sozlash**
    ```bash
    sudo ufw allow 80
    sudo ufw allow 443
    sudo ufw allow ssh
    sudo ufw enable
    ```

---

10. **Monitoring va Loglar**
    ```bash
    # Loglarni ko'rish
    docker-compose logs -f web
    sudo tail -f /var/log/nginx/error.log
    
    # Process monitoring
    sudo apt install -y htop
    htop
    ```

---

11. **Avtomatik Yangilash (CI/CD)**
`.github/workflows/deploy.yml` (GitHub Actions misoli):
    ```yaml
    name: Deploy
    on: [push]
    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - run: ssh user@server "cd /home/muhammad/foodie && git pull && docker-compose up -d --build"
    ```

---

**Muhim Production Sozlamalari**

`settings.py`
```python
# Xavfsizlik
DEBUG = False
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Static fayllar
STATIC_ROOT = '/home/muhammad/foodie/staticfiles'
```

`Dockerfile Optimizatsiya`
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "foodie.wsgi:application"]
```

---

### **Xatoliklar va Tekshiruvlar**
```bash
# Django check
docker-compose exec web python manage.py check --deploy

# DB connection
docker-compose exec db psql -U muhammad -d foodie

# Port tekshirish
sudo lsof -i :8000
```

---

### **Yakuniy Tekshiruvlar**
1. Brauzerda `https://example.com` oching
2. Admin panelni tekshiring: `https://example.com/admin`
3. `DEBUG=False` da xatolik sahifasi ishlayotganligiga ishonch hosil qiling

---

### **Qo'shimcha Maslahatlar**
- Har kuni backup: `docker-compose exec db pg_dump -U muhammad foodie > backup.sql`
- Yangiliklarni kuzatish: `journalctl -u docker --since "1 hour ago"`
- Load balancer qo'shish (Agar trafik ko'p bo'lsa)

Productionga tushirishdan oldin **staging serverda** sinovdan o'tkazishni unutmang! 🚀









