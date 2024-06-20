"""
Main router for the API.
"""

from fastapi import APIRouter

from app.presentation.apis import docs
from app.presentation.apis import dummy
from app.presentation.apis import health_check

api_router = APIRouter()
api_router_v1 = APIRouter(prefix="/v1")

api_router_v1.include_router(dummy.router, prefix="/dummy", tags=["dummy"])

api_router.include_router(docs.router)
api_router.include_router(health_check.router, prefix="/health", tags=["health_check"])
api_router.include_router(api_router_v1)
