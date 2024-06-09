# python
FROM python:3.12.0b3-slim
# work directory
WORKDIR /app
# python envs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
# system depend-s
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get -y install build-essential libssl-dev libffi-dev libblas3 libc6 liblapack3 gcc python3-dev python3-pip cython3

# pip depends
RUN pip install --upgrade pip 
# poetry
RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install
