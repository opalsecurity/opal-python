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

from opal_security.models.resource_remote_info_salesforce_role import ResourceRemoteInfoSalesforceRole

class TestResourceRemoteInfoSalesforceRole(unittest.TestCase):
    """ResourceRemoteInfoSalesforceRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfoSalesforceRole:
        """Test ResourceRemoteInfoSalesforceRole
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfoSalesforceRole`
        """
        model = ResourceRemoteInfoSalesforceRole()
        if include_optional:
            return ResourceRemoteInfoSalesforceRole(
                role_id = '0PS5Y090202wOV7WAM'
            )
        else:
            return ResourceRemoteInfoSalesforceRole(
                role_id = '0PS5Y090202wOV7WAM',
        )
        """

    def testResourceRemoteInfoSalesforceRole(self):
        """Test ResourceRemoteInfoSalesforceRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
