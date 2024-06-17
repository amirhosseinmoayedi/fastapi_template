from typing import Dict

from fastapi import FastAPI


def get_app() -> FastAPI:  # todo: complete this
    app = FastAPI(
        title="fastapi template",
    )

    @app.get("/")
    def root() -> Dict[str, str]:
        return {"message": "hello world"}

    return app
