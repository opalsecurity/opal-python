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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opal_security.models.app_validation_severity_enum import AppValidationSeverityEnum
from opal_security.models.app_validation_status_enum import AppValidationStatusEnum
from typing import Optional, Set
from typing_extensions import Self

class AppValidation(BaseModel):
    """
    # App validation object ### Description The `AppValidation` object is used to represent a validation check of an apps' configuration and permissions.  ### Usage Example List from the `GET Apps` endpoint.
    """ # noqa: E501
    key: StrictStr = Field(description="The key of the app validation. These are not unique IDs between runs.")
    name: Optional[Any]
    usage_reason: Optional[StrictStr] = Field(default=None, description="The reason for needing the validation.")
    details: Optional[StrictStr] = Field(default=None, description="Extra details regarding the validation. Could be an error message or restrictions on permissions.")
    severity: AppValidationSeverityEnum
    status: AppValidationStatusEnum
    updated_at: datetime = Field(description="The date and time the app validation was last run.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["key", "name", "usage_reason", "details", "severity", "status", "updated_at"]

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
        """Create an instance of AppValidation from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppValidation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "key": obj.get("key"),
            "name": obj.get("name"),
            "usage_reason": obj.get("usage_reason"),
            "details": obj.get("details"),
            "severity": obj.get("severity"),
            "status": obj.get("status"),
            "updated_at": obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


