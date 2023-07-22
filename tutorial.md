# Tutorial

pip install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn

docker-compose run app poetry run alembic revision --autogenerate -m "New Migration"
docker-compose run app poetry run alembic upgrade head

docker-compose build
docker-compose up
