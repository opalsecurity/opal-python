# coding: utf-8

"""
    Opal API

    The Opal API is a RESTful API that allows you to interact with the Opal Security platform programmatically.

    The version of the OpenAPI document: 1.0
    Contact: hello@opal.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opal_security.models.group_remote_info_snowflake_role import GroupRemoteInfoSnowflakeRole

class TestGroupRemoteInfoSnowflakeRole(unittest.TestCase):
    """GroupRemoteInfoSnowflakeRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupRemoteInfoSnowflakeRole:
        """Test GroupRemoteInfoSnowflakeRole
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupRemoteInfoSnowflakeRole`
        """
        model = GroupRemoteInfoSnowflakeRole()
        if include_optional:
            return GroupRemoteInfoSnowflakeRole(
                role_id = '01fa7402-01d8-103b-8deb-5f3a0ab7884'
            )
        else:
            return GroupRemoteInfoSnowflakeRole(
                role_id = '01fa7402-01d8-103b-8deb-5f3a0ab7884',
        )
        """

    def testGroupRemoteInfoSnowflakeRole(self):
        """Test GroupRemoteInfoSnowflakeRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
