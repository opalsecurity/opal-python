# ResourceRemoteInfoAzureResourceGroup

Remote info for Azure resource group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the resource group. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_resource_group import ResourceRemoteInfoAzureResourceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureResourceGroup from a JSON string
resource_remote_info_azure_resource_group_instance = ResourceRemoteInfoAzureResourceGroup.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureResourceGroup.to_json())

# convert the object into a dict
resource_remote_info_azure_resource_group_dict = resource_remote_info_azure_resource_group_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureResourceGroup from a dict
resource_remote_info_azure_resource_group_from_dict = ResourceRemoteInfoAzureResourceGroup.from_dict(resource_remote_info_azure_resource_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


