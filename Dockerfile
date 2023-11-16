FROM python:3.10-alpine3.17

ENV PYTHONUNBUFFERED 1

# Install poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /app

# Copy hanya pyproject.toml dan poetry.lock untuk cache layer
COPY pyproject.toml poetry.lock /app/
RUN poetry install

COPY . /app/

CMD ["python", "manage.py", "migrate"]