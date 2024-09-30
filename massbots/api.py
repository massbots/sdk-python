"""Realisation of Api class"""

from __future__ import annotations
import time
from typing import Callable

import requests

from . import models
from .error import ApiError


class Api:
    """
    The `Api` class provides methods to interact with the massbots.xyz API,
    allowing you to retrieve information about videos,channels, perform searches,
    and manage downloads.
    """

    base_url: str = "https://api.massbots.xyz"
    request_timeout = 300

    def __init__(self, token: str, bot_id: str | None = None):
        """
        Initializes the Api instance with the provided token and optional bot_id.

        Args:
            token (str): The API token for authentication.
            bot_id (str | None): An optional bot ID for bot-specific API calls.
        """
        self._token = token
        self._bot_id = bot_id

    def balance(self) -> int:
        """
        Retrieves the balance of the authenticated account.

        Returns:
            int: The balance of the account.
        """
        return models.Balance.from_dict(
            self._query_api(f"{self.base_url}/me/balance")
        ).balance

    def video_formats(self, video_id: str) -> models.VideoFormats:
        """
        Fetches available video formats for a given video ID.

        Args:
            video_id (str): The ID of the video.

        Returns:
            models.VideoFormats: An object containing information about available video formats.
        """
        data = self._query_api(f"{self.base_url}/video/{video_id}/formats")

        return models.VideoFormats.from_dict(data)

    def channel(self, channel_id: str) -> models.CustomChannel:
        """
        Retrieves information about a specific channel.

        Args:
            channel_id (str): The ID of the channel.

        Returns:
            models.CustomChannel: An object containing the channel information.
        """
        return models.CustomChannel.from_dict(
            self._query_api(f"{self.base_url}/channel/{channel_id}")
        )

    def search(self, query: str) -> list[Video]:
        """
        Searches for videos based on a query string.

        Args:
            query (str): The search query.

        Returns:
            list[Video]: A list of Video objects matching the search criteria.
        """
        from pprint import pprint

        data = self._query_api(f"{self.base_url}/search?q={query}")
        pprint(data)
        videos = [models.CustomVideo.from_dict(video) for video in data]
        return [Video(video, self, video.id) for video in videos]

    def video(self, video_id: str) -> Video:
        """
        Retrieves details about a specific video.

        Args:
            video_id (str): The ID of the video.

        Returns:
            Video: A Video object containing the video's details.
        """
        video = models.CustomVideo.from_dict(
            self._query_api(f"{self.base_url}/video/{video_id}")
        )
        return Video(video, self, video_id)

    def download(self, video_id: str, video_format: str) -> DownloadResult:
        """
        Initiates a download for a video in a specified format.

        Args:
            video_id (str): The ID of the video.
            video_format (str): The desired format for the download (e.g. 360p, 720p).

        Returns:
            DownloadResult: A DownloadResult object to track the download progress.
        """
        r = models.DownloadResult.from_dict(
            self._query_api(f"{self.base_url}/video/{video_id}/download/{video_format}")
        )
        return DownloadResult(r, self, video_id, video_format)

    def _query_api(self, url: str) -> dict:
        """
        Internal method to send a GET request to the specified API URL.

        Args:
            url (str): The API endpoint URL.

        Returns:
            dict: The JSON response from the API.

        Raises:
            ApiError: If the API response status code is not 200.
        """
        headers = {"X-Token": f"{self._token}"}
        if self._bot_id is not None:
            headers["X-Bot-Id"] = self._bot_id

        response = self._get_request(url, headers=headers)
        if response.status_code != requests.codes.ok:
            raise ApiError(status=response.status_code, data=response.json())

        return response.json()

    @classmethod
    def _get_request(cls, *args, **kwargs):
        """
        A static method to perform a GET request using the requests library.

        Returns:
            requests.Response: The response object.
        """
        return requests.get(*args, **kwargs, timeout=cls.request_timeout)


class DownloadResult(models.DownloadResult):
    """
    Represents the result of a video download process and provides methods
    to track the download's readiness status.
    """

    def __init__(
        self, r: models.DownloadResult, api: Api, video_id: str, video_format: str
    ):
        """
        Initializes the DownloadResult instance.

        Args:
            r (models.DownloadResult): The raw download result from the API.
            api (Api): The Api instance used for making requests.
            video_id (str): The ID of the video being downloaded.
            video_format (str): The format of the video being downloaded.
        """
        super().__init__(**r.to_dict())
        self._api: Api = api
        self._video_id: str = video_id
        self._format: str = video_format

    def wait_until_ready(
        self,
        delay: float = 5.0,
        callback: Callable[[models.DownloadResult], bool] | None = None,
    ) -> models.DownloadResult:
        """
        Waits until the download result is either ready or failed.

        Args:
            delay (float): Interval between polling requests in seconds. Default is 5.0.
            callback (Callable[[models.DownloadResult], bool], optional):
                      A callback function called on each iteration.
                      If it returns True, the waiting is interrupted.

        Returns:
            models.DownloadResult: The final download result when ready or failed.
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


class Video(models.CustomVideo):
    """
    Represents a video entity and provides methods to interact with its details and formats.
    """

    def __init__(self, r: models.CustomVideo, api: Api, video_id: str):
        """
        Initializes the Video instance.

        Args:
            r (models.CustomVideo): The raw video data from the API.
            api (Api): The Api instance used for making requests.
            video_id (str): The ID of the video.
        """
        super().__init__(**r.to_dict())
        self._api: Api = api
        self._video_id: str = video_id

    def formats(self) -> models.VideoFormats:
        """
        Retrieves the available formats for this video.

        Returns:
            models.VideoFormats: An object containing information about available video formats.
        """
        return self._api.video_formats(self.id)

    def download(self, video_format: str) -> DownloadResult:
        """
        Initiates a download for this video in a specified format.

        Args:
            video_format (str): The desired format for the download (e.g. 360p, 720p).

        Returns:
            DownloadResult: An object representing the download process.
        """
        return self._api.download(self.id, video_format)
