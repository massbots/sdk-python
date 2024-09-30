from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VideoFormat")


@_attrs_define
class VideoFormat:
    """Video format

    Attributes:
        format_ (str): Video resolution
        cached (bool): Set to `true` if the format is cached for quick downloading<br>
        file_size (int): File size in bytes, available only if video is not cached
    """

    format_: str
    cached: bool
    file_size: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        format_ = self.format_

        cached = self.cached

        file_size = self.file_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "cached": cached,
                "file_size": file_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        format_ = d.pop("format")

        cached = d.pop("cached")

        file_size = d.pop("file_size")

        video_format = cls(
            format_=format_,
            cached=cached,
            file_size=file_size,
        )

        video_format.additional_properties = d
        return video_format

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
