"""
    Opal API

    Your Home For Developer Resources.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@opal.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import opal
from opal.model.resource_type_enum import ResourceTypeEnum
from opal.model.visibility_enum import VisibilityEnum
globals()['ResourceTypeEnum'] = ResourceTypeEnum
globals()['VisibilityEnum'] = VisibilityEnum
from opal.model.resource import Resource


class TestResource(unittest.TestCase):
    """Resource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResource(self):
        """Test Resource"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Resource()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()