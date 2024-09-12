from __future__ import annotations

import requests
import time
from . import models
from .error import ApiError
from typing import List, Callable, Optional, Dict


class Api:
    base_url: str = "https://api.massbots.xyz"

    def __init__(self, token: str, bot_id: Optional[str] = None):
        self._token = token
        self._bot_id = bot_id

    def balance(self) -> int:
        return models.Balance.from_dict(self._do(f"{self.base_url}/me/balance")).balance

    def video_formats(self, id: str) -> models._VideoFormats:
        data = self._do(f"{self.base_url}/video/{id}/formats")
        return models._VideoFormats.from_dict(data)

    def channel(self, id: str) -> models.Channel:
        return models.Channel.from_dict(self._do(f"{self.base_url}/channel/{id}"))

    def search(self, query: str) -> List[Video]:
        data = self._do(f"{self.base_url}/search?q={query}")
        videos = [models.Video.from_dict(video) for video in data]
        return [Video(video, self, video.id) for video in videos]

    def video(self, id: str) -> Video:
        video = models.Video.from_dict(self._do(f"{self.base_url}/video/{id}"))
        return Video(video, self, id)

    def download(self, id: str, format: str) -> DownloadResult:
        r = models.DownloadResult.from_dict(
            self._do(f"{self.base_url}/video/{id}/download/{format}")
        )
        return DownloadResult(r, self, id, format)

    def _do(self, url: str):
        headers = {"X-Token": f"{self._token}"}
        if self._bot_id is not None:
            headers["X-Bot-Id"] = self._bot_id

        resp = requests.get(url, headers=headers)
        data = resp.json()

        if resp.status_code != 200:
            raise ApiError(status=resp.status_code, data=data)

        return data


class DownloadResult(models.DownloadResult):
    def __init__(self, r: models.DownloadResult, api, video_id, format):
        super().__init__(**r.to_dict())
        self._api = api
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
            r = self._api.download(self._video_id, self._format)
            if callback and callback(r):
                return r
            if r.status in ("ready", "failed"):
                return r
            time.sleep(delay)


class Video(models.Video):
    def __init__(self, r: models.Video, api, video_id):
        super().__init__(**r.to_dict())
        self._api = api
        self._video_id = video_id

    def formats(self) -> models._VideoFormats:
        return self._api.video_formats(self.id)

    def download(self, format: str) -> DownloadResult:
        return self._api.download(self.id, format)
