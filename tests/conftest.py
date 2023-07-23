from os import environ

import pytest_asyncio
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

environ["APP_ENV"] = "test"


@pytest_asyncio.fixture
def app() -> FastAPI:
    from app.main import create_app  # local import for testing purpose

    return create_app()


@pytest_asyncio.fixture
async def initialized_app(app: FastAPI) -> FastAPI:
    import os

    async with LifespanManager(app):
        engine = create_async_engine(url=str(os.getenv("DATABASE_URL")), pool_size=10, max_overflow=0, echo=False, future=True)
        async_session_factory = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=True)
        app.state.pool = async_session_factory
        yield app


@pytest_asyncio.fixture
async def client(initialized_app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://test",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client
