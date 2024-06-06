FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN apt-get install -y python3-pip
RUN pip install poetry
COPY poetry.lock /
COPY pyproject.toml /
RUN poetry install
COPY . /