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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opal_security.models.condition import Condition
from opal_security.models.reviewer_stage import ReviewerStage
from typing import Optional, Set
from typing_extensions import Self

class RequestConfiguration(BaseModel):
    """
    # Request Configuration Object ### Description The `RequestConfiguration` object is used to represent a request configuration.  ### Usage Example Returned from the `GET Request Configurations` endpoint.
    """ # noqa: E501
    condition: Optional[Condition] = Field(default=None, description="The condition for the request configuration.")
    allow_requests: StrictBool = Field(description="A bool representing whether or not to allow requests for this resource.")
    auto_approval: StrictBool = Field(description="A bool representing whether or not to automatically approve requests for this resource.")
    require_mfa_to_request: StrictBool = Field(description="A bool representing whether or not to require MFA for requesting access to this resource.")
    max_duration_minutes: Optional[StrictInt] = Field(default=None, description="The maximum duration for which the resource can be requested (in minutes).")
    recommended_duration_minutes: Optional[StrictInt] = Field(default=None, description="The recommended duration for which the resource should be requested (in minutes). -1 represents an indefinite duration.")
    require_support_ticket: StrictBool = Field(description="A bool representing whether or not access requests to the resource require an access ticket.")
    request_template_id: Optional[StrictStr] = Field(default=None, description="The ID of the associated request template.")
    reviewer_stages: Optional[List[ReviewerStage]] = Field(default=None, description="The list of reviewer stages for the request configuration.")
    priority: StrictInt = Field(description="The priority of the request configuration.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["condition", "allow_requests", "auto_approval", "require_mfa_to_request", "max_duration_minutes", "recommended_duration_minutes", "require_support_ticket", "request_template_id", "reviewer_stages", "priority"]

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
        """Create an instance of RequestConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of condition
        if self.condition:
            _dict['condition'] = self.condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reviewer_stages (list)
        _items = []
        if self.reviewer_stages:
            for _item_reviewer_stages in self.reviewer_stages:
                if _item_reviewer_stages:
                    _items.append(_item_reviewer_stages.to_dict())
            _dict['reviewer_stages'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RequestConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "condition": Condition.from_dict(obj["condition"]) if obj.get("condition") is not None else None,
            "allow_requests": obj.get("allow_requests"),
            "auto_approval": obj.get("auto_approval"),
            "require_mfa_to_request": obj.get("require_mfa_to_request"),
            "max_duration_minutes": obj.get("max_duration_minutes"),
            "recommended_duration_minutes": obj.get("recommended_duration_minutes"),
            "require_support_ticket": obj.get("require_support_ticket"),
            "request_template_id": obj.get("request_template_id"),
            "reviewer_stages": [ReviewerStage.from_dict(_item) for _item in obj["reviewer_stages"]] if obj.get("reviewer_stages") is not None else None,
            "priority": obj.get("priority")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


