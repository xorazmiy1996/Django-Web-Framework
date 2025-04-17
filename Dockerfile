FROM python:3.13.2

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x docker-entrypoint.sh  # Faylga bajarish huquqini berish
CMD  ["sh", "docker-entrypoint.sh"]