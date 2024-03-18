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
import json
from enum import Enum
from typing_extensions import Self


class ResourceUserAccessStatusEnum(str, Enum):
    """
    The status of the user's access to the resource.
    """

    """
    allowed enum values
    """
    AUTHORIZED = 'AUTHORIZED'
    REQUESTED = 'REQUESTED'
    UNAUTHORIZED = 'UNAUTHORIZED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ResourceUserAccessStatusEnum from a JSON string"""
        return cls(json.loads(json_str))

