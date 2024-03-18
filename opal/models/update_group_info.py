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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opal.models.create_request_configuration_info_list import CreateRequestConfigurationInfoList
from opal.models.request_configuration import RequestConfiguration
from typing import Optional, Set
from typing_extensions import Self

class UpdateGroupInfo(BaseModel):
    """
    # UpdateGroupInfo Object ### Description The `UpdateGroupInfo` object is used as an input to the UpdateGroup API.
    """ # noqa: E501
    group_id: StrictStr = Field(description="The ID of the group.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the group.")
    description: Optional[StrictStr] = Field(default=None, description="A description of the group.")
    admin_owner_id: Optional[StrictStr] = Field(default=None, description="The ID of the owner of the group.")
    max_duration: Optional[StrictInt] = Field(default=None, description="The maximum duration for which the group can be requested (in minutes). Use -1 to set to indefinite. Deprecated in favor of `request_configurations`.")
    recommended_duration: Optional[StrictInt] = Field(default=None, description="The recommended duration for which the group should be requested (in minutes). Will be the default value in a request. Use -1 to set to indefinite and 0 to unset. Deprecated in favor of `request_configurations`.")
    require_manager_approval: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not access requests to the group require manager approval. Deprecated in favor of `request_configurations`.")
    require_support_ticket: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not access requests to the group require an access ticket. Deprecated in favor of `request_configurations`.")
    folder_id: Optional[StrictStr] = Field(default=None, description="The ID of the folder that the group is located in.")
    require_mfa_to_approve: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to require MFA for reviewers to approve requests for this group.")
    require_mfa_to_request: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to require MFA for requesting access to this group. Deprecated in favor of `request_configurations`.")
    auto_approval: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to automatically approve requests to this group. Deprecated in favor of `request_configurations`.")
    configuration_template_id: Optional[StrictStr] = Field(default=None, description="The ID of the associated configuration template.")
    request_template_id: Optional[StrictStr] = Field(default=None, description="The ID of the associated request template. Deprecated in favor of `request_configurations`.")
    is_requestable: Optional[StrictBool] = Field(default=None, description="A bool representing whether or not to allow access requests to this group. Deprecated in favor of `request_configurations`.")
    request_configurations: Optional[List[RequestConfiguration]] = Field(default=None, description="The request configuration list of the configuration template. If not provided, the default request configuration will be used.")
    request_configuration_list: Optional[CreateRequestConfigurationInfoList] = None
    __properties: ClassVar[List[str]] = ["group_id", "name", "description", "admin_owner_id", "max_duration", "recommended_duration", "require_manager_approval", "require_support_ticket", "folder_id", "require_mfa_to_approve", "require_mfa_to_request", "auto_approval", "configuration_template_id", "request_template_id", "is_requestable", "request_configurations", "request_configuration_list"]

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
        """Create an instance of UpdateGroupInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in request_configurations (list)
        _items = []
        if self.request_configurations:
            for _item in self.request_configurations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['request_configurations'] = _items
        # override the default output from pydantic by calling `to_dict()` of request_configuration_list
        if self.request_configuration_list:
            _dict['request_configuration_list'] = self.request_configuration_list.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateGroupInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "group_id": obj.get("group_id"),
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
            "auto_approval": obj.get("auto_approval"),
            "configuration_template_id": obj.get("configuration_template_id"),
            "request_template_id": obj.get("request_template_id"),
            "is_requestable": obj.get("is_requestable"),
            "request_configurations": [RequestConfiguration.from_dict(_item) for _item in obj["request_configurations"]] if obj.get("request_configurations") is not None else None,
            "request_configuration_list": CreateRequestConfigurationInfoList.from_dict(obj["request_configuration_list"]) if obj.get("request_configuration_list") is not None else None
        })
        return _obj


