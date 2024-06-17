from fastapi.testclient import TestClient
from app.main import APP

client = TestClient(APP)


class TestApp:

    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}
