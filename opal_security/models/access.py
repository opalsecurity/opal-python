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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opal_security.models.entity_type_enum import EntityTypeEnum
from opal_security.models.resource_access_level import ResourceAccessLevel
from typing import Optional, Set
from typing_extensions import Self

class Access(BaseModel):
    """
    # Access Object ### Description The `Access` object is used to represent a principal's access to an entity, either directly or inherited.  ### Usage Example Fetch from the `LIST ResourceNonHumanIdentities` endpoint.
    """ # noqa: E501
    principal_id: StrictStr = Field(description="The ID of the principal with access.")
    principal_type: EntityTypeEnum
    entity_id: StrictStr = Field(description="The ID of the entity being accessed.")
    entity_type: EntityTypeEnum
    access_level: Optional[ResourceAccessLevel] = None
    expiration_date: Optional[datetime] = Field(default=None, description="The day and time the principal's access will expire.")
    has_direct_access: StrictBool = Field(description="The principal has direct access to this entity (vs. inherited access).")
    num_access_paths: StrictInt = Field(description="The number of ways in which the principal has access to this entity (directly and inherited).")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["principal_id", "principal_type", "entity_id", "entity_type", "access_level", "expiration_date", "has_direct_access", "num_access_paths"]

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
        """Create an instance of Access from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of access_level
        if self.access_level:
            _dict['access_level'] = self.access_level.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Access from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "principal_id": obj.get("principal_id"),
            "principal_type": obj.get("principal_type"),
            "entity_id": obj.get("entity_id"),
            "entity_type": obj.get("entity_type"),
            "access_level": ResourceAccessLevel.from_dict(obj["access_level"]) if obj.get("access_level") is not None else None,
            "expiration_date": obj.get("expiration_date"),
            "has_direct_access": obj.get("has_direct_access"),
            "num_access_paths": obj.get("num_access_paths")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


