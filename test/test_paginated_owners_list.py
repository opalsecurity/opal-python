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

from opal_security.models.paginated_owners_list import PaginatedOwnersList

class TestPaginatedOwnersList(unittest.TestCase):
    """PaginatedOwnersList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedOwnersList:
        """Test PaginatedOwnersList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedOwnersList`
        """
        model = PaginatedOwnersList()
        if include_optional:
            return PaginatedOwnersList(
                next = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw',
                previous = 'cj1sZXdwd2VycWVtY29zZnNkc2NzUWxNMEUxTXk0ME16UXpNallsTWtJ',
                results = [
                    {"owner_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","name":"API Owner","description":"This owner represents the API team owners.","access_request_escalation_period":120}
                    ]
            )
        else:
            return PaginatedOwnersList(
                results = [
                    {"owner_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","name":"API Owner","description":"This owner represents the API team owners.","access_request_escalation_period":120}
                    ],
        )
        """

    def testPaginatedOwnersList(self):
        """Test PaginatedOwnersList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
