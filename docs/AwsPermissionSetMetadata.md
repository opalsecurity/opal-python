# AwsPermissionSetMetadata

Metadata for AWS Identity Center permission set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_permission_set** | [**AwsPermissionSetMetadataAwsPermissionSet**](AwsPermissionSetMetadataAwsPermissionSet.md) |  | 

## Example

```python
from opal_security.models.aws_permission_set_metadata import AwsPermissionSetMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AwsPermissionSetMetadata from a JSON string
aws_permission_set_metadata_instance = AwsPermissionSetMetadata.from_json(json)
# print the JSON string representation of the object
print(AwsPermissionSetMetadata.to_json())

# convert the object into a dict
aws_permission_set_metadata_dict = aws_permission_set_metadata_instance.to_dict()
# create an instance of AwsPermissionSetMetadata from a dict
aws_permission_set_metadata_from_dict = AwsPermissionSetMetadata.from_dict(aws_permission_set_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


