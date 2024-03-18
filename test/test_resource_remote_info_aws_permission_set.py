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

from opal.models.resource_remote_info_aws_permission_set import ResourceRemoteInfoAwsPermissionSet

class TestResourceRemoteInfoAwsPermissionSet(unittest.TestCase):
    """ResourceRemoteInfoAwsPermissionSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfoAwsPermissionSet:
        """Test ResourceRemoteInfoAwsPermissionSet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfoAwsPermissionSet`
        """
        model = ResourceRemoteInfoAwsPermissionSet()
        if include_optional:
            return ResourceRemoteInfoAwsPermissionSet(
                arn = 'arn:aws:sso:::permissionSet/asdf-32139302d201d32/ps-f03323201211e1b9',
                account_id = '234234234234'
            )
        else:
            return ResourceRemoteInfoAwsPermissionSet(
                arn = 'arn:aws:sso:::permissionSet/asdf-32139302d201d32/ps-f03323201211e1b9',
                account_id = '234234234234',
        )
        """

    def testResourceRemoteInfoAwsPermissionSet(self):
        """Test ResourceRemoteInfoAwsPermissionSet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
