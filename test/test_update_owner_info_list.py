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

from opal.models.update_owner_info_list import UpdateOwnerInfoList

class TestUpdateOwnerInfoList(unittest.TestCase):
    """UpdateOwnerInfoList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateOwnerInfoList:
        """Test UpdateOwnerInfoList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateOwnerInfoList`
        """
        model = UpdateOwnerInfoList()
        if include_optional:
            return UpdateOwnerInfoList(
                owners = [
                    {"owner_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","name":"API Owner","description":"This owner represents the API team owners.","access_request_escalation_period":120}
                    ]
            )
        else:
            return UpdateOwnerInfoList(
                owners = [
                    {"owner_id":"f454d283-ca87-4a8a-bdbb-df212eca5353","name":"API Owner","description":"This owner represents the API team owners.","access_request_escalation_period":120}
                    ],
        )
        """

    def testUpdateOwnerInfoList(self):
        """Test UpdateOwnerInfoList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
