# ResourceRemoteInfoAzureStorageAccount

Remote info for Azure storage account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the storage account. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_storage_account import ResourceRemoteInfoAzureStorageAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureStorageAccount from a JSON string
resource_remote_info_azure_storage_account_instance = ResourceRemoteInfoAzureStorageAccount.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureStorageAccount.to_json())

# convert the object into a dict
resource_remote_info_azure_storage_account_dict = resource_remote_info_azure_storage_account_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureStorageAccount from a dict
resource_remote_info_azure_storage_account_from_dict = ResourceRemoteInfoAzureStorageAccount.from_dict(resource_remote_info_azure_storage_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


