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

from opal_security.models.paginated_uars_list import PaginatedUARsList

class TestPaginatedUARsList(unittest.TestCase):
    """PaginatedUARsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedUARsList:
        """Test PaginatedUARsList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedUARsList`
        """
        model = PaginatedUARsList()
        if include_optional:
            return PaginatedUARsList(
                next = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw',
                previous = 'cj1sZXdwd2VycWVtY29zZnNkc2NzUWxNMEUxTXk0ME16UXpNallsTWtJ',
                results = [
                    {"uar_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","name":"Monthly UAR (July)","send_reviewer_assignment_notification":false,"deadline":"2022-07-14 06:59:59","time_zone":"America/Los_Angeles","self_review_allowed":false,"uar_scope":{"tags":[{"key":"uar_scope","value":"high_priority"}],"names":["demo","api"],"admins":["f454d283-ca87-4a8a-bdbb-df212eca5353","8763d283-ca87-4a8a-bdbb-df212ecab139"]}}
                    ]
            )
        else:
            return PaginatedUARsList(
                results = [
                    {"uar_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","name":"Monthly UAR (July)","send_reviewer_assignment_notification":false,"deadline":"2022-07-14 06:59:59","time_zone":"America/Los_Angeles","self_review_allowed":false,"uar_scope":{"tags":[{"key":"uar_scope","value":"high_priority"}],"names":["demo","api"],"admins":["f454d283-ca87-4a8a-bdbb-df212eca5353","8763d283-ca87-4a8a-bdbb-df212ecab139"]}}
                    ],
        )
        """

    def testPaginatedUARsList(self):
        """Test PaginatedUARsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
