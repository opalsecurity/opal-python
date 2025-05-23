# coding: utf-8

"""
    Opal API

    The Opal API is a RESTful API that allows you to interact with the Opal Security platform programmatically.

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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Bundle(BaseModel):
    """
    Bundle
    """ # noqa: E501
    bundle_id: Optional[StrictStr] = Field(default=None, description="The ID of the bundle.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the bundle.")
    description: Optional[StrictStr] = Field(default=None, description="The description of the bundle.")
    created_at: Optional[datetime] = Field(default=None, description="The creation timestamp of the bundle, in ISO 8601 format")
    updated_at: Optional[datetime] = Field(default=None, description="The last updated timestamp of the bundle, in ISO 8601 format")
    admin_owner_id: Optional[StrictStr] = Field(default=None, description="The ID of the owner of the bundle.")
    total_num_items: Optional[StrictInt] = Field(default=None, description="The total number of items in the bundle.")
    total_num_resources: Optional[StrictInt] = Field(default=None, description="The total number of resources in the bundle.")
    total_num_groups: Optional[StrictInt] = Field(default=None, description="The total number of groups in the bundle.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["bundle_id", "name", "description", "created_at", "updated_at", "admin_owner_id", "total_num_items", "total_num_resources", "total_num_groups"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Bundle from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "bundle_id",
            "created_at",
            "updated_at",
            "total_num_items",
            "total_num_resources",
            "total_num_groups",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Bundle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bundle_id": obj.get("bundle_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "admin_owner_id": obj.get("admin_owner_id"),
            "total_num_items": obj.get("total_num_items"),
            "total_num_resources": obj.get("total_num_resources"),
            "total_num_groups": obj.get("total_num_groups")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


