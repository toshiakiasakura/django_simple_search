# syntax=docker/dockerfile:1
FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN mkdir /static
COPY ./static /static

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/

