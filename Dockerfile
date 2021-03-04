FROM python:2.7.10

RUN mkdir /app

COPY . /app

WORKDIR /app

EXPOSE 65432

