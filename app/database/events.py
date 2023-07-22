import logging
import os

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to database...")

    engine = create_async_engine(
        url=str(os.getenv("DATABASE_URL")), pool_size=50, max_overflow=0, echo=True, future=True)
    async_session_factory = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=True)
    app.state.pool = async_session_factory

    # await init_rates(settings)
    logger.info("Connected to database.")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing database connection...")

    # app.state.pool.close_all()

    logger.info("Database connection closed.")
