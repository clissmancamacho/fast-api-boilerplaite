# Bookairfreight Test

## Description

This is the solution of Bookairfreight Test using FastAPI with PostgreSQL \
Made with [FastAPI](https://fastapi.tiangolo.com), [PostgreSQL](https://www.postgresql.org/docs), [Docker](https://docs.docker.com), [Coverage](https://coverage.readthedocs.io/en/6.5.0/), [SQLAlchemy](https://docs.sqlalchemy.org/en/14/), [Pytest](https://docs.pytest.org/en/7.2.x/), [Black](https://black.readthedocs.io/en/stable/), [Flake8](https://flake8.pycqa.org/en/latest/), [Isort](https://pycqa.github.io/isort/),
and [Poetry](https://python-poetry.org/docs).

## Features

- 🐍 [Python 3.10](https://docs.python.org/3/) for programming language
- 🚀 [FastAPI](https://fastapi.tiangolo.com) for handling HTTP requests and responses
- 🐳 [Docker](https://docs.docker.com) for containerization
- 🐘 [PostgreSQL](https://www.postgresql.org/docs) for database
- 📦 [Poetry](https://python-poetry.org/docs) for dependency management
- 📈 [Coverage](https://coverage.readthedocs.io/en/6.5.0/) for code coverage
- 🧪 [Pytest](https://docs.pytest.org/en/7.2.x/) for unit and integration testing
- 💾 [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) ORM for interacting with a database
- 🚧 [Flake8](https://flake8.pycqa.org/en/latest/) for linting
- 🎨 [Black](https://black.readthedocs.io/en/stable/) for code formatting
- 📚 [Isort](https://pycqa.github.io/isort/) for sorting imports

## Requirements

- Python 3.10
- Poetry
- PostgreSQL
- Docker

## Getting Started

Every command below except `build` and `run` is executed in a docker container.

### Set Environment Variables

```bash
# Copy service env file
$ cp .env.example .env
```

### Build and run the app with Docker Compose

```bash
# Build docker image
$ docker-compose build

# Run the app in the background
$ docker-compose up -d

# Watch logs
$ docker-compose logs -f

# Execute a command in a running container
$ docker-compose exec app <command>
```

### Migrate database

before test or use the app, you need to migrate the database.

```bash
# init User table
$ docker-compose run app poetry run alembic upgrade head
```

### Test

```bash
# Run unit tests using pytest
$ docker-compose exec app poetry run pytest
```

### Lint and format

```bash
# Run flake8
$ docker-compose exec app poetry run flake8

# Run black
$ docker-compose exec app poetry run black .

# Run isort
$ docker-compose exec app poetry run isort .
```

## API Docs

Visit http://localhost:8000/docs or http://localhost:8000/redoc for API docs

### Add shipping rates

In this link http://localhost:8000/docs#/data/data_init_api_v1_data_init_post
You can upload the rates.json (example in root of repo) file and it will be added to the database.

### Drop shipping rates

You may also want to clear all data to load new ones. In this link you can flush the shipping rates: http://localhost:8000/docs#/data/data_flush_api_v1_data_flush_get

### View PostgreSQL with PgAdmin

You can also see your scheme from PgAdmin: http://localhost:5050, in the .env file there is all the information to configure the connection.
