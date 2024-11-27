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

from opal_security.models.group_binding import GroupBinding

class TestGroupBinding(unittest.TestCase):
    """GroupBinding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupBinding:
        """Test GroupBinding
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupBinding`
        """
        model = GroupBinding()
        if include_optional:
            return GroupBinding(
                group_binding_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
                created_by_id = '99d0b81d-14be-4cf6-bd27-348b4af1d11b',
                created_at = '2022-01-23T04:56:07Z',
                source_group_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
                groups = [
                    {"group_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","group_type":"OKTA_GROUP"}
                    ]
            )
        else:
            return GroupBinding(
                group_binding_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
                created_by_id = '99d0b81d-14be-4cf6-bd27-348b4af1d11b',
                created_at = '2022-01-23T04:56:07Z',
                source_group_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
                groups = [
                    {"group_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","group_type":"OKTA_GROUP"}
                    ],
        )
        """

    def testGroupBinding(self):
        """Test GroupBinding"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
