FROM python:3.13.2

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p staticfiles && chmod -R 777 staticfiles

RUN python manage.py collectstatic

CMD ["/bin/bash", "docker-entrypoint.sh"]