from typing import (
    Any,
    Type,
    TypeVar,
    TYPE_CHECKING,
)


from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from .video_thumbnails import VideoThumbnails


T = TypeVar("T", bound="Video")


@_attrs_define
class Video:
    """YouTube video

    Attributes:
        id (str):
        title (str):
        description (str):
        url (str):
        published_at (str):
        category_id (str):
        channel_id (str):
        channel_title (str):
        channel_url (str):
        comment_count (int):
        like_count (int):
        view_count (int):
        thumbnails (VideoThumbnails):
    """

    id: str
    title: str
    description: str
    url: str
    published_at: str
    category_id: str
    channel_id: str
    channel_title: str
    channel_url: str
    comment_count: int
    like_count: int
    view_count: int
    thumbnails: "VideoThumbnails"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from .video_thumbnails import VideoThumbnails

        id = self.id

        title = self.title

        description = self.description

        url = self.url

        published_at = self.published_at

        category_id = self.category_id

        channel_id = self.channel_id

        channel_title = self.channel_title

        channel_url = self.channel_url

        comment_count = self.comment_count

        like_count = self.like_count

        view_count = self.view_count
        
        if not isinstance(self.thumbnails, VideoThumbnails):
            self.thumbnails = VideoThumbnails.from_dict(self.thumbnails)
        
        thumbnails = self.thumbnails.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "description": description,
                "url": url,
                "published_at": published_at,
                "category_id": category_id,
                "channel_id": channel_id,
                "channel_title": channel_title,
                "channel_url": channel_url,
                "comment_count": comment_count,
                "like_count": like_count,
                "view_count": view_count,
                "thumbnails": thumbnails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: dict[str, Any]) -> T:
        from .video_thumbnails import VideoThumbnails

        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        description = d.pop("description")

        url = d.pop("url")

        published_at = d.pop("published_at")

        category_id = d.pop("category_id", 0)

        channel_id = d.pop("channel_id")

        channel_title = d.pop("channel_title")

        channel_url = d.pop("channel_url")

        comment_count = d.pop("comment_count")

        like_count = d.pop("like_count")

        view_count = d.pop("view_count")

        thumbnails = VideoThumbnails.from_dict(d.pop("thumbnails"))

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

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
