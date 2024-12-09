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


class AppTypeEnum(str, Enum):
    """
    The type of an app.
    """

    """
    allowed enum values
    """
    ACTIVE_DIRECTORY = 'ACTIVE_DIRECTORY'
    AZURE_AD = 'AZURE_AD'
    AWS = 'AWS'
    AWS_SSO = 'AWS_SSO'
    CUSTOM = 'CUSTOM'
    DUO = 'DUO'
    GCP = 'GCP'
    GIT_HUB = 'GIT_HUB'
    GIT_LAB = 'GIT_LAB'
    GOOGLE_GROUPS = 'GOOGLE_GROUPS'
    GOOGLE_WORKSPACE = 'GOOGLE_WORKSPACE'
    LDAP = 'LDAP'
    MARIADB = 'MARIADB'
    MONGO = 'MONGO'
    MONGO_ATLAS = 'MONGO_ATLAS'
    MYSQL = 'MYSQL'
    OKTA_DIRECTORY = 'OKTA_DIRECTORY'
    OPAL = 'OPAL'
    PAGERDUTY = 'PAGERDUTY'
    SALESFORCE = 'SALESFORCE'
    TAILSCALE = 'TAILSCALE'
    TELEPORT = 'TELEPORT'
    WORKDAY = 'WORKDAY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AppTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


