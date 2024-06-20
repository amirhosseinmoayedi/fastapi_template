from typing import Annotated, List

from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from app.presentation.apis.dummy.v1.schema import DummyResponse, DummyRequest
from app.presentation.utils import CommonQueryParams
from app.service import DummyService

router = APIRouter()


@cbv(router)
class DummyView:
    service: DummyService = Depends(DummyService)

    @router.get("/", status_code=200, response_model=List[DummyResponse])
    async def get_dummies(
        self, commons_params: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
    ) -> list[dict]:
        """
        Retrieve all dummy objects from the database.

        :param commons_params:
        :return: list of dummy objects from database.
        """
        return self.service.get_dummies()

    @router.post("/", status_code=201)
    async def create_dummy_model(self, dummy_object: DummyRequest) -> None:
        """
        Creates dummy model in the database.

        :param dummy_object: new dummy model item.
        """
        return self.service.create_dummy(dummy_object)

    @router.get("/{dummy_id}", status_code=200, response_model=DummyResponse)
    def get_dummy_model(self, dummy_id: int) -> dict:
        """
        Retrieve a dummy object from the database.

        :param dummy_id: id of the dummy object.
        :return: dummy object from database.
        """
        return self.service.get_dummy(dummy_id)

    @router.patch(
        "/{dummy_id}",
        status_code=200,
    )
    def update_dummy_model(self, dummy_id: int, dummy_object: DummyRequest) -> None:
        """
        Updates a dummy object in the database.

        :param dummy_id: id of the dummy object.
        :param dummy_object: updated dummy object.
        """
        return self.service.update_dummy(dummy_id, dummy_object)
