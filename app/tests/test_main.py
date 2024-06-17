from fastapi.testclient import TestClient
from app.presentation.application import get_app

client = TestClient(get_app())


class TestApp:

    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "hello world"}
