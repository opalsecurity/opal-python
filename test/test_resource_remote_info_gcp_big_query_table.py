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

from opal_security.models.resource_remote_info_gcp_big_query_table import ResourceRemoteInfoGcpBigQueryTable

class TestResourceRemoteInfoGcpBigQueryTable(unittest.TestCase):
    """ResourceRemoteInfoGcpBigQueryTable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfoGcpBigQueryTable:
        """Test ResourceRemoteInfoGcpBigQueryTable
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfoGcpBigQueryTable`
        """
        model = ResourceRemoteInfoGcpBigQueryTable()
        if include_optional:
            return ResourceRemoteInfoGcpBigQueryTable(
                project_id = 'example-project-898931321',
                dataset_id = 'example-dataset-898931321',
                table_id = 'example-table-898931321'
            )
        else:
            return ResourceRemoteInfoGcpBigQueryTable(
                project_id = 'example-project-898931321',
                dataset_id = 'example-dataset-898931321',
                table_id = 'example-table-898931321',
        )
        """

    def testResourceRemoteInfoGcpBigQueryTable(self):
        """Test ResourceRemoteInfoGcpBigQueryTable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
