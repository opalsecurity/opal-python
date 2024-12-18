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
from opal_security.models.group_remote_info import GroupRemoteInfo
from opal_security.models.group_type_enum import GroupTypeEnum
from opal_security.models.risk_sensitivity_enum import RiskSensitivityEnum
from typing import Optional, Set
from typing_extensions import Self

class CreateGroupInfo(BaseModel):
    """
    # CreateGroupInfo Object ### Description The `CreateGroupInfo` object is used to store creation info for a group.  ### Usage Example Use in the `POST Groups` endpoint.
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the remote group.")
    description: Optional[StrictStr] = Field(default=None, description="A description of the remote group.")
    group_type: GroupTypeEnum
    app_id: StrictStr = Field(description="The ID of the app for the group.")
    remote_info: Optional[GroupRemoteInfo] = None
    remote_group_id: Optional[StrictStr] = Field(default=None, description="Deprecated - use remote_info instead. The ID of the group on the remote system. Include only for items linked to remote systems. See [this guide](https://docs.opal.dev/reference/end-system-objects) for details on how to specify this field.")
    metadata: Optional[StrictStr] = Field(default=None, description="Deprecated - use remote_info instead.  JSON metadata about the remote group. Include only for items linked to remote systems. See [this guide](https://docs.opal.dev/reference/end-system-objects) for details on how to specify this field. The required format is dependent on group_type and should have the following schema: <style type=\"text/css\"> code {max-height:300px !important} </style> ```json {   \"$schema\": \"http://json-schema.org/draft-04/schema#\",   \"title\": \"Group Metadata\",   \"properties\": {     \"ad_group\": {       \"properties\": {         \"object_guid\": {           \"type\": \"string\"         }       },       \"required\": [\"object_guid\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"Active Directory Group\"     },     \"duo_group\": {       \"properties\": {         \"group_id\": {           \"type\": \"string\"         }       },       \"required\": [\"group_id\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"Duo Group\"     },     \"git_hub_team\": {       \"properties\": {         \"org_name\": {           \"type\": \"string\"         },         \"team_slug\": {           \"type\": \"string\"         }       },       \"required\": [\"org_name\", \"team_slug\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"GitHub Team\"     },     \"google_groups_group\": {       \"properties\": {         \"group_id\": {           \"type\": \"string\"         }       },       \"required\": [\"group_id\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"Google Groups Group\"     },     \"ldap_group\": {       \"properties\": {         \"group_uid\": {           \"type\": \"string\"         }       },       \"required\": [\"group_uid\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"LDAP Group\"     },     \"okta_directory_group\": {       \"properties\": {         \"group_id\": {           \"type\": \"string\"         }       },       \"required\": [\"group_id\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"Okta Directory Group\"     }   },   \"additionalProperties\": false,   \"minProperties\": 1,   \"maxProperties\": 1,   \"type\": \"object\" } ```")
    custom_request_notification: Optional[Annotated[str, Field(strict=True, max_length=800)]] = Field(default=None, description="Custom request notification sent upon request approval.")
    risk_sensitivity_override: Optional[RiskSensitivityEnum] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["name", "description", "group_type", "app_id", "remote_info", "remote_group_id", "metadata", "custom_request_notification", "risk_sensitivity_override"]

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
        """Create an instance of CreateGroupInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of remote_info
        if self.remote_info:
            _dict['remote_info'] = self.remote_info.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateGroupInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "group_type": obj.get("group_type"),
            "app_id": obj.get("app_id"),
            "remote_info": GroupRemoteInfo.from_dict(obj["remote_info"]) if obj.get("remote_info") is not None else None,
            "remote_group_id": obj.get("remote_group_id"),
            "metadata": obj.get("metadata"),
            "custom_request_notification": obj.get("custom_request_notification"),
            "risk_sensitivity_override": obj.get("risk_sensitivity_override")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


