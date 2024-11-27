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

from opal_security.models.group_resource import GroupResource

class TestGroupResource(unittest.TestCase):
    """GroupResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupResource:
        """Test GroupResource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupResource`
        """
        model = GroupResource()
        if include_optional:
            return GroupResource(
                group_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
                resource_id = 'b5a5ca27-0ea3-4d86-9199-2126d57d1fbd',
                access_level = {"access_level_name":"AdminRole","access_level_remote_id":"arn:aws:iam::590304332660:role/AdministratorAccess"}
            )
        else:
            return GroupResource(
                group_id = 'f454d283-ca87-4a8a-bdbb-df212eca5353',
                resource_id = 'b5a5ca27-0ea3-4d86-9199-2126d57d1fbd',
                access_level = {"access_level_name":"AdminRole","access_level_remote_id":"arn:aws:iam::590304332660:role/AdministratorAccess"},
        )
        """

    def testGroupResource(self):
        """Test GroupResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
