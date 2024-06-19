from typing import List


class DummyService:
    def __init__(self):
        pass

    def get_dummies(self) -> List[dict]:
        return [{"id": 1, "name": "Dummy 1"}, {"id": 2, "name": "Dummy 2"}]

    def get_dummy(self, identifier) -> dict:
        return {"id": 1, "name": "Dummy 1"}

    def create_dummy(self, dummy):
        pass

    def update_dummy(self, dummy):
        pass
