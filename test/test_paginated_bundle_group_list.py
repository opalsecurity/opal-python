# coding: utf-8

"""
    Opal API

    The Opal API is a RESTful API that allows you to interact with the Opal Security platform programmatically.

    The version of the OpenAPI document: 1.0
    Contact: hello@opal.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opal_security.models.paginated_bundle_group_list import PaginatedBundleGroupList

class TestPaginatedBundleGroupList(unittest.TestCase):
    """PaginatedBundleGroupList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedBundleGroupList:
        """Test PaginatedBundleGroupList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedBundleGroupList`
        """
        model = PaginatedBundleGroupList()
        if include_optional:
            return PaginatedBundleGroupList(
                previous = 'cj1sZXdwd2VycWVtY29zZnNkc2NzUWxNMEUxTXk0ME16UXpNallsTWtJ',
                next = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw',
                total_count = 2,
                bundle_groups = [
                    opal_security.models.bundle_group.BundleGroup(
                        bundle_id = 'a381e7a3-e5e0-4c48-b1d6-4ccb4c191bc1', 
                        group_id = 'a381e7a3-e5e0-4c48-b1d6-4ccb4c191bc1', )
                    ]
            )
        else:
            return PaginatedBundleGroupList(
                bundle_groups = [
                    opal_security.models.bundle_group.BundleGroup(
                        bundle_id = 'a381e7a3-e5e0-4c48-b1d6-4ccb4c191bc1', 
                        group_id = 'a381e7a3-e5e0-4c48-b1d6-4ccb4c191bc1', )
                    ],
        )
        """

    def testPaginatedBundleGroupList(self):
        """Test PaginatedBundleGroupList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
