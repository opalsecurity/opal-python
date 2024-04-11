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

from opal.models.create_group_info import CreateGroupInfo

class TestCreateGroupInfo(unittest.TestCase):
    """CreateGroupInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateGroupInfo:
        """Test CreateGroupInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateGroupInfo`
        """
        model = CreateGroupInfo()
        if include_optional:
            return CreateGroupInfo(
                name = 'mongo-db-prod',
                description = 'Engineering team Okta group.',
                group_type = 'OPAL_GROUP',
                app_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
                remote_info = opal.models.group_remote_info.GroupRemoteInfo(
                    active_directory_group = opal.models.group_remote_info_active_directory_group.GroupRemoteInfo_active_directory_group(
                        group_id = '01fa7402-01d8-103b-8deb-5f3a0ab7884', ), 
                    github_team = opal.models.group_remote_info_github_team.GroupRemoteInfo_github_team(
                        team_id = '898931321', 
                        team_slug = 'opal-security', ), 
                    gitlab_group = opal.models.group_remote_info_gitlab_group.GroupRemoteInfo_gitlab_group(
                        group_id = '898931321', ), 
                    google_group = opal.models.group_remote_info_google_group.GroupRemoteInfo_google_group(
                        group_id = '1y6w882181n7sg', ), 
                    ldap_group = opal.models.group_remote_info_ldap_group.GroupRemoteInfo_ldap_group(
                        group_id = '01fa7402-01d8-103b-8deb-5f3a0ab7884', ), 
                    okta_group = opal.models.group_remote_info_okta_group.GroupRemoteInfo_okta_group(
                        group_id = '00gjs33pe8rtmRrp3rd6', ), 
                    duo_group = opal.models.group_remote_info_duo_group.GroupRemoteInfo_duo_group(
                        group_id = 'DSRD8W89B9DNDBY4RHAC', ), 
                    azure_ad_security_group = opal.models.group_remote_info_azure_ad_security_group.GroupRemoteInfo_azure_ad_security_group(
                        group_id = '01fa7402-01d8-103b-8deb-5f3a0ab7884', ), 
                    azure_ad_microsoft_365_group = opal.models.group_remote_info_azure_ad_microsoft_365_group.GroupRemoteInfo_azure_ad_microsoft_365_group(
                        group_id = '01fa7402-01d8-103b-8deb-5f3a0ab7884', ), ),
                remote_group_id = '00g4fixjd6Bc9w012345',
                metadata = '{ "okta_directory_group": { "group_id": "00g4bs66kwtpe1g12345" } }'
            )
        else:
            return CreateGroupInfo(
                name = 'mongo-db-prod',
                group_type = 'OPAL_GROUP',
                app_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
        )
        """

    def testCreateGroupInfo(self):
        """Test CreateGroupInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
