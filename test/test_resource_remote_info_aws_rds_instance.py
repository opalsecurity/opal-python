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

from opal.models.resource_remote_info_aws_rds_instance import ResourceRemoteInfoAwsRdsInstance

class TestResourceRemoteInfoAwsRdsInstance(unittest.TestCase):
    """ResourceRemoteInfoAwsRdsInstance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfoAwsRdsInstance:
        """Test ResourceRemoteInfoAwsRdsInstance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfoAwsRdsInstance`
        """
        model = ResourceRemoteInfoAwsRdsInstance()
        if include_optional:
            return ResourceRemoteInfoAwsRdsInstance(
                instance_id = 'demo-mysql-db',
                region = 'us-east-2',
                resource_id = 'db-AOO8V0XUCNU13XLZXQDQRSN0NQ',
                account_id = '234234234234'
            )
        else:
            return ResourceRemoteInfoAwsRdsInstance(
                instance_id = 'demo-mysql-db',
                region = 'us-east-2',
                resource_id = 'db-AOO8V0XUCNU13XLZXQDQRSN0NQ',
        )
        """

    def testResourceRemoteInfoAwsRdsInstance(self):
        """Test ResourceRemoteInfoAwsRdsInstance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
