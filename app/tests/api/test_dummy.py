from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from starlette import status

from app.presentation.application import get_app
from app.service import DummyService


@pytest.fixture
def client():
    return TestClient(get_app())


@pytest.fixture
def mock_dummy_service():
    return MagicMock(spec=DummyService)


class TestDummyView:
    def test_get_dummies(self, client: TestClient):
        response = client.get("/api/v1/dummy/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [
            {"id": 1, "name": "Dummy 1"},
            {"id": 2, "name": "Dummy 2"},
        ]

    def test_create_dummy_model(self, client: TestClient):
        dummy_data = {"name": "New Dummy"}
        response = client.post("/api/v1/dummy/", json=dummy_data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_dummy_model(self, client: TestClient):
        dummy_id = 1
        response = client.get(f"/api/v1/dummy/{dummy_id}")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"id": dummy_id, "name": "Dummy 1"}

    def test_update_dummy_model(self, client: TestClient):
        dummy_id = 1
        dummy_data = {"name": "Updated Dummy"}
        response = client.patch(f"/api/v1/dummy/{dummy_id}", json=dummy_data)
        assert response.status_code == status.HTTP_200_OK
