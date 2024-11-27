# AwsPermissionSetMetadataAwsPermissionSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** | The ARN of the permission set. | 
**account_id** | **str** | The ID of an AWS account to which this permission set is provisioned. | 

## Example

```python
from opal_security.models.aws_permission_set_metadata_aws_permission_set import AwsPermissionSetMetadataAwsPermissionSet

# TODO update the JSON string below
json = "{}"
# create an instance of AwsPermissionSetMetadataAwsPermissionSet from a JSON string
aws_permission_set_metadata_aws_permission_set_instance = AwsPermissionSetMetadataAwsPermissionSet.from_json(json)
# print the JSON string representation of the object
print(AwsPermissionSetMetadataAwsPermissionSet.to_json())

# convert the object into a dict
aws_permission_set_metadata_aws_permission_set_dict = aws_permission_set_metadata_aws_permission_set_instance.to_dict()
# create an instance of AwsPermissionSetMetadataAwsPermissionSet from a dict
aws_permission_set_metadata_aws_permission_set_from_dict = AwsPermissionSetMetadataAwsPermissionSet.from_dict(aws_permission_set_metadata_aws_permission_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


