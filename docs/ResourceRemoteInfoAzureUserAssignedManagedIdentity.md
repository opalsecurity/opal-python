# ResourceRemoteInfoAzureUserAssignedManagedIdentity

Remote info for Azure user assigned managed identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the user assigned managed identity. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_user_assigned_managed_identity import ResourceRemoteInfoAzureUserAssignedManagedIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureUserAssignedManagedIdentity from a JSON string
resource_remote_info_azure_user_assigned_managed_identity_instance = ResourceRemoteInfoAzureUserAssignedManagedIdentity.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureUserAssignedManagedIdentity.to_json())

# convert the object into a dict
resource_remote_info_azure_user_assigned_managed_identity_dict = resource_remote_info_azure_user_assigned_managed_identity_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureUserAssignedManagedIdentity from a dict
resource_remote_info_azure_user_assigned_managed_identity_from_dict = ResourceRemoteInfoAzureUserAssignedManagedIdentity.from_dict(resource_remote_info_azure_user_assigned_managed_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


