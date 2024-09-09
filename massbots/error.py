import json
from typing import Optional, Any
from json import JSONDecodeError


class ApiError(Exception):
    def __init__(
        self,
        status=None,
        reason=None,
        http_resp=None,
        *,
        body: Optional[Any] = None
    ):
        self.status = status
        self.reason = reason
        self.http_resp = http_resp
        self.body = body

    def __str__(self):
        s = f"{self.reason} ({self.status})"
        if self.body.error:
            s += f": {self.body.error}"
        return s

