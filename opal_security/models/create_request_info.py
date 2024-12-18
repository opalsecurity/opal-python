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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from opal_security.models.create_request_info_custom_metadata_inner import CreateRequestInfoCustomMetadataInner
from opal_security.models.create_request_info_groups_inner import CreateRequestInfoGroupsInner
from opal_security.models.create_request_info_resources_inner import CreateRequestInfoResourcesInner
from opal_security.models.create_request_info_support_ticket import CreateRequestInfoSupportTicket
from typing import Optional, Set
from typing_extensions import Self

class CreateRequestInfo(BaseModel):
    """
    All the information needed for creating a request
    """ # noqa: E501
    resources: List[CreateRequestInfoResourcesInner]
    groups: List[CreateRequestInfoGroupsInner]
    target_user_id: Optional[StrictStr] = Field(default=None, description="The ID of the user to be granted access. Should not be specified if target_group_id is specified.")
    target_group_id: Optional[StrictStr] = Field(default=None, description="The ID of the group the request is for.  Should not be specified if target_user_id is specified.")
    reason: StrictStr
    support_ticket: Optional[CreateRequestInfoSupportTicket] = None
    duration_minutes: Annotated[int, Field(strict=True, ge=-1)] = Field(description="The duration of the request in minutes. -1 represents an indefinite duration")
    custom_metadata: Optional[List[CreateRequestInfoCustomMetadataInner]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["resources", "groups", "target_user_id", "target_group_id", "reason", "support_ticket", "duration_minutes", "custom_metadata"]

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
        """Create an instance of CreateRequestInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item_resources in self.resources:
                if _item_resources:
                    _items.append(_item_resources.to_dict())
            _dict['resources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of support_ticket
        if self.support_ticket:
            _dict['support_ticket'] = self.support_ticket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_metadata (list)
        _items = []
        if self.custom_metadata:
            for _item_custom_metadata in self.custom_metadata:
                if _item_custom_metadata:
                    _items.append(_item_custom_metadata.to_dict())
            _dict['custom_metadata'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resources": [CreateRequestInfoResourcesInner.from_dict(_item) for _item in obj["resources"]] if obj.get("resources") is not None else None,
            "groups": [CreateRequestInfoGroupsInner.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "target_user_id": obj.get("target_user_id"),
            "target_group_id": obj.get("target_group_id"),
            "reason": obj.get("reason"),
            "support_ticket": CreateRequestInfoSupportTicket.from_dict(obj["support_ticket"]) if obj.get("support_ticket") is not None else None,
            "duration_minutes": obj.get("duration_minutes"),
            "custom_metadata": [CreateRequestInfoCustomMetadataInner.from_dict(_item) for _item in obj["custom_metadata"]] if obj.get("custom_metadata") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


