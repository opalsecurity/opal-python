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

from opal.models.resource_access_user_list import ResourceAccessUserList

class TestResourceAccessUserList(unittest.TestCase):
    """ResourceAccessUserList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceAccessUserList:
        """Test ResourceAccessUserList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceAccessUserList`
        """
        model = ResourceAccessUserList()
        if include_optional:
            return ResourceAccessUserList(
                results = [
                    {"full_name":"Jake Barnes","user_id":"29827fb8-f2dd-4e80-9576-28e31e9934ac","resource_id":"1b978423-db0a-4037-a4cf-f79c60cb67b3","expiration_date":"2022-01-23T04:56:07Z","email":"jake@company.dev"}
                    ]
            )
        else:
            return ResourceAccessUserList(
        )
        """

    def testResourceAccessUserList(self):
        """Test ResourceAccessUserList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()