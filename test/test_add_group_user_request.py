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

from opal_security.models.add_group_user_request import AddGroupUserRequest

class TestAddGroupUserRequest(unittest.TestCase):
    """AddGroupUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddGroupUserRequest:
        """Test AddGroupUserRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddGroupUserRequest`
        """
        model = AddGroupUserRequest()
        if include_optional:
            return AddGroupUserRequest(
                duration_minutes = 60,
                access_level_remote_id = 'arn:aws:iam::590304332660:role/AdministratorAccess'
            )
        else:
            return AddGroupUserRequest(
                duration_minutes = 60,
        )
        """

    def testAddGroupUserRequest(self):
        """Test AddGroupUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
