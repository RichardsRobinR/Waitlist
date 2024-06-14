FROM python:3.12.3-slim

RUN apt-get update && apt-get install -y virtualenv
RUN virtualenv env

WORKDIR /workdir

COPY requirements.txt /workdir

RUN pip install -r requirements.txt

COPY . /workdir

EXPOSE 8000

RUN python manage.py migrate

CMD python /workdir/manage.py runserver 0.0.0.0:8000
