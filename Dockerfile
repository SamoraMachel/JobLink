FROM python:3.9

RUN mkdir app

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8084

CMD python3 JobLink/manage.py runserver 8084