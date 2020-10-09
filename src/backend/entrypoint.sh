FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq && apt-get install -y wait-for-it

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/