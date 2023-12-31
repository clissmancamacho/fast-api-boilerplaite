from typing import Callable

from fastapi import FastAPI

from app.database.events import close_db_connection, connect_to_db


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app)

    return start_app


def create_stop_app_handler(app):
    async def stop_app():
        await close_db_connection(app)

    return stop_app
