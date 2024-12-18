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

from opal_security.models.resource_remote_info import ResourceRemoteInfo

class TestResourceRemoteInfo(unittest.TestCase):
    """ResourceRemoteInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRemoteInfo:
        """Test ResourceRemoteInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRemoteInfo`
        """
        model = ResourceRemoteInfo()
        if include_optional:
            return ResourceRemoteInfo(
                aws_account = opal.models.resource_remote_info_aws_account.ResourceRemoteInfo_aws_account(
                    account_id = '234234234234', ),
                aws_permission_set = opal.models.resource_remote_info_aws_permission_set.ResourceRemoteInfo_aws_permission_set(
                    arn = 'arn:aws:sso:::permissionSet/asdf-32139302d201d32/ps-f03323201211e1b9', 
                    account_id = '234234234234', ),
                aws_iam_role = opal.models.resource_remote_info_aws_iam_role.ResourceRemoteInfo_aws_iam_role(
                    arn = 'arn:aws:iam::179308207300:role/MyRole', 
                    account_id = '234234234234', ),
                aws_ec2_instance = opal.models.resource_remote_info_aws_ec2_instance.ResourceRemoteInfo_aws_ec2_instance(
                    instance_id = 'i-13f1a1e2899f9e93a', 
                    region = 'us-east-2', 
                    account_id = '234234234234', ),
                aws_rds_instance = opal.models.resource_remote_info_aws_rds_instance.ResourceRemoteInfo_aws_rds_instance(
                    instance_id = 'demo-mysql-db', 
                    region = 'us-east-2', 
                    resource_id = 'db-AOO8V0XUCNU13XLZXQDQRSN0NQ', 
                    account_id = '234234234234', ),
                aws_eks_cluster = opal.models.resource_remote_info_aws_eks_cluster.ResourceRemoteInfo_aws_eks_cluster(
                    arn = 'arn:aws:eks:us-east-2:234234234234:cluster/testcluster', 
                    account_id = '234234234234', ),
                gcp_organization = opal.models.resource_remote_info_gcp_organization.ResourceRemoteInfo_gcp_organization(
                    organization_id = 'organizations/898931321', ),
                gcp_bucket = opal.models.resource_remote_info_gcp_bucket.ResourceRemoteInfo_gcp_bucket(
                    bucket_id = 'example-bucket-898931321', ),
                gcp_compute_instance = opal.models.resource_remote_info_gcp_compute_instance.ResourceRemoteInfo_gcp_compute_instance(
                    instance_id = 'example-instance-898931321', 
                    project_id = 'example-project-898931321', 
                    zone = 'us-central1-a', ),
                gcp_big_query_dataset = opal.models.resource_remote_info_gcp_big_query_dataset.ResourceRemoteInfo_gcp_big_query_dataset(
                    project_id = 'example-project-898931321', 
                    dataset_id = 'example-dataset-898931321', ),
                gcp_big_query_table = opal.models.resource_remote_info_gcp_big_query_table.ResourceRemoteInfo_gcp_big_query_table(
                    project_id = 'example-project-898931321', 
                    dataset_id = 'example-dataset-898931321', 
                    table_id = 'example-table-898931321', ),
                gcp_folder = opal.models.resource_remote_info_gcp_folder.ResourceRemoteInfo_gcp_folder(
                    folder_id = 'folder/898931321', ),
                gcp_gke_cluster = opal.models.resource_remote_info_gcp_gke_cluster.ResourceRemoteInfo_gcp_gke_cluster(
                    cluster_name = 'example-cluster-898931321', ),
                gcp_project = opal.models.resource_remote_info_gcp_project.ResourceRemoteInfo_gcp_project(
                    project_id = 'example-project-898931321', ),
                gcp_sql_instance = opal.models.resource_remote_info_gcp_sql_instance.ResourceRemoteInfo_gcp_sql_instance(
                    instance_id = 'example-sql-898931321', 
                    project_id = 'example-project-898931321', ),
                github_repo = opal.models.resource_remote_info_github_repo.ResourceRemoteInfo_github_repo(
                    repo_id = '898931321', 
                    repo_name = 'Opal Security', ),
                gitlab_project = opal.models.resource_remote_info_gitlab_project.ResourceRemoteInfo_gitlab_project(
                    project_id = '898931321', ),
                okta_app = opal.models.resource_remote_info_okta_app.ResourceRemoteInfo_okta_app(
                    app_id = 'a9dfas0f678asdf67867', ),
                okta_standard_role = opal.models.resource_remote_info_okta_standard_role.ResourceRemoteInfo_okta_standard_role(
                    role_type = 'ORG_ADMIN', ),
                okta_custom_role = opal.models.resource_remote_info_okta_custom_role.ResourceRemoteInfo_okta_custom_role(
                    role_id = 'a9dfas0f678asdf67867', ),
                pagerduty_role = opal.models.resource_remote_info_pagerduty_role.ResourceRemoteInfo_pagerduty_role(
                    role_name = 'owner', ),
                salesforce_permission_set = opal.models.resource_remote_info_salesforce_permission_set.ResourceRemoteInfo_salesforce_permission_set(
                    permission_set_id = '0PS5Y090202wOV7WAM', ),
                salesforce_profile = opal.models.resource_remote_info_salesforce_profile.ResourceRemoteInfo_salesforce_profile(
                    profile_id = '0PS5Y090202wOV7WAM', 
                    user_license_id = '1005Y030081Qb5XJHS', ),
                salesforce_role = opal.models.resource_remote_info_salesforce_role.ResourceRemoteInfo_salesforce_role(
                    role_id = '0PS5Y090202wOV7WAM', ),
                teleport_role = opal.models.resource_remote_info_teleport_role.ResourceRemoteInfo_teleport_role(
                    role_name = 'admin_role', )
            )
        else:
            return ResourceRemoteInfo(
        )
        """

    def testResourceRemoteInfo(self):
        """Test ResourceRemoteInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
