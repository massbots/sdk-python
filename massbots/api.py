from __future__ import annotations
import requests
import time

import models
from .error import ApiError

from typing import List, Callable, Optional


class Api:
    base_url: str = "https://api.massbots.xyz"

    def __init__(self, token: str, bot_id: Optional[str] = None):
        self.token = token
        self.bot_id = bot_id

    def balance(self) -> int:
        return models.Balance.from_dict(self.__do(f"{self.base_url}/me/balance")).balance

    def video_formats(self, id: str) -> List[models.VideoFormat]:
        data = self.__do(f"{self.base_url}/video/{id}/formats")
        return [models.VideoFormat.from_dict(data[format]) for format in data]

    def channel(self, id: str) -> models.Channel:
        return models.Channel.from_dict(self.__do(f"{self.base_url}/channel/{id}"))

    def search(self, query: str) -> List[Video]:
        data = self.__do(f"{self.base_url}/search?q={query}")
        videos = [models.Video.from_dict(video) for video in data]
        return [Video(video, self, video.id) for video in videos]

    def video(self, id: str) -> Video:
        video = models.Video.from_dict(self.__do(f"{self.base_url}/video/{id}"))
        return Video(video, self, id)

    def download(self, id: str, format: str) -> DownloadResult:
        r = models.DownloadResult.from_dict(
            self.__do(f"{self.base_url}/video/{id}/download/{format}")
        )
        return DownloadResult(r, self, id, format)

    def __do(self, url: str):
        headers = {
            "X-Token": f"{self.token}"
        }
        if self.bot_id is not None:
            headers["X-Bot-Id"] = self.bot_id

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise ApiError(
                status=response.status_code,
                reason=response.json().get("error"),
                http_resp=response,
                body=response.json()
            )
        return response.json()


class DownloadResult(models.DownloadResult):
    def __init__(self, r: models.DownloadResult, api, video_id, format):
        super().__init__(**r.to_dict())
        self.api = api
        self._video_id = video_id
        self._format = format

    def wait_until_ready(
        self,
        delay: float = 5.0,
        callback: Callable[[models.DownloadResult], bool] = None,
    ) -> models.DownloadResult:
        """
        Waits until the download result is ready or failed.

        Args:
            delay (float): Interval between polling requests. Default is 5.0 seconds.
            callback (Callable[[dl.Result], bool]): Callback function for each iteration.
        """
        if not delay or delay <= 0:
            delay = 1.0

        while True:
            r = self.api.download(self._video_id, self._format)
            if callback and callback(r):
                return r
            if r.status in ("ready", "failed"):
                return r
            time.sleep(delay)


class Video(models.Video):
    def __init__(self, r: models.Video, api, video_id):
        super().__init__(**r.to_dict())
        self.api = api
        self._video_id = video_id

    def formats(self) -> List[models.VideoFormat]:
        return self.api.video_formats(self.id)

    def download(self, format: str) -> DownloadResult:
        return self.api.download(self.id, format)
