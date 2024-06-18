from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from app.settings import settings

from app.presentation.apis.router import api_router
from app.presentation.lifetime import register_startup_event, register_shutdown_event


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    #
    app = FastAPI(
        title="fastapi template",
        version=settings.version,
        docs_url=None,
        redoc_url=None,
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    register_startup_event(app)
    register_shutdown_event(app)

    app.include_router(router=api_router, prefix="/api")

    return app
