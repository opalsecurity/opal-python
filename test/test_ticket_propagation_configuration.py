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

from opal_security.models.ticket_propagation_configuration import TicketPropagationConfiguration

class TestTicketPropagationConfiguration(unittest.TestCase):
    """TicketPropagationConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TicketPropagationConfiguration:
        """Test TicketPropagationConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TicketPropagationConfiguration`
        """
        model = TicketPropagationConfiguration()
        if include_optional:
            return TicketPropagationConfiguration(
                enabled_on_grant = True,
                enabled_on_revocation = True,
                ticket_provider = 'LINEAR',
                ticket_project_id = ''
            )
        else:
            return TicketPropagationConfiguration(
                enabled_on_grant = True,
                enabled_on_revocation = True,
        )
        """

    def testTicketPropagationConfiguration(self):
        """Test TicketPropagationConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
