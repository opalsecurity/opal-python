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

from opal.models.idp_group_mapping_list import IdpGroupMappingList

class TestIdpGroupMappingList(unittest.TestCase):
    """IdpGroupMappingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdpGroupMappingList:
        """Test IdpGroupMappingList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdpGroupMappingList`
        """
        model = IdpGroupMappingList()
        if include_optional:
            return IdpGroupMappingList(
                idp_group_mappings = [
                    {id=7870617d-e72a-47f5-a84c-693817ab4567, organization_id=1520617d-e72a-47f5-a84c-693817ab48ad2, app_resource_id=6f99639b-7928-4043-8184-47cbc6766145, group_id=6f99639b-7928-4043-8184-47cbc6766145, alias=finance-team, hidden_from_end_user=false}
                    ]
            )
        else:
            return IdpGroupMappingList(
                idp_group_mappings = [
                    {id=7870617d-e72a-47f5-a84c-693817ab4567, organization_id=1520617d-e72a-47f5-a84c-693817ab48ad2, app_resource_id=6f99639b-7928-4043-8184-47cbc6766145, group_id=6f99639b-7928-4043-8184-47cbc6766145, alias=finance-team, hidden_from_end_user=false}
                    ],
        )
        """

    def testIdpGroupMappingList(self):
        """Test IdpGroupMappingList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
