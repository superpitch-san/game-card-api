FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app/card-game-api

COPY requirements.txt /app/card-game-api/

RUN pip install -r requirements.txt && pip install django-tastypie && pip install django-cors-headers

COPY . /app/card-game-api/

RUN python manage.py makemigrations && python manage.py migrate