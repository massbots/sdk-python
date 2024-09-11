class ApiError(Exception):
    def __init__(
        self,
        status: int = None,
        data: dict = None,
    ):
        self.status = status
        self.error = data.get("error", "")

    def __str__(self):
        return f"{self.error} ({self.status})"
