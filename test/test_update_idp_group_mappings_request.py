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

from opal_security.models.update_idp_group_mappings_request import UpdateIdpGroupMappingsRequest

class TestUpdateIdpGroupMappingsRequest(unittest.TestCase):
    """UpdateIdpGroupMappingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateIdpGroupMappingsRequest:
        """Test UpdateIdpGroupMappingsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateIdpGroupMappingsRequest`
        """
        model = UpdateIdpGroupMappingsRequest()
        if include_optional:
            return UpdateIdpGroupMappingsRequest(
                mappings = [
                    opal.models.update_idp_group_mappings_request_mappings_inner.updateIdpGroupMappings_request_mappings_inner(
                        group_id = '', 
                        alias = '', )
                    ]
            )
        else:
            return UpdateIdpGroupMappingsRequest(
                mappings = [
                    opal.models.update_idp_group_mappings_request_mappings_inner.updateIdpGroupMappings_request_mappings_inner(
                        group_id = '', 
                        alias = '', )
                    ],
        )
        """

    def testUpdateIdpGroupMappingsRequest(self):
        """Test UpdateIdpGroupMappingsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
