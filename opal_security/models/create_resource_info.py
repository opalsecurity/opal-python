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
from opal_security.models.resource_remote_info import ResourceRemoteInfo
from opal_security.models.resource_type_enum import ResourceTypeEnum
from opal_security.models.risk_sensitivity_enum import RiskSensitivityEnum
from typing import Optional, Set
from typing_extensions import Self

class CreateResourceInfo(BaseModel):
    """
    # CreateResourceInfo Object ### Description The `CreateResourceInfo` object is used to store creation info for a resource.  ### Usage Example Use in the `POST Resources` endpoint.
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the remote resource.")
    description: Optional[StrictStr] = Field(default=None, description="A description of the remote resource.")
    resource_type: ResourceTypeEnum
    app_id: StrictStr = Field(description="The ID of the app for the resource.")
    remote_info: Optional[ResourceRemoteInfo] = None
    remote_resource_id: Optional[StrictStr] = Field(default=None, description="Deprecated - use remote_info instead. The ID of the resource on the remote system. Include only for items linked to remote systems. See [this guide](https://docs.opal.dev/reference/end-system-objects) for details on how to specify this field.")
    metadata: Optional[StrictStr] = Field(default=None, description="Deprecated - use remote_info instead.  JSON metadata about the remote resource. Include only for items linked to remote systems. See [this guide](https://docs.opal.dev/reference/end-system-objects) for details on how to specify this field. The required format is dependent on resource_type and should have the following schema: <style type=\"text/css\"> code {max-height:300px !important} </style> ```json {   \"$schema\": \"http://json-schema.org/draft-04/schema#\",   \"title\": \"Resource Metadata\",   \"properties\": {     \"aws_ec2_instance\": {       \"properties\": {         \"instance_id\": {           \"type\": \"string\"         },         \"region\": {           \"type\": \"string\"         }       },       \"required\": [\"instance_id\", \"region\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"AWS EC2 Instance\"     },     \"aws_eks_cluster\": {       \"properties\": {         \"cluster_name\": {           \"type\": \"string\"         },         \"cluster_region\": {           \"type\": \"string\"         },         \"cluster_arn\": {           \"type\": \"string\"         }       },       \"required\": [\"cluster_name\", \"cluster_region\", \"cluster_arn\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"AWS EKS Cluster\"     },     \"aws_rds_instance\": {       \"properties\": {         \"instance_id\": {           \"type\": \"string\"         },         \"engine\": {           \"type\": \"string\"         },         \"region\": {           \"type\": \"string\"         },         \"resource_id\": {           \"type\": \"string\"         },         \"database_name\": {           \"type\": \"string\"         }       },       \"required\": [         \"instance_id\",         \"engine\",         \"region\",         \"resource_id\",         \"database_name\"       ],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"AWS RDS Instance\"     },     \"aws_role\": {       \"properties\": {         \"arn\": {           \"type\": \"string\"         },         \"name\": {           \"type\": \"string\"         }       },       \"required\": [\"arn\", \"name\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"AWS Role\"     },     \"gcp_bucket\": {       \"properties\": {         \"bucket_id\": {           \"type\": \"string\"         }       },       \"required\": [\"bucket_id\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"GCP Bucket\"     },     \"gcp_compute_instance\": {       \"properties\": {         \"instance_id\": {           \"type\": \"string\"         },         \"project_id\": {           \"type\": \"string\"         },         \"zone\": {           \"type\": \"string\"         }       },       \"required\": [\"instance_id\", \"project_id\", \"zone\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"GCP Compute Instance\"     },     \"gcp_folder\": {       \"properties\": {         \"folder_id\": {           \"type\": \"string\"         }       },       \"required\": [\"folder_id\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"GCP Folder\"     },     \"gcp_gke_cluster\": {       \"properties\": {         \"cluster_name\": {           \"type\": \"string\"         }       },       \"required\": [\"cluster_name\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"GCP GKE Cluster\"     },     \"gcp_project\": {       \"properties\": {         \"project_id\": {           \"type\": \"string\"         }       },       \"required\": [\"project_id\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"GCP Project\"     },     \"gcp_sql_instance\": {       \"properties\": {         \"instance_id\": {           \"type\": \"string\"         },         \"project_id\": {           \"type\": \"string\"         }       },       \"required\": [\"instance_id\", \"project_id\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"GCP SQL Instance\"     },     \"git_hub_repo\": {       \"properties\": {         \"org_name\": {           \"type\": \"string\"         },         \"repo_name\": {           \"type\": \"string\"         }       },       \"required\": [\"org_name\", \"repo_name\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"GitHub Repo\"     },     \"okta_directory_app\": {       \"properties\": {         \"app_id\": {           \"type\": \"string\"         },         \"logo_url\": {           \"type\": \"string\"         }       },       \"required\": [\"app_id\", \"logo_url\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"Okta Directory App\"     },     \"okta_directory_role\": {       \"properties\": {         \"role_type\": {           \"type\": \"string\"         },         \"role_id\": {           \"type\": \"string\"         }       },       \"required\": [\"role_type\", \"role_id\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"Okta Directory Role\"     },     \"salesforce_profile\": {       \"properties\": {         \"user_license\": {           \"type\": \"string\"         }       },       \"required\": [\"user_license\"],       \"additionalProperties\": false,       \"type\": \"object\",       \"title\": \"Salesforce Profile\"     }   },   \"additionalProperties\": false,   \"minProperties\": 1,   \"maxProperties\": 1,   \"type\": \"object\" } ```")
    custom_request_notification: Optional[Annotated[str, Field(strict=True, max_length=800)]] = Field(default=None, description="Custom request notification sent upon request approval.")
    risk_sensitivity_override: Optional[RiskSensitivityEnum] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["name", "description", "resource_type", "app_id", "remote_info", "remote_resource_id", "metadata", "custom_request_notification", "risk_sensitivity_override"]

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
        """Create an instance of CreateResourceInfo from a JSON string"""
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
        """Create an instance of CreateResourceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "resource_type": obj.get("resource_type"),
            "app_id": obj.get("app_id"),
            "remote_info": ResourceRemoteInfo.from_dict(obj["remote_info"]) if obj.get("remote_info") is not None else None,
            "remote_resource_id": obj.get("remote_resource_id"),
            "metadata": obj.get("metadata"),
            "custom_request_notification": obj.get("custom_request_notification"),
            "risk_sensitivity_override": obj.get("risk_sensitivity_override")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


