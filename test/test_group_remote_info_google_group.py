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

from opal.models.group_remote_info_google_group import GroupRemoteInfoGoogleGroup

class TestGroupRemoteInfoGoogleGroup(unittest.TestCase):
    """GroupRemoteInfoGoogleGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupRemoteInfoGoogleGroup:
        """Test GroupRemoteInfoGoogleGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupRemoteInfoGoogleGroup`
        """
        model = GroupRemoteInfoGoogleGroup()
        if include_optional:
            return GroupRemoteInfoGoogleGroup(
                group_id = '1y6w882181n7sg'
            )
        else:
            return GroupRemoteInfoGoogleGroup(
                group_id = '1y6w882181n7sg',
        )
        """

    def testGroupRemoteInfoGoogleGroup(self):
        """Test GroupRemoteInfoGoogleGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()