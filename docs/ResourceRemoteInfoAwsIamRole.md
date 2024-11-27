# ResourceRemoteInfoAwsIamRole

Remote info for AWS IAM role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** | The ARN of the IAM role. | 
**account_id** | **str** | The id of the AWS account. Required for AWS Organizations. | [optional] 

## Example

```python
from opal_security.models.resource_remote_info_aws_iam_role import ResourceRemoteInfoAwsIamRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAwsIamRole from a JSON string
resource_remote_info_aws_iam_role_instance = ResourceRemoteInfoAwsIamRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAwsIamRole.to_json())

# convert the object into a dict
resource_remote_info_aws_iam_role_dict = resource_remote_info_aws_iam_role_instance.to_dict()
# create an instance of ResourceRemoteInfoAwsIamRole from a dict
resource_remote_info_aws_iam_role_from_dict = ResourceRemoteInfoAwsIamRole.from_dict(resource_remote_info_aws_iam_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


