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

from opal_security.models.resource_remote_info_teleport_role import ResourceRemoteInfoTeleportRole

class TestResourceRemoteInfoTeleportRole(unittest.TestCase):
    """ResourceRemoteInfoTeleportRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfoTeleportRole:
        """Test ResourceRemoteInfoTeleportRole
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfoTeleportRole`
        """
        model = ResourceRemoteInfoTeleportRole()
        if include_optional:
            return ResourceRemoteInfoTeleportRole(
                role_name = 'admin_role'
            )
        else:
            return ResourceRemoteInfoTeleportRole(
                role_name = 'admin_role',
        )
        """

    def testResourceRemoteInfoTeleportRole(self):
        """Test ResourceRemoteInfoTeleportRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
