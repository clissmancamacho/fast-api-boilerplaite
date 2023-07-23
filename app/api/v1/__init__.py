from fastapi import APIRouter

from app.api.v1 import data, quotes

api_router = APIRouter()

api_router.include_router(quotes.router, prefix="/quotes", tags=["quotes"])
api_router.include_router(data.router, prefix="/data", tags=["data"])
