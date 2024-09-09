from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field









T = TypeVar("T", bound="DownloadResult")


@_attrs_define
class DownloadResult:
    """ 
        Attributes:
            status (str): One of: `queued`, `downloading`, `ready`, `failed`
            file_id (str): Telegram's `file_id` used for sending cached files
     """

    status: str
    file_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        file_id = self.file_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "file_id": file_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        file_id = d.pop("file_id", "")

        download_result = cls(
            status=status,
            file_id=file_id,
        )


        download_result.additional_properties = d
        return download_result

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
