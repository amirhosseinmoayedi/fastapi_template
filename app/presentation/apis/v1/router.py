from fastapi import APIRouter

from app.presentation.apis.v1 import dummy, docs

router = APIRouter(prefix="/v1")

router.include_router(docs.router)
router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
