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

from opal_security.models.create_request_configuration_info_list import CreateRequestConfigurationInfoList

class TestCreateRequestConfigurationInfoList(unittest.TestCase):
    """CreateRequestConfigurationInfoList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateRequestConfigurationInfoList:
        """Test CreateRequestConfigurationInfoList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRequestConfigurationInfoList`
        """
        model = CreateRequestConfigurationInfoList()
        if include_optional:
            return CreateRequestConfigurationInfoList(
                request_configurations = [
                    {"request_configuration_id":"7c86c85d-0651-43e2-a748-d69d658418e8","organization_id":"w86c85d-0651-43e2-a748-d69d658418e8","created_at":"2021-01-06T20:00:00Z","updated_at":"2021-01-06T20:00:00Z","condition":{"group_id":"1b978423-db0a-4037-a4cf-f79c60cb67b3"},"allow_requests":true,"auto_approval":false,"require_mfa_to_request":false,"max_duration_minutes":120,"recommended_duration_minutes":120,"require_support_ticket":false,"reviewer_stages":[{"reviewer_stage_id":"7c86c85d-0651-43e2-a748-d69d658418e8","owner_ids":["37cb7e41-12ba-46da-92ff-030abe0450b1","37cb7e41-12ba-46da-92ff-030abe0450b2"],"stage":1}],"priority":1}
                    ]
            )
        else:
            return CreateRequestConfigurationInfoList(
                request_configurations = [
                    {"request_configuration_id":"7c86c85d-0651-43e2-a748-d69d658418e8","organization_id":"w86c85d-0651-43e2-a748-d69d658418e8","created_at":"2021-01-06T20:00:00Z","updated_at":"2021-01-06T20:00:00Z","condition":{"group_id":"1b978423-db0a-4037-a4cf-f79c60cb67b3"},"allow_requests":true,"auto_approval":false,"require_mfa_to_request":false,"max_duration_minutes":120,"recommended_duration_minutes":120,"require_support_ticket":false,"reviewer_stages":[{"reviewer_stage_id":"7c86c85d-0651-43e2-a748-d69d658418e8","owner_ids":["37cb7e41-12ba-46da-92ff-030abe0450b1","37cb7e41-12ba-46da-92ff-030abe0450b2"],"stage":1}],"priority":1}
                    ],
        )
        """

    def testCreateRequestConfigurationInfoList(self):
        """Test CreateRequestConfigurationInfoList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
