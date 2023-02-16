FROM python:3.9

RUN mkdir app

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip3 install gunicorn

RUN python manage.py makemigrations

RUN python manage.py migrate


