FROM python:3.9.1-alpine
LABEL maintainer="Lauren Pappas"
LABEL version="1.0"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
