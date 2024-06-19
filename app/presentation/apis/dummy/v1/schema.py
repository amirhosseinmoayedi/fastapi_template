from typing import Optional

from pydantic import BaseModel


class DummyResponse(BaseModel):
    """
    DTO for dummy models.

    It returned when accessing dummy models from the API.
    """

    id: int
    name: str


class DummyRequest(BaseModel):
    """DTO for creating new dummy model."""

    id: Optional[int] = None
    name: str
