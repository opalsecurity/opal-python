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

from datetime import datetime
from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from opal.models.resource_access_level import ResourceAccessLevel
from typing import Optional, Set
from typing_extensions import Self

class Session(BaseModel):
    """
    # Session Object ### Description The `Session` object is used to represent an access session. Some resources can be accessed temporarily via a time-bounded session.  ### Usage Example Fetch from the `LIST Sessions` endpoint.
    """ # noqa: E501
    connection_id: StrictStr = Field(description="The ID of the connection.")
    user_id: StrictStr = Field(description="The ID of the user.")
    resource_id: StrictStr = Field(description="The ID of the resource.")
    access_level: ResourceAccessLevel
    expiration_date: datetime = Field(description="The day and time the user's access will expire.")
    __properties: ClassVar[List[str]] = ["connection_id", "user_id", "resource_id", "access_level", "expiration_date"]

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
        """Create an instance of Session from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_level
        if self.access_level:
            _dict['access_level'] = self.access_level.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Session from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connection_id": obj.get("connection_id"),
            "user_id": obj.get("user_id"),
            "resource_id": obj.get("resource_id"),
            "access_level": ResourceAccessLevel.from_dict(obj["access_level"]) if obj.get("access_level") is not None else None,
            "expiration_date": obj.get("expiration_date")
        })
        return _obj


