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
from typing_extensions import Annotated
from opal_security.models.create_request_configuration_info_list import CreateRequestConfigurationInfoList
from opal_security.models.request_configuration import RequestConfiguration
from opal_security.models.risk_sensitivity_enum import RiskSensitivityEnum
from opal_security.models.ticket_propagation_configuration import TicketPropagationConfiguration
from typing import Optional, Set
from typing_extensions import Self

class UpdateResourceInfo(BaseModel):
    """
    # UpdateResourceInfo Object ### Description The `UpdateResourceInfo` object is used as an input to the UpdateResource API.
    """ # noqa: E501
    resource_id: StrictStr = Field(description="The ID of the resource.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the resource.")
    description: Optional[StrictStr] = Field(default=None, description="A description of the resource.")
    admin_owner_id: Optional[StrictStr] = Field(default=None, description="The ID of the owner of the resource.")
    max_duration: Optional[StrictInt] = Field(default=None, description="The maximum duration for which the resource can be requested (in minutes). Use -1 to set to indefinite. Deprecated in favor of `request_configurations`.")
    recommended_duration: Optional[StrictInt] = Field(default=None, description="The recommended duration for which the resource should be requested (in minutes). Will be the default value in a request. Use -1 to set to indefinite and 0 to unset. Deprecated in favor of `request_configurations`.")
    require_manager_approval: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not access requests to the resource require manager approval.")
    require_support_ticket: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not access requests to the resource require an access ticket. Deprecated in favor of `request_configurations`.")
    folder_id: Optional[StrictStr] = Field(default=None, description="The ID of the folder that the resource is located in.")
    require_mfa_to_approve: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to require MFA for reviewers to approve requests for this resource.")
    require_mfa_to_request: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to require MFA for requesting access to this resource. Deprecated in favor of `request_configurations`.")
    require_mfa_to_connect: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to require MFA to connect to this resource.")
    auto_approval: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to automatically approve requests to this resource. Deprecated in favor of `request_configurations`.")
    ticket_propagation: Optional[TicketPropagationConfiguration] = None
    custom_request_notification: Optional[Annotated[str, Field(strict=True, max_length=800)]] = Field(default=None, description="Custom request notification sent upon request approval.")
    risk_sensitivity_override: Optional[RiskSensitivityEnum] = None
    configuration_template_id: Optional[StrictStr] = Field(default=None, description="The ID of the associated configuration template.")
    request_template_id: Optional[StrictStr] = Field(default=None, description="The ID of the associated request template. Deprecated in favor of `request_configurations`.")
    is_requestable: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to allow access requests to this resource. Deprecated in favor of `request_configurations`.")
    request_configurations: Optional[List[RequestConfiguration]] = Field(default=None, description="A list of configurations for requests to this resource. If not provided, the default request configuration will be used.")
    request_configuration_list: Optional[CreateRequestConfigurationInfoList] = Field(default=None, description="A list of configurations for requests to this resource. If not provided, the default request configuration will be used. Deprecated in favor of `request_configurations`.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["resource_id", "name", "description", "admin_owner_id", "max_duration", "recommended_duration", "require_manager_approval", "require_support_ticket", "folder_id", "require_mfa_to_approve", "require_mfa_to_request", "require_mfa_to_connect", "auto_approval", "ticket_propagation", "custom_request_notification", "risk_sensitivity_override", "configuration_template_id", "request_template_id", "is_requestable", "request_configurations", "request_configuration_list"]

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
        """Create an instance of UpdateResourceInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ticket_propagation
        if self.ticket_propagation:
            _dict['ticket_propagation'] = self.ticket_propagation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in request_configurations (list)
        _items = []
        if self.request_configurations:
            for _item_request_configurations in self.request_configurations:
                if _item_request_configurations:
                    _items.append(_item_request_configurations.to_dict())
            _dict['request_configurations'] = _items
        # override the default output from pydantic by calling `to_dict()` of request_configuration_list
        if self.request_configuration_list:
            _dict['request_configuration_list'] = self.request_configuration_list.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateResourceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resource_id": obj.get("resource_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "admin_owner_id": obj.get("admin_owner_id"),
            "max_duration": obj.get("max_duration"),
            "recommended_duration": obj.get("recommended_duration"),
            "require_manager_approval": obj.get("require_manager_approval"),
            "require_support_ticket": obj.get("require_support_ticket"),
            "folder_id": obj.get("folder_id"),
            "require_mfa_to_approve": obj.get("require_mfa_to_approve"),
            "require_mfa_to_request": obj.get("require_mfa_to_request"),
            "require_mfa_to_connect": obj.get("require_mfa_to_connect"),
            "auto_approval": obj.get("auto_approval"),
            "ticket_propagation": TicketPropagationConfiguration.from_dict(obj["ticket_propagation"]) if obj.get("ticket_propagation") is not None else None,
            "custom_request_notification": obj.get("custom_request_notification"),
            "risk_sensitivity_override": obj.get("risk_sensitivity_override"),
            "configuration_template_id": obj.get("configuration_template_id"),
            "request_template_id": obj.get("request_template_id"),
            "is_requestable": obj.get("is_requestable"),
            "request_configurations": [RequestConfiguration.from_dict(_item) for _item in obj["request_configurations"]] if obj.get("request_configurations") is not None else None,
            "request_configuration_list": CreateRequestConfigurationInfoList.from_dict(obj["request_configuration_list"]) if obj.get("request_configuration_list") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


