# ResourceRemoteInfoAwsRdsCluster

Remote info for AWS RDS cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The clusterId of the RDS cluster. | 
**region** | **str** | The region of the RDS cluster. | 
**resource_id** | **str** | The resourceId of the RDS cluster. | 
**account_id** | **str** | The id of the AWS account. Required for AWS Organizations. | 
**database_name** | **str** | The name of the database in the RDS cluster. This can be the value of the tag &#x60;opal:database-name&#x60; or the database name. | 
**engine** | [**RDSEngineEnum**](RDSEngineEnum.md) |  | 

## Example

```python
from opal_security.models.resource_remote_info_aws_rds_cluster import ResourceRemoteInfoAwsRdsCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAwsRdsCluster from a JSON string
resource_remote_info_aws_rds_cluster_instance = ResourceRemoteInfoAwsRdsCluster.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAwsRdsCluster.to_json())

# convert the object into a dict
resource_remote_info_aws_rds_cluster_dict = resource_remote_info_aws_rds_cluster_instance.to_dict()
# create an instance of ResourceRemoteInfoAwsRdsCluster from a dict
resource_remote_info_aws_rds_cluster_from_dict = ResourceRemoteInfoAwsRdsCluster.from_dict(resource_remote_info_aws_rds_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


