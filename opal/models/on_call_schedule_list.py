# coding: utf-8

"""
    Opal API

    Your Home For Developer Resources.

    The version of the OpenAPI document: 1.0
    Contact: hello@opal.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel
from typing import Any, ClassVar, Dict, List
from opal.models.on_call_schedule import OnCallSchedule
from typing import Optional, Set
from typing_extensions import Self

class OnCallScheduleList(BaseModel):
    """
    OnCallScheduleList
    """ # noqa: E501
    on_call_schedules: List[OnCallSchedule]
    __properties: ClassVar[List[str]] = ["on_call_schedules"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OnCallScheduleList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in on_call_schedules (list)
        _items = []
        if self.on_call_schedules:
            for _item in self.on_call_schedules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['on_call_schedules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OnCallScheduleList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "on_call_schedules": [OnCallSchedule.from_dict(_item) for _item in obj["on_call_schedules"]] if obj.get("on_call_schedules") is not None else None
        })
        return _obj

