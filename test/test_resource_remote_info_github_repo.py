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

from opal_security.models.resource_remote_info_github_repo import ResourceRemoteInfoGithubRepo

class TestResourceRemoteInfoGithubRepo(unittest.TestCase):
    """ResourceRemoteInfoGithubRepo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfoGithubRepo:
        """Test ResourceRemoteInfoGithubRepo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfoGithubRepo`
        """
        model = ResourceRemoteInfoGithubRepo()
        if include_optional:
            return ResourceRemoteInfoGithubRepo(
                repo_id = '898931321',
                repo_name = 'Opal Security'
            )
        else:
            return ResourceRemoteInfoGithubRepo(
                repo_name = 'Opal Security',
        )
        """

    def testResourceRemoteInfoGithubRepo(self):
        """Test ResourceRemoteInfoGithubRepo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
