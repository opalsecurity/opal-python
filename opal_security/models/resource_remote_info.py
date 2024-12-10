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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from opal_security.models.resource_remote_info_aws_account import ResourceRemoteInfoAwsAccount
from opal_security.models.resource_remote_info_aws_ec2_instance import ResourceRemoteInfoAwsEc2Instance
from opal_security.models.resource_remote_info_aws_eks_cluster import ResourceRemoteInfoAwsEksCluster
from opal_security.models.resource_remote_info_aws_iam_role import ResourceRemoteInfoAwsIamRole
from opal_security.models.resource_remote_info_aws_permission_set import ResourceRemoteInfoAwsPermissionSet
from opal_security.models.resource_remote_info_aws_rds_instance import ResourceRemoteInfoAwsRdsInstance
from opal_security.models.resource_remote_info_gcp_big_query_dataset import ResourceRemoteInfoGcpBigQueryDataset
from opal_security.models.resource_remote_info_gcp_big_query_table import ResourceRemoteInfoGcpBigQueryTable
from opal_security.models.resource_remote_info_gcp_bucket import ResourceRemoteInfoGcpBucket
from opal_security.models.resource_remote_info_gcp_compute_instance import ResourceRemoteInfoGcpComputeInstance
from opal_security.models.resource_remote_info_gcp_folder import ResourceRemoteInfoGcpFolder
from opal_security.models.resource_remote_info_gcp_gke_cluster import ResourceRemoteInfoGcpGkeCluster
from opal_security.models.resource_remote_info_gcp_organization import ResourceRemoteInfoGcpOrganization
from opal_security.models.resource_remote_info_gcp_project import ResourceRemoteInfoGcpProject
from opal_security.models.resource_remote_info_gcp_service_account import ResourceRemoteInfoGcpServiceAccount
from opal_security.models.resource_remote_info_gcp_sql_instance import ResourceRemoteInfoGcpSqlInstance
from opal_security.models.resource_remote_info_github_repo import ResourceRemoteInfoGithubRepo
from opal_security.models.resource_remote_info_gitlab_project import ResourceRemoteInfoGitlabProject
from opal_security.models.resource_remote_info_okta_app import ResourceRemoteInfoOktaApp
from opal_security.models.resource_remote_info_okta_custom_role import ResourceRemoteInfoOktaCustomRole
from opal_security.models.resource_remote_info_okta_standard_role import ResourceRemoteInfoOktaStandardRole
from opal_security.models.resource_remote_info_pagerduty_role import ResourceRemoteInfoPagerdutyRole
from opal_security.models.resource_remote_info_salesforce_permission_set import ResourceRemoteInfoSalesforcePermissionSet
from opal_security.models.resource_remote_info_salesforce_profile import ResourceRemoteInfoSalesforceProfile
from opal_security.models.resource_remote_info_salesforce_role import ResourceRemoteInfoSalesforceRole
from opal_security.models.resource_remote_info_teleport_role import ResourceRemoteInfoTeleportRole
from typing import Optional, Set
from typing_extensions import Self

class ResourceRemoteInfo(BaseModel):
    """
    Information that defines the remote resource. This replaces the deprecated remote_id and metadata fields.
    """ # noqa: E501
    aws_account: Optional[ResourceRemoteInfoAwsAccount] = None
    aws_permission_set: Optional[ResourceRemoteInfoAwsPermissionSet] = None
    aws_iam_role: Optional[ResourceRemoteInfoAwsIamRole] = None
    aws_ec2_instance: Optional[ResourceRemoteInfoAwsEc2Instance] = None
    aws_rds_instance: Optional[ResourceRemoteInfoAwsRdsInstance] = None
    aws_eks_cluster: Optional[ResourceRemoteInfoAwsEksCluster] = None
    gcp_organization: Optional[ResourceRemoteInfoGcpOrganization] = None
    gcp_bucket: Optional[ResourceRemoteInfoGcpBucket] = None
    gcp_compute_instance: Optional[ResourceRemoteInfoGcpComputeInstance] = None
    gcp_big_query_dataset: Optional[ResourceRemoteInfoGcpBigQueryDataset] = None
    gcp_big_query_table: Optional[ResourceRemoteInfoGcpBigQueryTable] = None
    gcp_folder: Optional[ResourceRemoteInfoGcpFolder] = None
    gcp_gke_cluster: Optional[ResourceRemoteInfoGcpGkeCluster] = None
    gcp_project: Optional[ResourceRemoteInfoGcpProject] = None
    gcp_sql_instance: Optional[ResourceRemoteInfoGcpSqlInstance] = None
    gcp_service_account: Optional[ResourceRemoteInfoGcpServiceAccount] = None
    github_repo: Optional[ResourceRemoteInfoGithubRepo] = None
    gitlab_project: Optional[ResourceRemoteInfoGitlabProject] = None
    okta_app: Optional[ResourceRemoteInfoOktaApp] = None
    okta_standard_role: Optional[ResourceRemoteInfoOktaStandardRole] = None
    okta_custom_role: Optional[ResourceRemoteInfoOktaCustomRole] = None
    pagerduty_role: Optional[ResourceRemoteInfoPagerdutyRole] = None
    salesforce_permission_set: Optional[ResourceRemoteInfoSalesforcePermissionSet] = None
    salesforce_profile: Optional[ResourceRemoteInfoSalesforceProfile] = None
    salesforce_role: Optional[ResourceRemoteInfoSalesforceRole] = None
    teleport_role: Optional[ResourceRemoteInfoTeleportRole] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["aws_account", "aws_permission_set", "aws_iam_role", "aws_ec2_instance", "aws_rds_instance", "aws_eks_cluster", "gcp_organization", "gcp_bucket", "gcp_compute_instance", "gcp_big_query_dataset", "gcp_big_query_table", "gcp_folder", "gcp_gke_cluster", "gcp_project", "gcp_sql_instance", "gcp_service_account", "github_repo", "gitlab_project", "okta_app", "okta_standard_role", "okta_custom_role", "pagerduty_role", "salesforce_permission_set", "salesforce_profile", "salesforce_role", "teleport_role"]

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
        """Create an instance of ResourceRemoteInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aws_account
        if self.aws_account:
            _dict['aws_account'] = self.aws_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_permission_set
        if self.aws_permission_set:
            _dict['aws_permission_set'] = self.aws_permission_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_iam_role
        if self.aws_iam_role:
            _dict['aws_iam_role'] = self.aws_iam_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_ec2_instance
        if self.aws_ec2_instance:
            _dict['aws_ec2_instance'] = self.aws_ec2_instance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_rds_instance
        if self.aws_rds_instance:
            _dict['aws_rds_instance'] = self.aws_rds_instance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_eks_cluster
        if self.aws_eks_cluster:
            _dict['aws_eks_cluster'] = self.aws_eks_cluster.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_organization
        if self.gcp_organization:
            _dict['gcp_organization'] = self.gcp_organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_bucket
        if self.gcp_bucket:
            _dict['gcp_bucket'] = self.gcp_bucket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_compute_instance
        if self.gcp_compute_instance:
            _dict['gcp_compute_instance'] = self.gcp_compute_instance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_big_query_dataset
        if self.gcp_big_query_dataset:
            _dict['gcp_big_query_dataset'] = self.gcp_big_query_dataset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_big_query_table
        if self.gcp_big_query_table:
            _dict['gcp_big_query_table'] = self.gcp_big_query_table.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_folder
        if self.gcp_folder:
            _dict['gcp_folder'] = self.gcp_folder.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_gke_cluster
        if self.gcp_gke_cluster:
            _dict['gcp_gke_cluster'] = self.gcp_gke_cluster.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_project
        if self.gcp_project:
            _dict['gcp_project'] = self.gcp_project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_sql_instance
        if self.gcp_sql_instance:
            _dict['gcp_sql_instance'] = self.gcp_sql_instance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_service_account
        if self.gcp_service_account:
            _dict['gcp_service_account'] = self.gcp_service_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of github_repo
        if self.github_repo:
            _dict['github_repo'] = self.github_repo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gitlab_project
        if self.gitlab_project:
            _dict['gitlab_project'] = self.gitlab_project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of okta_app
        if self.okta_app:
            _dict['okta_app'] = self.okta_app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of okta_standard_role
        if self.okta_standard_role:
            _dict['okta_standard_role'] = self.okta_standard_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of okta_custom_role
        if self.okta_custom_role:
            _dict['okta_custom_role'] = self.okta_custom_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pagerduty_role
        if self.pagerduty_role:
            _dict['pagerduty_role'] = self.pagerduty_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of salesforce_permission_set
        if self.salesforce_permission_set:
            _dict['salesforce_permission_set'] = self.salesforce_permission_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of salesforce_profile
        if self.salesforce_profile:
            _dict['salesforce_profile'] = self.salesforce_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of salesforce_role
        if self.salesforce_role:
            _dict['salesforce_role'] = self.salesforce_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of teleport_role
        if self.teleport_role:
            _dict['teleport_role'] = self.teleport_role.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResourceRemoteInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aws_account": ResourceRemoteInfoAwsAccount.from_dict(obj["aws_account"]) if obj.get("aws_account") is not None else None,
            "aws_permission_set": ResourceRemoteInfoAwsPermissionSet.from_dict(obj["aws_permission_set"]) if obj.get("aws_permission_set") is not None else None,
            "aws_iam_role": ResourceRemoteInfoAwsIamRole.from_dict(obj["aws_iam_role"]) if obj.get("aws_iam_role") is not None else None,
            "aws_ec2_instance": ResourceRemoteInfoAwsEc2Instance.from_dict(obj["aws_ec2_instance"]) if obj.get("aws_ec2_instance") is not None else None,
            "aws_rds_instance": ResourceRemoteInfoAwsRdsInstance.from_dict(obj["aws_rds_instance"]) if obj.get("aws_rds_instance") is not None else None,
            "aws_eks_cluster": ResourceRemoteInfoAwsEksCluster.from_dict(obj["aws_eks_cluster"]) if obj.get("aws_eks_cluster") is not None else None,
            "gcp_organization": ResourceRemoteInfoGcpOrganization.from_dict(obj["gcp_organization"]) if obj.get("gcp_organization") is not None else None,
            "gcp_bucket": ResourceRemoteInfoGcpBucket.from_dict(obj["gcp_bucket"]) if obj.get("gcp_bucket") is not None else None,
            "gcp_compute_instance": ResourceRemoteInfoGcpComputeInstance.from_dict(obj["gcp_compute_instance"]) if obj.get("gcp_compute_instance") is not None else None,
            "gcp_big_query_dataset": ResourceRemoteInfoGcpBigQueryDataset.from_dict(obj["gcp_big_query_dataset"]) if obj.get("gcp_big_query_dataset") is not None else None,
            "gcp_big_query_table": ResourceRemoteInfoGcpBigQueryTable.from_dict(obj["gcp_big_query_table"]) if obj.get("gcp_big_query_table") is not None else None,
            "gcp_folder": ResourceRemoteInfoGcpFolder.from_dict(obj["gcp_folder"]) if obj.get("gcp_folder") is not None else None,
            "gcp_gke_cluster": ResourceRemoteInfoGcpGkeCluster.from_dict(obj["gcp_gke_cluster"]) if obj.get("gcp_gke_cluster") is not None else None,
            "gcp_project": ResourceRemoteInfoGcpProject.from_dict(obj["gcp_project"]) if obj.get("gcp_project") is not None else None,
            "gcp_sql_instance": ResourceRemoteInfoGcpSqlInstance.from_dict(obj["gcp_sql_instance"]) if obj.get("gcp_sql_instance") is not None else None,
            "gcp_service_account": ResourceRemoteInfoGcpServiceAccount.from_dict(obj["gcp_service_account"]) if obj.get("gcp_service_account") is not None else None,
            "github_repo": ResourceRemoteInfoGithubRepo.from_dict(obj["github_repo"]) if obj.get("github_repo") is not None else None,
            "gitlab_project": ResourceRemoteInfoGitlabProject.from_dict(obj["gitlab_project"]) if obj.get("gitlab_project") is not None else None,
            "okta_app": ResourceRemoteInfoOktaApp.from_dict(obj["okta_app"]) if obj.get("okta_app") is not None else None,
            "okta_standard_role": ResourceRemoteInfoOktaStandardRole.from_dict(obj["okta_standard_role"]) if obj.get("okta_standard_role") is not None else None,
            "okta_custom_role": ResourceRemoteInfoOktaCustomRole.from_dict(obj["okta_custom_role"]) if obj.get("okta_custom_role") is not None else None,
            "pagerduty_role": ResourceRemoteInfoPagerdutyRole.from_dict(obj["pagerduty_role"]) if obj.get("pagerduty_role") is not None else None,
            "salesforce_permission_set": ResourceRemoteInfoSalesforcePermissionSet.from_dict(obj["salesforce_permission_set"]) if obj.get("salesforce_permission_set") is not None else None,
            "salesforce_profile": ResourceRemoteInfoSalesforceProfile.from_dict(obj["salesforce_profile"]) if obj.get("salesforce_profile") is not None else None,
            "salesforce_role": ResourceRemoteInfoSalesforceRole.from_dict(obj["salesforce_role"]) if obj.get("salesforce_role") is not None else None,
            "teleport_role": ResourceRemoteInfoTeleportRole.from_dict(obj["teleport_role"]) if obj.get("teleport_role") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


