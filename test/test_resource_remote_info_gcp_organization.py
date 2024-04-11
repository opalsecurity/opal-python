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

from opal.models.resource_remote_info_gcp_organization import ResourceRemoteInfoGcpOrganization

class TestResourceRemoteInfoGcpOrganization(unittest.TestCase):
    """ResourceRemoteInfoGcpOrganization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfoGcpOrganization:
        """Test ResourceRemoteInfoGcpOrganization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfoGcpOrganization`
        """
        model = ResourceRemoteInfoGcpOrganization()
        if include_optional:
            return ResourceRemoteInfoGcpOrganization(
                organization_id = 'organizations/898931321'
            )
        else:
            return ResourceRemoteInfoGcpOrganization(
                organization_id = 'organizations/898931321',
        )
        """

    def testResourceRemoteInfoGcpOrganization(self):
        """Test ResourceRemoteInfoGcpOrganization"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
