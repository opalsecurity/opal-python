# ResourceRemoteInfoAzureEntraIdRole

Remote info for Azure Entra ID role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The remote role identifier from Entra (object ID). | 

## Example

```python
from opal_security.models.resource_remote_info_azure_entra_id_role import ResourceRemoteInfoAzureEntraIdRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureEntraIdRole from a JSON string
resource_remote_info_azure_entra_id_role_instance = ResourceRemoteInfoAzureEntraIdRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureEntraIdRole.to_json())

# convert the object into a dict
resource_remote_info_azure_entra_id_role_dict = resource_remote_info_azure_entra_id_role_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureEntraIdRole from a dict
resource_remote_info_azure_entra_id_role_from_dict = ResourceRemoteInfoAzureEntraIdRole.from_dict(resource_remote_info_azure_entra_id_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


