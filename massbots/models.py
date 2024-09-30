from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from .openapi.models import *


T = TypeVar("T", bound="Channel")


@_attrs_define
class CustomChannel(Channel):
    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        description = self.description
        url = self.url
        banner_url = self.banner_url
        comment_count = self.comment_count
        subscriber_count = self.subscriber_count
        video_count = self.video_count
        view_count = self.view_count

        # Handle case where thumbnails might be None
        thumbnails = self.thumbnails.to_dict() if self.thumbnails is not None else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "description": description,
                "url": url,
                "banner_url": banner_url,
                "comment_count": comment_count,
                "subscriber_count": subscriber_count,
                "video_count": video_count,
                "view_count": view_count,
                "thumbnails": thumbnails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        description = d.pop("description")

        url = d.pop("url")

        banner_url = d.pop("banner_url")

        comment_count = d.pop("comment_count")

        subscriber_count = d.pop("subscriber_count")

        video_count = d.pop("video_count")

        view_count = d.pop("view_count")

        # Handle case where thumbnails might be None
        thumbnails_data = d.pop("thumbnails", None)
        thumbnails = (
            ChannelThumbnails.from_dict(thumbnails_data)
            if thumbnails_data is not None
            else None
        )

        channel = cls(
            id=id,
            title=title,
            description=description,
            url=url,
            banner_url=banner_url,
            comment_count=comment_count,
            subscriber_count=subscriber_count,
            video_count=video_count,
            view_count=view_count,
            thumbnails=thumbnails,
        )

        channel.additional_properties = d
        return channel


T = TypeVar("T", bound="Video")


@_attrs_define
class CustomVideo(Video):
    category_id: str = None

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        description = self.description
        url = self.url
        published_at = self.published_at
        channel_id = self.channel_id
        channel_title = self.channel_title
        channel_url = self.channel_url
        comment_count = self.comment_count
        like_count = self.like_count
        view_count = self.view_count

        # Handle case where thumbnails might be None
        thumbnails = self.thumbnails.to_dict() if self.thumbnails else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "description": description,
                "url": url,
                "published_at": published_at,
                "channel_id": channel_id,
                "channel_title": channel_title,
                "channel_url": channel_url,
                "comment_count": comment_count,
                "like_count": like_count,
                "view_count": view_count,
                "thumbnails": thumbnails,
            }
        )

        # Conditionally add category_id if it is not None
        if self.category_id is not None:
            field_dict["category_id"] = self.category_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()
        id = d.pop("id")
        title = d.pop("title")
        description = d.pop("description")
        url = d.pop("url")
        published_at = d.pop("published_at")

        # Handle case where category_id might be missing
        category_id = d.pop("category_id", None)

        channel_id = d.pop("channel_id")
        channel_title = d.pop("channel_title")
        channel_url = d.pop("channel_url")
        comment_count = d.pop("comment_count")
        like_count = d.pop("like_count")
        view_count = d.pop("view_count")

        # Handle case where thumbnails might be None
        thumbnails_data = d.pop("thumbnails", None)
        thumbnails = (
            VideoThumbnails.from_dict(thumbnails_data) if thumbnails_data else None
        )

        video = cls(
            id=id,
            title=title,
            description=description,
            url=url,
            published_at=published_at,
            category_id=category_id,
            channel_id=channel_id,
            channel_title=channel_title,
            channel_url=channel_url,
            comment_count=comment_count,
            like_count=like_count,
            view_count=view_count,
            thumbnails=thumbnails,
        )

        video.additional_properties = d
        return video


T = TypeVar("T", bound="CustomVideoFormat")


class CustomVideoFormat(VideoFormat):
    file_size: int | None = None

    def __init__(self, format_: str, cached: bool, file_size: int | None = None):
        super().__init__(format_=format_, cached=cached, file_size=file_size)

    def to_dict(self) -> Dict[str, Any]:
        field_dict = super().to_dict()

        # Remove file_size if it's None
        if self.file_size is None:
            field_dict.pop("file_size", None)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        # Handle the case where file_size might be missing or None
        file_size = src_dict.get("file_size")
        return cls(
            format_=src_dict["format"], cached=src_dict["cached"], file_size=file_size
        )


@_attrs_define
class VideoFormats:
    """A collection of video formats"""

    formats: Dict[str, CustomVideoFormat] = _attrs_field(factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        # Convert each CustomVideoFormat object in the dictionary to its dictionary representation
        return {key: value.to_dict() for key, value in self.formats.items()}

    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> "VideoFormats":
        # Convert the dictionary into CustomVideoFormat objects
        formats = {
            key: CustomVideoFormat.from_dict(value) for key, value in src_dict.items()
        }
        return cls(formats=formats)

    def add_format(self, video_format: CustomVideoFormat) -> None:
        # Add a new format to the collection
        self.formats[video_format.format_] = video_format

    def filter(self, cached: bool):
        return {u: v for u, v in self.formats.items() if v.cached == cached}

    def __getitem__(self, key: str) -> CustomVideoFormat:
        return self.formats[key]

    def __setitem__(self, key: str, value: CustomVideoFormat) -> None:
        self.formats[key] = value

    def __delitem__(self, key: str) -> None:
        del self.formats[key]

    def __contains__(self, key: str) -> bool:
        return key in self.formats
