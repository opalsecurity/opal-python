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

from opal_security.models.resource_remote_info_salesforce_permission_set import ResourceRemoteInfoSalesforcePermissionSet

class TestResourceRemoteInfoSalesforcePermissionSet(unittest.TestCase):
    """ResourceRemoteInfoSalesforcePermissionSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfoSalesforcePermissionSet:
        """Test ResourceRemoteInfoSalesforcePermissionSet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfoSalesforcePermissionSet`
        """
        model = ResourceRemoteInfoSalesforcePermissionSet()
        if include_optional:
            return ResourceRemoteInfoSalesforcePermissionSet(
                permission_set_id = '0PS5Y090202wOV7WAM'
            )
        else:
            return ResourceRemoteInfoSalesforcePermissionSet(
                permission_set_id = '0PS5Y090202wOV7WAM',
        )
        """

    def testResourceRemoteInfoSalesforcePermissionSet(self):
        """Test ResourceRemoteInfoSalesforcePermissionSet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
