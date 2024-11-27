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

from opal_security.models.resource_remote_info_gcp_service_account import ResourceRemoteInfoGcpServiceAccount

class TestResourceRemoteInfoGcpServiceAccount(unittest.TestCase):
    """ResourceRemoteInfoGcpServiceAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfoGcpServiceAccount:
        """Test ResourceRemoteInfoGcpServiceAccount
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfoGcpServiceAccount`
        """
        model = ResourceRemoteInfoGcpServiceAccount()
        if include_optional:
            return ResourceRemoteInfoGcpServiceAccount(
                email = 'production@project.iam.gserviceaccount.com',
                service_account_id = '103561576023829463298',
                project_id = 'example-project-898931321'
            )
        else:
            return ResourceRemoteInfoGcpServiceAccount(
                email = 'production@project.iam.gserviceaccount.com',
                service_account_id = '103561576023829463298',
                project_id = 'example-project-898931321',
        )
        """

    def testResourceRemoteInfoGcpServiceAccount(self):
        """Test ResourceRemoteInfoGcpServiceAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
