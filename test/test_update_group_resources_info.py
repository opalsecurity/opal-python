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

from opal.models.update_group_resources_info import UpdateGroupResourcesInfo

class TestUpdateGroupResourcesInfo(unittest.TestCase):
    """UpdateGroupResourcesInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateGroupResourcesInfo:
        """Test UpdateGroupResourcesInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateGroupResourcesInfo`
        """
        model = UpdateGroupResourcesInfo()
        if include_optional:
            return UpdateGroupResourcesInfo(
                resources = [
                    {"resource_id":"b5a5ca27-0ea3-4d86-9199-2126d57d1fbd","access_level_remote_id":"write"}
                    ]
            )
        else:
            return UpdateGroupResourcesInfo(
                resources = [
                    {"resource_id":"b5a5ca27-0ea3-4d86-9199-2126d57d1fbd","access_level_remote_id":"write"}
                    ],
        )
        """

    def testUpdateGroupResourcesInfo(self):
        """Test UpdateGroupResourcesInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
