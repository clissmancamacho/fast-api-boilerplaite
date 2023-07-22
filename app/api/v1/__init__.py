from fastapi import APIRouter

from app.api.v1 import quotes

api_router = APIRouter()

api_router.include_router(quotes.router, prefix="/quotes", tags=["quotes"])
