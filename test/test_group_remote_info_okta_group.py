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

from opal_security.models.group_remote_info_okta_group import GroupRemoteInfoOktaGroup

class TestGroupRemoteInfoOktaGroup(unittest.TestCase):
    """GroupRemoteInfoOktaGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupRemoteInfoOktaGroup:
        """Test GroupRemoteInfoOktaGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupRemoteInfoOktaGroup`
        """
        model = GroupRemoteInfoOktaGroup()
        if include_optional:
            return GroupRemoteInfoOktaGroup(
                group_id = '00gjs33pe8rtmRrp3rd6'
            )
        else:
            return GroupRemoteInfoOktaGroup(
                group_id = '00gjs33pe8rtmRrp3rd6',
        )
        """

    def testGroupRemoteInfoOktaGroup(self):
        """Test GroupRemoteInfoOktaGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
