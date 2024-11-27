# ResourceRemoteInfo

Information that defines the remote resource. This replaces the deprecated remote_id and metadata fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_account** | [**ResourceRemoteInfoAwsAccount**](ResourceRemoteInfoAwsAccount.md) |  | [optional] 
**aws_permission_set** | [**ResourceRemoteInfoAwsPermissionSet**](ResourceRemoteInfoAwsPermissionSet.md) |  | [optional] 
**aws_iam_role** | [**ResourceRemoteInfoAwsIamRole**](ResourceRemoteInfoAwsIamRole.md) |  | [optional] 
**aws_ec2_instance** | [**ResourceRemoteInfoAwsEc2Instance**](ResourceRemoteInfoAwsEc2Instance.md) |  | [optional] 
**aws_rds_instance** | [**ResourceRemoteInfoAwsRdsInstance**](ResourceRemoteInfoAwsRdsInstance.md) |  | [optional] 
**aws_eks_cluster** | [**ResourceRemoteInfoAwsEksCluster**](ResourceRemoteInfoAwsEksCluster.md) |  | [optional] 
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
**github_repo** | [**ResourceRemoteInfoGithubRepo**](ResourceRemoteInfoGithubRepo.md) |  | [optional] 
**gitlab_project** | [**ResourceRemoteInfoGitlabProject**](ResourceRemoteInfoGitlabProject.md) |  | [optional] 
**okta_app** | [**ResourceRemoteInfoOktaApp**](ResourceRemoteInfoOktaApp.md) |  | [optional] 
**okta_standard_role** | [**ResourceRemoteInfoOktaStandardRole**](ResourceRemoteInfoOktaStandardRole.md) |  | [optional] 
**okta_custom_role** | [**ResourceRemoteInfoOktaCustomRole**](ResourceRemoteInfoOktaCustomRole.md) |  | [optional] 
**pagerduty_role** | [**ResourceRemoteInfoPagerdutyRole**](ResourceRemoteInfoPagerdutyRole.md) |  | [optional] 
**salesforce_permission_set** | [**ResourceRemoteInfoSalesforcePermissionSet**](ResourceRemoteInfoSalesforcePermissionSet.md) |  | [optional] 
**salesforce_profile** | [**ResourceRemoteInfoSalesforceProfile**](ResourceRemoteInfoSalesforceProfile.md) |  | [optional] 
**salesforce_role** | [**ResourceRemoteInfoSalesforceRole**](ResourceRemoteInfoSalesforceRole.md) |  | [optional] 
**teleport_role** | [**ResourceRemoteInfoTeleportRole**](ResourceRemoteInfoTeleportRole.md) |  | [optional] 

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


