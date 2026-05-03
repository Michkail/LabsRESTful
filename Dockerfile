FROM python:3.10-alpine3.17

ENV PYTHONUNBUFFERED 1
ENV PIP_NO_BUILD_ISOLATION 1
ENV PIP_USE_PEP517 0

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev

RUN pip install --no-cache-dir \
    "setuptools<70" \
    wheel \
    pkgconfig

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app/
