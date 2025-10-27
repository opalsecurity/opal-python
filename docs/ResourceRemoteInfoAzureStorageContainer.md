# ResourceRemoteInfoAzureStorageContainer

Remote info for Azure storage container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the storage container. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_storage_container import ResourceRemoteInfoAzureStorageContainer

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureStorageContainer from a JSON string
resource_remote_info_azure_storage_container_instance = ResourceRemoteInfoAzureStorageContainer.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureStorageContainer.to_json())

# convert the object into a dict
resource_remote_info_azure_storage_container_dict = resource_remote_info_azure_storage_container_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureStorageContainer from a dict
resource_remote_info_azure_storage_container_from_dict = ResourceRemoteInfoAzureStorageContainer.from_dict(resource_remote_info_azure_storage_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


