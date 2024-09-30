from typing import (
    Any,
    Type,
    TypeVar,
    TYPE_CHECKING,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from .thumbnail import Thumbnail


T = TypeVar("T", bound="VideoThumbnails")


@_attrs_define
class VideoThumbnails:
    """ """

    additional_properties: dict[str, "Thumbnail"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from .thumbnail import Thumbnail

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: dict[str, Any]) -> T:
        from .thumbnail import Thumbnail

        d = src_dict.copy()
        video_thumbnails = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Thumbnail.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        video_thumbnails.additional_properties = additional_properties
        return video_thumbnails

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "Thumbnail":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "Thumbnail") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
