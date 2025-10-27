# ResourceRemoteInfoAzureManagementGroup

Remote info for Azure management group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the management group. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_management_group import ResourceRemoteInfoAzureManagementGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureManagementGroup from a JSON string
resource_remote_info_azure_management_group_instance = ResourceRemoteInfoAzureManagementGroup.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureManagementGroup.to_json())

# convert the object into a dict
resource_remote_info_azure_management_group_dict = resource_remote_info_azure_management_group_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureManagementGroup from a dict
resource_remote_info_azure_management_group_from_dict = ResourceRemoteInfoAzureManagementGroup.from_dict(resource_remote_info_azure_management_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


