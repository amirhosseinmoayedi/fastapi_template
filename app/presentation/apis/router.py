from fastapi import APIRouter

from app.presentation.apis import docs
from app.presentation.apis import health_check

api_router = APIRouter()

api_router.include_router(docs.router)
api_router.include_router(health_check.router, prefix="/health", tags=["health_check"])
