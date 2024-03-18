# coding: utf-8

"""
    Opal API

    Your Home For Developer Resources.

    The version of the OpenAPI document: 1.0
    Contact: hello@opal.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opal.models.condition import Condition

class TestCondition(unittest.TestCase):
    """Condition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Condition:
        """Test Condition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Condition`
        """
        model = Condition()
        if include_optional:
            return Condition(
                group_ids = ["1b978423-db0a-4037-a4cf-f79c60cb67b3"],
                role_remote_ids = ["arn:aws:iam::590304332660:role/AdministratorAccess"]
            )
        else:
            return Condition(
        )
        """

    def testCondition(self):
        """Test Condition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
