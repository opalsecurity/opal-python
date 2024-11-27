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

from opal_security.models.paginated_group_bindings_list import PaginatedGroupBindingsList

class TestPaginatedGroupBindingsList(unittest.TestCase):
    """PaginatedGroupBindingsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedGroupBindingsList:
        """Test PaginatedGroupBindingsList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedGroupBindingsList`
        """
        model = PaginatedGroupBindingsList()
        if include_optional:
            return PaginatedGroupBindingsList(
                next = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw',
                previous = 'cj1sZXdwd2VycWtJ',
                results = [
                    {"group_binding_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","created_by_id":"99d0b81d-14be-4cf6-bd27-348b4af1d11b","created_at":"2022-01-23T04:56:07Z","source_group_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","groups":[{"group_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","group_type":"OKTA_GROUP"},{"group_id":"99d0b81d-14be-4cf6-bd27-348b4af1d11b","group_type":"AWS_SSO_GROUP"}]}
                    ]
            )
        else:
            return PaginatedGroupBindingsList(
                results = [
                    {"group_binding_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","created_by_id":"99d0b81d-14be-4cf6-bd27-348b4af1d11b","created_at":"2022-01-23T04:56:07Z","source_group_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","groups":[{"group_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","group_type":"OKTA_GROUP"},{"group_id":"99d0b81d-14be-4cf6-bd27-348b4af1d11b","group_type":"AWS_SSO_GROUP"}]}
                    ],
        )
        """

    def testPaginatedGroupBindingsList(self):
        """Test PaginatedGroupBindingsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
