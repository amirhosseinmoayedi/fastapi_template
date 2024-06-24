from typing import Annotated, List

from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from loguru import logger

from app.presentation.apis.v1.dummy.schema import DummyResponse, DummyRequest
from app.presentation.utils import CommonQueryParams
from app.repository.db.models import DummyModel
from app.service import DummyService

router = APIRouter()


@cbv(router)
class DummyView:

    def __init__(self, service: DummyService = Depends(DummyService)):  # noqa: B008
        self.service: DummyService = service

    @router.get("/error", status_code=500)
    async def get_dummy_error(self):
        """
        :raise value error.
        """
        try:
            raise ValueError("Dummy error")
        except ValueError as e:
            logger.bind(type="DUMMY").error("Dummy error")
            raise e

    @router.get("/", status_code=200, response_model=List[DummyResponse])
    async def get_dummies(
        self, commons_params: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
    ) -> list[DummyModel]:
        """
        Retrieve all dummy objects from the database.

        :param commons_params:
        :return: list of dummy objects from database.
        """
        return await self.service.get_all()

    @router.post("/", status_code=201, response_model=DummyResponse)
    async def create_dummy_model(self, dummy_object: DummyRequest) -> DummyModel:
        """
        Creates dummy model in the database.

        :param dummy_object: new dummy model item.
        """
        return await self.service.create(dummy_object.name)

    @router.get("/{dummy_id}", status_code=200, response_model=DummyResponse)
    async def get_dummy_model(self, dummy_id: int) -> DummyModel:
        """
        Retrieve a dummy object from the database.

        :param dummy_id: id of the dummy object.
        :return: dummy object from database.
        """
        return await self.service.get(dummy_id)

    @router.patch(
        "/{dummy_id}",
        status_code=200,
    )
    async def update_dummy_model(self, dummy_id: int, dummy_object: DummyRequest) -> None:
        """
        Updates a dummy object in the database.

        :param dummy_id: id of the dummy object.
        :param dummy_object: updated dummy object.
        """
        await self.service.update(dummy_id, dummy_object.name)

    @router.delete("/{dummy_id}", status_code=204)
    async def delete_dummy_model(self, dummy_id: int) -> None:
        """
        Deletes a dummy object from the database.

        :param dummy_id: id of the dummy object.
        """
        await self.service.delete(dummy_id)
