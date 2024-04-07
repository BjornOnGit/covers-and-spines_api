FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN command
WORKDIR /app
COPY requirements.txt /app
RUN python -m pip install requests
RUN python -m pip install -r requirements.txt

COPY . /app
