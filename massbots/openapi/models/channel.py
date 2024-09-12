from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field



from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from .channel_thumbnails import ChannelThumbnails





T = TypeVar("T", bound="Channel")


@_attrs_define
class Channel:
    """ YouTube channel

        Attributes:
            id (str):
            title (str):
            description (str):
            url (str):
            banner_url (str):
            comment_count (int):
            subscriber_count (int):
            video_count (int):
            view_count (int):
            thumbnails (ChannelThumbnails):
     """

    id: str
    title: str
    description: str
    url: str
    banner_url: str
    comment_count: int
    subscriber_count: int
    video_count: int
    view_count: int
    thumbnails: 'ChannelThumbnails'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from .channel_thumbnails import ChannelThumbnails
        id = self.id

        title = self.title

        description = self.description

        url = self.url

        banner_url = self.banner_url

        comment_count = self.comment_count

        subscriber_count = self.subscriber_count

        video_count = self.video_count

        view_count = self.view_count

        thumbnails = self.thumbnails.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
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
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from .channel_thumbnails import ChannelThumbnails
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

        thumbnails = None
        thumbs = d.pop("thumbnails", None)
        if thumbs is not None:
            thumbnails = ChannelThumbnails.from_dict(thumbs)




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

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
