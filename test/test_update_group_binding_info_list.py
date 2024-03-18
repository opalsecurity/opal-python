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

from opal.models.update_group_binding_info_list import UpdateGroupBindingInfoList

class TestUpdateGroupBindingInfoList(unittest.TestCase):
    """UpdateGroupBindingInfoList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateGroupBindingInfoList:
        """Test UpdateGroupBindingInfoList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateGroupBindingInfoList`
        """
        model = UpdateGroupBindingInfoList()
        if include_optional:
            return UpdateGroupBindingInfoList(
                group_bindings = [
                    {"group_binding_id":"0ae19dbf-324d-4216-999c-574d46182c7e","source_group_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","groups":[{"group_id":"f454d283-ca87-4a8a-bdbb-df212eca5353"},{"group_id":"99d0b81d-14be-4cf6-bd27-348b4af1d11b"}]}
                    ]
            )
        else:
            return UpdateGroupBindingInfoList(
                group_bindings = [
                    {"group_binding_id":"0ae19dbf-324d-4216-999c-574d46182c7e","source_group_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","groups":[{"group_id":"f454d283-ca87-4a8a-bdbb-df212eca5353"},{"group_id":"99d0b81d-14be-4cf6-bd27-348b4af1d11b"}]}
                    ],
        )
        """

    def testUpdateGroupBindingInfoList(self):
        """Test UpdateGroupBindingInfoList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()