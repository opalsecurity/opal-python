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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opal.models.request_custom_field_response import RequestCustomFieldResponse
from opal.models.request_status_enum import RequestStatusEnum
from opal.models.requested_item import RequestedItem
from typing import Optional, Set
from typing_extensions import Self

class Request(BaseModel):
    """
    # Request Object ### Description The `Request` object is used to represent a request.  ### Usage Example Returned from the `GET Requests` endpoint.
    """ # noqa: E501
    id: StrictStr = Field(description="The unique identifier of the request.")
    created_at: datetime = Field(description="The date and time the request was created.")
    updated_at: datetime = Field(description="The date and time the request was last updated.")
    requester_id: StrictStr = Field(description="The unique identifier of the user who created the request.")
    target_user_id: StrictStr = Field(description="The unique identifier of the user who is the target of the request.")
    status: RequestStatusEnum
    reason: StrictStr = Field(description="The reason for the request.")
    duration_minutes: Optional[StrictInt] = Field(default=None, description="The duration of the request in minutes.")
    requested_items_list: Optional[List[RequestedItem]] = Field(default=None, description="The list of targets for the request.")
    custom_fields_responses: Optional[List[RequestCustomFieldResponse]] = Field(default=None, description="The responses given to the custom fields associated to the request")
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "requester_id", "target_user_id", "status", "reason", "duration_minutes", "requested_items_list", "custom_fields_responses"]

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
        """Create an instance of Request from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in requested_items_list (list)
        _items = []
        if self.requested_items_list:
            for _item in self.requested_items_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requested_items_list'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields_responses (list)
        _items = []
        if self.custom_fields_responses:
            for _item in self.custom_fields_responses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['custom_fields_responses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "requester_id": obj.get("requester_id"),
            "target_user_id": obj.get("target_user_id"),
            "status": obj.get("status"),
            "reason": obj.get("reason"),
            "duration_minutes": obj.get("duration_minutes"),
            "requested_items_list": [RequestedItem.from_dict(_item) for _item in obj["requested_items_list"]] if obj.get("requested_items_list") is not None else None,
            "custom_fields_responses": [RequestCustomFieldResponse.from_dict(_item) for _item in obj["custom_fields_responses"]] if obj.get("custom_fields_responses") is not None else None
        })
        return _obj

