FROM python:3.12.1-slim

WORKDIR /app

COPY poetry.lock ./
COPY pyproject.toml .

RUN python -m pip install poetry
RUN pip install --upgrade pip

COPY . /app/

WORKDIR appTreinoBackend/

RUN poetry install --no-dev
RUN poetry run python manage.py makemigrations
RUN poetry run python manage.py migrate

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]