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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from opal_security.models.ticket_propagation_configuration import TicketPropagationConfiguration
from opal_security.models.visibility_info import VisibilityInfo
from typing import Optional, Set
from typing_extensions import Self

class ConfigurationTemplate(BaseModel):
    """
    # Configuration Template Object ### Description The `ConfigurationTemplate` object is used to represent a configuration template.  ### Usage Example Returned from the `GET Configuration Templates` endpoint.
    """ # noqa: E501
    configuration_template_id: Optional[StrictStr] = Field(default=None, description="The ID of the configuration template.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the configuration template.")
    admin_owner_id: Optional[StrictStr] = Field(default=None, description="The ID of the owner of the configuration template.")
    visibility: Optional[VisibilityInfo] = Field(default=None, description="The visibility info of the configuration template.")
    linked_audit_message_channel_ids: Optional[List[StrictStr]] = Field(default=None, description="The IDs of the audit message channels linked to the configuration template.")
    request_configuration_id: Optional[StrictStr] = Field(default=None, description="The ID of the request configuration linked to the configuration template.")
    member_oncall_schedule_ids: Optional[List[StrictStr]] = Field(default=None, description="The IDs of the on-call schedules linked to the configuration template.")
    break_glass_user_ids: Optional[List[StrictStr]] = Field(default=None, description="The IDs of the break glass users linked to the configuration template.")
    require_mfa_to_approve: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to require MFA for reviewers to approve requests for this configuration template.")
    require_mfa_to_connect: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to require MFA to connect to resources associated with this configuration template.")
    ticket_propagation: Optional[TicketPropagationConfiguration] = None
    custom_request_notification: Optional[Annotated[str, Field(strict=True, max_length=800)]] = Field(default=None, description="Custom request notification sent upon request approval for this configuration template.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["configuration_template_id", "name", "admin_owner_id", "visibility", "linked_audit_message_channel_ids", "request_configuration_id", "member_oncall_schedule_ids", "break_glass_user_ids", "require_mfa_to_approve", "require_mfa_to_connect", "ticket_propagation", "custom_request_notification"]

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
        """Create an instance of ConfigurationTemplate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of visibility
        if self.visibility:
            _dict['visibility'] = self.visibility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ticket_propagation
        if self.ticket_propagation:
            _dict['ticket_propagation'] = self.ticket_propagation.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configuration_template_id": obj.get("configuration_template_id"),
            "name": obj.get("name"),
            "admin_owner_id": obj.get("admin_owner_id"),
            "visibility": VisibilityInfo.from_dict(obj["visibility"]) if obj.get("visibility") is not None else None,
            "linked_audit_message_channel_ids": obj.get("linked_audit_message_channel_ids"),
            "request_configuration_id": obj.get("request_configuration_id"),
            "member_oncall_schedule_ids": obj.get("member_oncall_schedule_ids"),
            "break_glass_user_ids": obj.get("break_glass_user_ids"),
            "require_mfa_to_approve": obj.get("require_mfa_to_approve"),
            "require_mfa_to_connect": obj.get("require_mfa_to_connect"),
            "ticket_propagation": TicketPropagationConfiguration.from_dict(obj["ticket_propagation"]) if obj.get("ticket_propagation") is not None else None,
            "custom_request_notification": obj.get("custom_request_notification")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


