# coding: utf-8

"""
    Opal API

    The Opal API is a RESTful API that allows you to interact with the Opal Security platform programmatically.

    The version of the OpenAPI document: 1.0
    Contact: hello@opal.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opal_security.models.group_containing_group_list import GroupContainingGroupList

class TestGroupContainingGroupList(unittest.TestCase):
    """GroupContainingGroupList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupContainingGroupList:
        """Test GroupContainingGroupList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupContainingGroupList`
        """
        model = GroupContainingGroupList()
        if include_optional:
            return GroupContainingGroupList(
                containing_groups = [
                    {containing_group_id=f454d283-ca87-4a8a-bdbb-df212eca5353}
                    ]
            )
        else:
            return GroupContainingGroupList(
                containing_groups = [
                    {containing_group_id=f454d283-ca87-4a8a-bdbb-df212eca5353}
                    ],
        )
        """

    def testGroupContainingGroupList(self):
        """Test GroupContainingGroupList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
