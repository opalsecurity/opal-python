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

from opal.models.group_access_level import GroupAccessLevel

class TestGroupAccessLevel(unittest.TestCase):
    """GroupAccessLevel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupAccessLevel:
        """Test GroupAccessLevel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupAccessLevel`
        """
        model = GroupAccessLevel()
        if include_optional:
            return GroupAccessLevel(
                access_level_name = 'Developer',
                access_level_remote_id = '20'
            )
        else:
            return GroupAccessLevel(
                access_level_name = 'Developer',
                access_level_remote_id = '20',
        )
        """

    def testGroupAccessLevel(self):
        """Test GroupAccessLevel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
