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

from opal.models.request_custom_field_response_field_value import RequestCustomFieldResponseFieldValue

class TestRequestCustomFieldResponseFieldValue(unittest.TestCase):
    """RequestCustomFieldResponseFieldValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestCustomFieldResponseFieldValue:
        """Test RequestCustomFieldResponseFieldValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestCustomFieldResponseFieldValue`
        """
        model = RequestCustomFieldResponseFieldValue()
        if include_optional:
            return RequestCustomFieldResponseFieldValue(
            )
        else:
            return RequestCustomFieldResponseFieldValue(
        )
        """

    def testRequestCustomFieldResponseFieldValue(self):
        """Test RequestCustomFieldResponseFieldValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
