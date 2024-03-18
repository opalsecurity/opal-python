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

from opal.models.uar import UAR

class TestUAR(unittest.TestCase):
    """UAR unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UAR:
        """Test UAR
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UAR`
        """
        model = UAR()
        if include_optional:
            return UAR(
                uar_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
                name = 'Monthly UAR (July)',
                reviewer_assignment_policy = 'MANUALLY',
                send_reviewer_assignment_notification = False,
                deadline = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_zone = 'America/Los_Angeles',
                self_review_allowed = False,
                uar_scope = {"tags":[{"key":"uar_scope","value":"high_priority"}],"names":["demo","api"],"admins":["f454d283-ca87-4a8a-bdbb-df212eca5353","8763d283-ca87-4a8a-bdbb-df212ecab139"]}
            )
        else:
            return UAR(
                uar_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
                name = 'Monthly UAR (July)',
                reviewer_assignment_policy = 'MANUALLY',
                send_reviewer_assignment_notification = False,
                deadline = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_zone = 'America/Los_Angeles',
                self_review_allowed = False,
        )
        """

    def testUAR(self):
        """Test UAR"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
