# ResourceRemoteInfoAwsPermissionSet

Remote info for AWS Identity Center permission set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** | The ARN of the permission set. | 
**account_id** | **str** | The ID of an AWS account to which this permission set is provisioned. | 

## Example

```python
from opal_security.models.resource_remote_info_aws_permission_set import ResourceRemoteInfoAwsPermissionSet

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAwsPermissionSet from a JSON string
resource_remote_info_aws_permission_set_instance = ResourceRemoteInfoAwsPermissionSet.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAwsPermissionSet.to_json())

# convert the object into a dict
resource_remote_info_aws_permission_set_dict = resource_remote_info_aws_permission_set_instance.to_dict()
# create an instance of ResourceRemoteInfoAwsPermissionSet from a dict
resource_remote_info_aws_permission_set_from_dict = ResourceRemoteInfoAwsPermissionSet.from_dict(resource_remote_info_aws_permission_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


