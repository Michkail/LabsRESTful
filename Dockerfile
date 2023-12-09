FROM python:3.10-alpine3.17

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install poetry && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/
RUN poetry install

COPY . /app/
