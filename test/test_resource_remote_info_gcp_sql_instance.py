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

from opal.models.resource_remote_info_gcp_sql_instance import ResourceRemoteInfoGcpSqlInstance

class TestResourceRemoteInfoGcpSqlInstance(unittest.TestCase):
    """ResourceRemoteInfoGcpSqlInstance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfoGcpSqlInstance:
        """Test ResourceRemoteInfoGcpSqlInstance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfoGcpSqlInstance`
        """
        model = ResourceRemoteInfoGcpSqlInstance()
        if include_optional:
            return ResourceRemoteInfoGcpSqlInstance(
                instance_id = 'example-sql-898931321',
                project_id = 'example-project-898931321'
            )
        else:
            return ResourceRemoteInfoGcpSqlInstance(
                instance_id = 'example-sql-898931321',
                project_id = 'example-project-898931321',
        )
        """

    def testResourceRemoteInfoGcpSqlInstance(self):
        """Test ResourceRemoteInfoGcpSqlInstance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
