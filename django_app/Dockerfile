FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY django_app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY django_app /app

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "ars0n_django.wsgi:application", "-b", "0.0.0.0:8000", "--workers=3"]
