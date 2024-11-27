# ResourceRemoteInfoAwsEksCluster

Remote info for AWS EKS cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** | The ARN of the EKS cluster. | 
**account_id** | **str** | The id of the AWS account. Required for AWS Organizations. | [optional] 

## Example

```python
from opal_security.models.resource_remote_info_aws_eks_cluster import ResourceRemoteInfoAwsEksCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAwsEksCluster from a JSON string
resource_remote_info_aws_eks_cluster_instance = ResourceRemoteInfoAwsEksCluster.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAwsEksCluster.to_json())

# convert the object into a dict
resource_remote_info_aws_eks_cluster_dict = resource_remote_info_aws_eks_cluster_instance.to_dict()
# create an instance of ResourceRemoteInfoAwsEksCluster from a dict
resource_remote_info_aws_eks_cluster_from_dict = ResourceRemoteInfoAwsEksCluster.from_dict(resource_remote_info_aws_eks_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


