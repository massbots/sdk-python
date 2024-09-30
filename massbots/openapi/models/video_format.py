from typing import Any, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

import json


T = TypeVar("T", bound="VideoFormat")


@_attrs_define
class VideoFormat:
    """Video format

    Attributes:
        format (str): Video resolution
        cached (bool): Set to `true` if the format is cached for quick downloading
        file_size (int): File size in bytes, available only if video is not cached
    """

    format: str
    cached: bool
    file_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format = self.format

        cached = self.cached

        file_size = self.file_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format,
                "cached": cached,
                "file_size": file_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        format_ = d.pop("format")

        cached = d.pop("cached")

        file_size = d.pop("file_size", 0)

        video_format = cls(
            format=format_,
            cached=cached,
            file_size=file_size,
        )

        video_format.additional_properties = d
        return video_format

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


@_attrs_define
class VideoFormats:
    """VideoFormats class that contains a list of VideoFormat instances

    Attributes:
        formats (list[VideoFormat]): list of video formats
    """

    formats: list[VideoFormat] = _attrs_field(factory=list)
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        formats_dict = [format.to_dict() for format in self.formats]
        field_dict: dict[str, Any] = {"formats": formats_dict}
        field_dict.update(self.additional_properties)
        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        # Initialize an empty list for formats
        formats_list = []

        # Iterate through the input dictionary and convert each item to VideoFormat
        for format_name, format_data in d.items():
            if isinstance(format_data, dict):
                format_data["format"] = format_name  # Set the format name from the key
                formats_list.append(VideoFormat.from_dict(format_data))

        video_formats = cls(formats=formats_list)

        # If there are any additional properties, assign them
        video_formats.additional_properties = d
        return video_formats

    def to_json(self) -> str:
        """Returns the JSON representation of the VideoFormats instance"""
        return json.dumps(self.to_dict())

    def filter(self, cached: bool) -> list[VideoFormat]:
        return {fmt.format: fmt for fmt in self.formats if fmt.cached}

    @classmethod
    def from_json(cls: Type[T], json_str: str) -> T | None:
        """Create an instance of VideoFormats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

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
