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


class AppValidationSeverityEnum(str, Enum):
    """
    The severity of an app validation.
    """

    """
    allowed enum values
    """
    CRITICAL = 'CRITICAL'
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AppValidationSeverityEnum from a JSON string"""
        return cls(json.loads(json_str))


