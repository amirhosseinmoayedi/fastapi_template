from typing import Union


class CommonQueryParams:
    """
    Common query parameters for all endpoints

    Attributes:
    - q: str: search query
    - skip: int: number of items to skip
    - limit: int: number of items to return

    """

    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit
