from __future__ import annotations
from .openapi.models import Video, Channel, VideoFormat, DownloadResult, Balance
from typing import Dict, ClassVar, List, Optional, Any, Set
import json


class _VideoFormats():
    formats: Dict[str, VideoFormat]
    __properties: ClassVar[List[str]] = ["formats"]

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return str(self.formats)

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[_VideoFormats]:
        """Create an instance of VideoFormats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set(
            [
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in formats (dict)
        _field_dict = {}
        if self.formats:
            for _key_formats in self.formats:
                if self.formats[_key_formats]:
                    _field_dict[_key_formats] = self.formats[_key_formats].to_dict()
            _dict['formats'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[_VideoFormats]:
        """Create an instance of VideoFormats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return None

        _obj = _VideoFormats()
        _obj.formats = {"formats": dict(
            (_k, VideoFormat.from_dict(_v))
            for _k, _v in obj["formats"].items()
        )
        if obj.get("formats") is not None
        else None
                        }
        return _obj

    @property
    def formats_cached(self):
        return {k: v for k, v in self.formats.items() if v.cached}

    @property
    def formats_uncached(self):
        return {k: v for k, v in self.formats.items() if not v.cached}


Video = Video
Channel = Channel
VideoFormat = VideoFormat
DownloadResult = DownloadResult
Balance = Balance
