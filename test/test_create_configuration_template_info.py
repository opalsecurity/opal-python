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

from opal_security.models.create_configuration_template_info import CreateConfigurationTemplateInfo

class TestCreateConfigurationTemplateInfo(unittest.TestCase):
    """CreateConfigurationTemplateInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateConfigurationTemplateInfo:
        """Test CreateConfigurationTemplateInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateConfigurationTemplateInfo`
        """
        model = CreateConfigurationTemplateInfo()
        if include_optional:
            return CreateConfigurationTemplateInfo(
                admin_owner_id = '7c86c85d-0651-43e2-a748-d69d658418e8',
                visibility = {"visibility":"LIMITED","visibility_group_ids":["7870617d-e72a-47f5-a84c-693817ab4567","1520617d-e72a-47f5-a84c-693817ab48ad2"]},
                linked_audit_message_channel_ids = ["37cb7e41-12ba-46da-92ff-030abe0450b1","37cb7e41-12ba-46da-92ff-030abe0450b2"],
                member_oncall_schedule_ids = ["37cb7e41-12ba-46da-92ff-030abe0450b1","37cb7e41-12ba-46da-92ff-030abe0450b2"],
                break_glass_user_ids = ["37cb7e41-12ba-46da-92ff-030abe0450b1","37cb7e41-12ba-46da-92ff-030abe0450b2"],
                require_mfa_to_approve = False,
                require_mfa_to_connect = False,
                name = 'Prod AWS Template',
                request_configurations = [
                    {"request_configuration_id":"7c86c85d-0651-43e2-a748-d69d658418e8","organization_id":"w86c85d-0651-43e2-a748-d69d658418e8","created_at":"2021-01-06T20:00:00Z","updated_at":"2021-01-06T20:00:00Z","condition":{"group_id":"1b978423-db0a-4037-a4cf-f79c60cb67b3"},"allow_requests":true,"auto_approval":false,"require_mfa_to_request":false,"max_duration_minutes":120,"recommended_duration_minutes":120,"require_support_ticket":false,"reviewer_stages":[{"reviewer_stage_id":"7c86c85d-0651-43e2-a748-d69d658418e8","owner_ids":["37cb7e41-12ba-46da-92ff-030abe0450b1","37cb7e41-12ba-46da-92ff-030abe0450b2"],"stage":1}],"priority":1}
                    ],
                request_configuration_list = {"request_configurations":[{"request_configuration_id":"7c86c85d-0651-43e2-a748-d69d658418e8","organization_id":"w86c85d-0651-43e2-a748-d69d658418e8","condition":null,"allow_requests":true,"auto_approval":false,"require_mfa_to_request":false,"max_duration_minutes":120,"recommended_duration_minutes":120,"require_support_ticket":false,"reviewer_stages":[{"reviewer_stage_id":"7c86c85d-0651-43e2-a748-d69d658418e8","owner_ids":["37cb7e41-12ba-46da-92ff-030abe0450b1","37cb7e41-12ba-46da-92ff-030abe0450b2"],"stage":1}],"priority":0},{"request_configuration_id":"7c86c85d-0651-43e2-a748-d69d658418e9","organization_id":"w86c85d-0651-43e2-a748-d69d658418e8","condition":{"group_id":"1b978423-db0a-4037-a4cf-f79c60cb67b4"},"allow_requests":true,"auto_approval":false,"require_mfa_to_request":false,"max_duration_minutes":120,"recommended_duration_minutes":120,"require_support_ticket":false,"reviewer_stages":[{"reviewer_stage_id":"7c86c85d-0651-43e2-a748-d69d658418e8","owner_ids":["37cb7e41-12ba-46da-92ff-030abe0450b1","37cb7e41-12ba-46da-92ff-030abe0450b2"],"stage":1}],"priority":1}]}
            )
        else:
            return CreateConfigurationTemplateInfo(
                admin_owner_id = '7c86c85d-0651-43e2-a748-d69d658418e8',
                visibility = {"visibility":"LIMITED","visibility_group_ids":["7870617d-e72a-47f5-a84c-693817ab4567","1520617d-e72a-47f5-a84c-693817ab48ad2"]},
                require_mfa_to_approve = False,
                require_mfa_to_connect = False,
                name = 'Prod AWS Template',
        )
        """

    def testCreateConfigurationTemplateInfo(self):
        """Test CreateConfigurationTemplateInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
