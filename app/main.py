from typing import Dict

from fastapi import FastAPI

APP = FastAPI()


@APP.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}
