import json
from typing import Optional, Any
from json import JSONDecodeError


class ApiError(Exception):
    def __init__(
        self,
        status=None,
        http_resp=None,
        *,
        body: Optional[Any] = None
    ):
        self.status = status
        self.http_resp = http_resp
        self.body = body

    def __str__(self):
        s = f"({self.status})"
        if 'error' in self.body:
            s += f": {self.body['error']}"
        return s

