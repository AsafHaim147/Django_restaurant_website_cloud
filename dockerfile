FROM python:3.10-slim

WORKDIR /BeitHaam

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY BeitHaam/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD python BeitHaam/manage.py runserver 0.0.0.0:8000