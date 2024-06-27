from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_fastapi_instrumentator.instrumentation import PrometheusFastApiInstrumentator

from app.presentation.limiter import setup_limiter
from app.repository.db.utils import setup_db, close_db


def setup_prometheus(app: FastAPI) -> None:
    """
    Enables prometheus integration.

    :param app: current application.
    """
    PrometheusFastApiInstrumentator(should_group_status_codes=False).instrument(
        app,
    ).expose(app, should_gzip=True, name="metrics")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    on start up behaviour is before the yield and shutdown is after the yield

    :param app:
    """
    # startup
    print("started")
    app.middleware_stack = None
    setup_prometheus(app)
    setup_limiter(app)

    await setup_db(app)
    app.middleware_stack = app.build_middleware_stack()
    yield
    # shutdown
    await close_db(app)
