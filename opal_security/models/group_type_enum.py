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
import json
from enum import Enum
from typing_extensions import Self


class GroupTypeEnum(str, Enum):
    """
    The type of the group.
    """

    """
    allowed enum values
    """
    ACTIVE_DIRECTORY_GROUP = 'ACTIVE_DIRECTORY_GROUP'
    AWS_SSO_GROUP = 'AWS_SSO_GROUP'
    DATABRICKS_ACCOUNT_GROUP = 'DATABRICKS_ACCOUNT_GROUP'
    DUO_GROUP = 'DUO_GROUP'
    GIT_HUB_TEAM = 'GIT_HUB_TEAM'
    GIT_LAB_GROUP = 'GIT_LAB_GROUP'
    GOOGLE_GROUPS_GROUP = 'GOOGLE_GROUPS_GROUP'
    GOOGLE_GROUPS_GKE_GROUP = 'GOOGLE_GROUPS_GKE_GROUP'
    LDAP_GROUP = 'LDAP_GROUP'
    OKTA_GROUP = 'OKTA_GROUP'
    OKTA_GROUP_RULE = 'OKTA_GROUP_RULE'
    TAILSCALE_GROUP = 'TAILSCALE_GROUP'
    OPAL_GROUP = 'OPAL_GROUP'
    OPAL_ACCESS_RULE = 'OPAL_ACCESS_RULE'
    AZURE_AD_SECURITY_GROUP = 'AZURE_AD_SECURITY_GROUP'
    AZURE_AD_MICROSOFT_365_GROUP = 'AZURE_AD_MICROSOFT_365_GROUP'
    CONNECTOR_GROUP = 'CONNECTOR_GROUP'
    SNOWFLAKE_ROLE = 'SNOWFLAKE_ROLE'
    WORKDAY_USER_SECURITY_GROUP = 'WORKDAY_USER_SECURITY_GROUP'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GroupTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


