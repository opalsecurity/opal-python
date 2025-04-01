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

from opal_security.models.tag_selector import TagSelector

class TestTagSelector(unittest.TestCase):
    """TagSelector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagSelector:
        """Test TagSelector
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagSelector`
        """
        model = TagSelector()
        if include_optional:
            return TagSelector(
                key = '',
                value = '',
                connection_id = ''
            )
        else:
            return TagSelector(
                key = '',
                value = '',
                connection_id = '',
        )
        """

    def testTagSelector(self):
        """Test TagSelector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
