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

from opal_security.models.on_call_schedule_list import OnCallScheduleList

class TestOnCallScheduleList(unittest.TestCase):
    """OnCallScheduleList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OnCallScheduleList:
        """Test OnCallScheduleList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OnCallScheduleList`
        """
        model = OnCallScheduleList()
        if include_optional:
            return OnCallScheduleList(
                on_call_schedules = [
                    {"on_call_schedule_id":"50d5e9f6-f23f-4d5a-ae91-b2640cf3975e","third_party_provider":"PAGER_DUTY","remote_id":"P7OWH2R","name":"Customer Support On-Call"}
                    ]
            )
        else:
            return OnCallScheduleList(
                on_call_schedules = [
                    {"on_call_schedule_id":"50d5e9f6-f23f-4d5a-ae91-b2640cf3975e","third_party_provider":"PAGER_DUTY","remote_id":"P7OWH2R","name":"Customer Support On-Call"}
                    ],
        )
        """

    def testOnCallScheduleList(self):
        """Test OnCallScheduleList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
