FROM python:3.12-slim

WORKDIR /app_03

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN apt-get install -y python3-pip
RUN pip install poetry
COPY poetry.lock /app_03/
COPY pyproject.toml /app_03/
RUN poetry install
COPY . /app_03/