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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opal_security.models.uar_reviewer_assignment_policy_enum import UARReviewerAssignmentPolicyEnum
from opal_security.models.uar_scope import UARScope
from typing import Optional, Set
from typing_extensions import Self

class UAR(BaseModel):
    """
    A user access review.
    """ # noqa: E501
    uar_id: StrictStr = Field(description="The ID of the UAR.")
    name: StrictStr = Field(description="The name of the UAR.")
    reviewer_assignment_policy: UARReviewerAssignmentPolicyEnum
    send_reviewer_assignment_notification: StrictBool = Field(description="A bool representing whether to send a notification to reviewers when they're assigned a new review. Default is False.")
    deadline: datetime = Field(description="The last day for reviewers to complete their access reviews.")
    time_zone: StrictStr = Field(description="The time zone name (as defined by the IANA Time Zone database) used in the access review deadline and exported audit report. Default is America/Los_Angeles.")
    self_review_allowed: StrictBool = Field(description="A bool representing whether to present a warning when a user is the only reviewer for themself. Default is False.")
    uar_scope: Optional[UARScope] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["uar_id", "name", "reviewer_assignment_policy", "send_reviewer_assignment_notification", "deadline", "time_zone", "self_review_allowed", "uar_scope"]

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
        """Create an instance of UAR from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of uar_scope
        if self.uar_scope:
            _dict['uar_scope'] = self.uar_scope.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UAR from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uar_id": obj.get("uar_id"),
            "name": obj.get("name"),
            "reviewer_assignment_policy": obj.get("reviewer_assignment_policy"),
            "send_reviewer_assignment_notification": obj.get("send_reviewer_assignment_notification"),
            "deadline": obj.get("deadline"),
            "time_zone": obj.get("time_zone"),
            "self_review_allowed": obj.get("self_review_allowed"),
            "uar_scope": UARScope.from_dict(obj["uar_scope"]) if obj.get("uar_scope") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


