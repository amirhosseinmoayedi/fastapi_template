from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.tests.factories.dummy import DummyModelFactory


class TestDummyView:
    @pytest.fixture(autouse=True)
    async def setup(self, client: TestClient, dbsession: AsyncSession):
        # setup for this fixture
        DummyModelFactory.create_batch(10)
        yield
        # teardown for this fixture
        DummyModelFactory.clean_up()

    @pytest.mark.anyio
    async def test_create_dummy_model(self, client: TestClient, dbsession: AsyncSession):
        dummy_data = {"name": "New Dummy"}
        response = client.post("/api/v1/dummy/", json=dummy_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json().get("id") == 11
        assert response.json().get("name") == "New Dummy"
        assert (
            datetime.strptime(response.json().get("created_at"), "%Y-%m-%dT%H:%M:%S.%f").date()
            == datetime.today().date()
        )

    @pytest.mark.anyio
    async def test_get_dummies(self, client: TestClient, dbsession: AsyncSession):
        response = client.get("/api/v1/dummy")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 10
        assert response.json()[0].get("id") is not None
        assert response.json()[0].get("name") is not None
        assert response.json()[0].get("created_at") is not None
        assert response.json()[0].get("updated_at") is not None
