# ResourceRemoteInfoAwsAccount

Remote info for AWS account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The id of the AWS account. | 

## Example

```python
from opal_security.models.resource_remote_info_aws_account import ResourceRemoteInfoAwsAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAwsAccount from a JSON string
resource_remote_info_aws_account_instance = ResourceRemoteInfoAwsAccount.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAwsAccount.to_json())

# convert the object into a dict
resource_remote_info_aws_account_dict = resource_remote_info_aws_account_instance.to_dict()
# create an instance of ResourceRemoteInfoAwsAccount from a dict
resource_remote_info_aws_account_from_dict = ResourceRemoteInfoAwsAccount.from_dict(resource_remote_info_aws_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


