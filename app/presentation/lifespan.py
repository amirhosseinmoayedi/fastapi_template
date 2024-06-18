from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_fastapi_instrumentator.instrumentation import PrometheusFastApiInstrumentator


def setup_prometheus(app: FastAPI) -> None:
    """
    Enables prometheus integration.

    :param app: current application.
    """
    PrometheusFastApiInstrumentator(should_group_status_codes=False).instrument(
        app,
    ).expose(app, should_gzip=True, name="prometheus_metrics")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    on start up behaviour is before the yield and shutdown is after the yield

    :param app:
    """
    app.middleware_stack = None
    setup_prometheus(app)
    app.middleware_stack = app.build_middleware_stack()
    # startup
    yield
    # shutdown
