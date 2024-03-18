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
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Tag(BaseModel):
    """
    # Tag Object ### Description The `Tag` object is used to represent a tag.  ### Usage Example Get tags from the `GET Tag` endpoint.
    """ # noqa: E501
    tag_id: StrictStr = Field(description="The ID of the tag.")
    created_at: Optional[datetime] = Field(default=None, description="The date the tag was created.")
    updated_at: Optional[datetime] = Field(default=None, description="The date the tag was last updated.")
    user_creator_id: Optional[StrictStr] = Field(default=None, description="The ID of the user that created the tag.")
    key: Optional[StrictStr] = Field(default=None, description="The key of the tag.")
    value: Optional[StrictStr] = Field(default=None, description="The value of the tag.")
    __properties: ClassVar[List[str]] = ["tag_id", "created_at", "updated_at", "user_creator_id", "key", "value"]

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
        """Create an instance of Tag from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Tag from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tag_id": obj.get("tag_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "user_creator_id": obj.get("user_creator_id"),
            "key": obj.get("key"),
            "value": obj.get("value")
        })
        return _obj

