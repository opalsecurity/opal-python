# ResourceRemoteInfo

Information that defines the remote resource. This replaces the deprecated remote_id and metadata fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databricks_account_service_principal** | [**ResourceRemoteInfoDatabricksAccountServicePrincipal**](ResourceRemoteInfoDatabricksAccountServicePrincipal.md) |  | [optional] 
**azure_subscription** | [**ResourceRemoteInfoAzureSubscription**](ResourceRemoteInfoAzureSubscription.md) |  | [optional] 
**azure_resource_group** | [**ResourceRemoteInfoAzureResourceGroup**](ResourceRemoteInfoAzureResourceGroup.md) |  | [optional] 
**azure_management_group** | [**ResourceRemoteInfoAzureManagementGroup**](ResourceRemoteInfoAzureManagementGroup.md) |  | [optional] 
**azure_virtual_machine** | [**ResourceRemoteInfoAzureVirtualMachine**](ResourceRemoteInfoAzureVirtualMachine.md) |  | [optional] 
**azure_storage_account** | [**ResourceRemoteInfoAzureStorageAccount**](ResourceRemoteInfoAzureStorageAccount.md) |  | [optional] 
**azure_storage_container** | [**ResourceRemoteInfoAzureStorageContainer**](ResourceRemoteInfoAzureStorageContainer.md) |  | [optional] 
**azure_sql_server** | [**ResourceRemoteInfoAzureSqlServer**](ResourceRemoteInfoAzureSqlServer.md) |  | [optional] 
**azure_sql_database** | [**ResourceRemoteInfoAzureSqlDatabase**](ResourceRemoteInfoAzureSqlDatabase.md) |  | [optional] 
**azure_sql_managed_instance** | [**ResourceRemoteInfoAzureSqlManagedInstance**](ResourceRemoteInfoAzureSqlManagedInstance.md) |  | [optional] 
**azure_sql_managed_database** | [**ResourceRemoteInfoAzureSqlManagedDatabase**](ResourceRemoteInfoAzureSqlManagedDatabase.md) |  | [optional] 
**azure_user_assigned_managed_identity** | [**ResourceRemoteInfoAzureUserAssignedManagedIdentity**](ResourceRemoteInfoAzureUserAssignedManagedIdentity.md) |  | [optional] 
**azure_enterprise_app** | [**ResourceRemoteInfoAzureEnterpriseApp**](ResourceRemoteInfoAzureEnterpriseApp.md) |  | [optional] 
**azure_entra_id_role** | [**ResourceRemoteInfoAzureEntraIdRole**](ResourceRemoteInfoAzureEntraIdRole.md) |  | [optional] 
**aws_organizational_unit** | [**ResourceRemoteInfoAwsOrganizationalUnit**](ResourceRemoteInfoAwsOrganizationalUnit.md) |  | [optional] 
**aws_account** | [**ResourceRemoteInfoAwsAccount**](ResourceRemoteInfoAwsAccount.md) |  | [optional] 
**aws_permission_set** | [**ResourceRemoteInfoAwsPermissionSet**](ResourceRemoteInfoAwsPermissionSet.md) |  | [optional] 
**aws_iam_role** | [**ResourceRemoteInfoAwsIamRole**](ResourceRemoteInfoAwsIamRole.md) |  | [optional] 
**aws_ec2_instance** | [**ResourceRemoteInfoAwsEc2Instance**](ResourceRemoteInfoAwsEc2Instance.md) |  | [optional] 
**aws_rds_cluster** | [**ResourceRemoteInfoAwsRdsCluster**](ResourceRemoteInfoAwsRdsCluster.md) |  | [optional] 
**aws_rds_instance** | [**ResourceRemoteInfoAwsRdsInstance**](ResourceRemoteInfoAwsRdsInstance.md) |  | [optional] 
**aws_eks_cluster** | [**ResourceRemoteInfoAwsEksCluster**](ResourceRemoteInfoAwsEksCluster.md) |  | [optional] 
**custom_connector** | [**ResourceRemoteInfoCustomConnector**](ResourceRemoteInfoCustomConnector.md) |  | [optional] 
**gcp_organization** | [**ResourceRemoteInfoGcpOrganization**](ResourceRemoteInfoGcpOrganization.md) |  | [optional] 
**gcp_bucket** | [**ResourceRemoteInfoGcpBucket**](ResourceRemoteInfoGcpBucket.md) |  | [optional] 
**gcp_compute_instance** | [**ResourceRemoteInfoGcpComputeInstance**](ResourceRemoteInfoGcpComputeInstance.md) |  | [optional] 
**gcp_big_query_dataset** | [**ResourceRemoteInfoGcpBigQueryDataset**](ResourceRemoteInfoGcpBigQueryDataset.md) |  | [optional] 
**gcp_big_query_table** | [**ResourceRemoteInfoGcpBigQueryTable**](ResourceRemoteInfoGcpBigQueryTable.md) |  | [optional] 
**gcp_folder** | [**ResourceRemoteInfoGcpFolder**](ResourceRemoteInfoGcpFolder.md) |  | [optional] 
**gcp_gke_cluster** | [**ResourceRemoteInfoGcpGkeCluster**](ResourceRemoteInfoGcpGkeCluster.md) |  | [optional] 
**gcp_project** | [**ResourceRemoteInfoGcpProject**](ResourceRemoteInfoGcpProject.md) |  | [optional] 
**gcp_sql_instance** | [**ResourceRemoteInfoGcpSqlInstance**](ResourceRemoteInfoGcpSqlInstance.md) |  | [optional] 
**gcp_service_account** | [**ResourceRemoteInfoGcpServiceAccount**](ResourceRemoteInfoGcpServiceAccount.md) |  | [optional] 
**google_workspace_role** | [**ResourceRemoteInfoGoogleWorkspaceRole**](ResourceRemoteInfoGoogleWorkspaceRole.md) |  | [optional] 
**github_repo** | [**ResourceRemoteInfoGithubRepo**](ResourceRemoteInfoGithubRepo.md) |  | [optional] 
**github_org_role** | [**ResourceRemoteInfoGithubOrgRole**](ResourceRemoteInfoGithubOrgRole.md) |  | [optional] 
**github_org** | [**ResourceRemoteInfoGithubOrg**](ResourceRemoteInfoGithubOrg.md) |  | [optional] 
**gitlab_project** | [**ResourceRemoteInfoGitlabProject**](ResourceRemoteInfoGitlabProject.md) |  | [optional] 
**okta_app** | [**ResourceRemoteInfoOktaApp**](ResourceRemoteInfoOktaApp.md) |  | [optional] 
**okta_standard_role** | [**ResourceRemoteInfoOktaStandardRole**](ResourceRemoteInfoOktaStandardRole.md) |  | [optional] 
**okta_custom_role** | [**ResourceRemoteInfoOktaCustomRole**](ResourceRemoteInfoOktaCustomRole.md) |  | [optional] 
**snowflake_database** | [**ResourceRemoteInfoSnowflakeDatabase**](ResourceRemoteInfoSnowflakeDatabase.md) |  | [optional] 
**snowflake_schema** | [**ResourceRemoteInfoSnowflakeSchema**](ResourceRemoteInfoSnowflakeSchema.md) |  | [optional] 
**snowflake_table** | [**ResourceRemoteInfoSnowflakeTable**](ResourceRemoteInfoSnowflakeTable.md) |  | [optional] 
**ilevel_advanced_role** | [**ResourceRemoteInfoIlevelAdvancedRole**](ResourceRemoteInfoIlevelAdvancedRole.md) |  | [optional] 
**tailscale_ssh** | [**ResourceRemoteInfoTailscaleSsh**](ResourceRemoteInfoTailscaleSsh.md) |  | [optional] 
**pagerduty_role** | [**ResourceRemoteInfoPagerdutyRole**](ResourceRemoteInfoPagerdutyRole.md) |  | [optional] 
**workday_role** | [**ResourceRemoteInfoWorkdayRole**](ResourceRemoteInfoWorkdayRole.md) |  | [optional] 
**salesforce_permission_set** | [**ResourceRemoteInfoSalesforcePermissionSet**](ResourceRemoteInfoSalesforcePermissionSet.md) |  | [optional] 
**salesforce_profile** | [**ResourceRemoteInfoSalesforceProfile**](ResourceRemoteInfoSalesforceProfile.md) |  | [optional] 
**salesforce_role** | [**ResourceRemoteInfoSalesforceRole**](ResourceRemoteInfoSalesforceRole.md) |  | [optional] 
**teleport_role** | [**ResourceRemoteInfoTeleportRole**](ResourceRemoteInfoTeleportRole.md) |  | [optional] 
**datastax_astra_role** | [**ResourceRemoteInfoDatastaxAstraRole**](ResourceRemoteInfoDatastaxAstraRole.md) |  | [optional] 
**coupa_role** | [**ResourceRemoteInfoCoupaRole**](ResourceRemoteInfoCoupaRole.md) |  | [optional] 
**cursor_organization** | [**ResourceRemoteInfoCursorOrganization**](ResourceRemoteInfoCursorOrganization.md) |  | [optional] 
**openai_platform_project** | [**ResourceRemoteInfoOpenaiPlatformProject**](ResourceRemoteInfoOpenaiPlatformProject.md) |  | [optional] 
**openai_platform_service_account** | [**ResourceRemoteInfoOpenaiPlatformServiceAccount**](ResourceRemoteInfoOpenaiPlatformServiceAccount.md) |  | [optional] 
**anthropic_workspace** | [**ResourceRemoteInfoAnthropicWorkspace**](ResourceRemoteInfoAnthropicWorkspace.md) |  | [optional] 
**oracle_fusion_role** | [**ResourceRemoteInfoOracleFusionRole**](ResourceRemoteInfoOracleFusionRole.md) |  | [optional] 

## Example

```python
from opal_security.models.resource_remote_info import ResourceRemoteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfo from a JSON string
resource_remote_info_instance = ResourceRemoteInfo.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfo.to_json())

# convert the object into a dict
resource_remote_info_dict = resource_remote_info_instance.to_dict()
# create an instance of ResourceRemoteInfo from a dict
resource_remote_info_from_dict = ResourceRemoteInfo.from_dict(resource_remote_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


