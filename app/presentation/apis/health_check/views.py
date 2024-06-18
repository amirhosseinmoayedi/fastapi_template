from fastapi import APIRouter
from app.presentation.apis.health_check.schema import HealthCheckMessage

router = APIRouter()


@router.get("/", response_model=HealthCheckMessage)
async def send_echo_message() -> str:
    """
    Health Check endpoint
    """
    return "OK"
