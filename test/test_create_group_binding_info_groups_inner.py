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

from opal.models.create_group_binding_info_groups_inner import CreateGroupBindingInfoGroupsInner

class TestCreateGroupBindingInfoGroupsInner(unittest.TestCase):
    """CreateGroupBindingInfoGroupsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateGroupBindingInfoGroupsInner:
        """Test CreateGroupBindingInfoGroupsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateGroupBindingInfoGroupsInner`
        """
        model = CreateGroupBindingInfoGroupsInner()
        if include_optional:
            return CreateGroupBindingInfoGroupsInner(
                group_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353'
            )
        else:
            return CreateGroupBindingInfoGroupsInner(
                group_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
        )
        """

    def testCreateGroupBindingInfoGroupsInner(self):
        """Test CreateGroupBindingInfoGroupsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()