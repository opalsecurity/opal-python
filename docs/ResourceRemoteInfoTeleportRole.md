# ResourceRemoteInfoTeleportRole

Remote info for Teleport role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | The name role. | 

## Example

```python
from opal_security.models.resource_remote_info_teleport_role import ResourceRemoteInfoTeleportRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoTeleportRole from a JSON string
resource_remote_info_teleport_role_instance = ResourceRemoteInfoTeleportRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoTeleportRole.to_json())

# convert the object into a dict
resource_remote_info_teleport_role_dict = resource_remote_info_teleport_role_instance.to_dict()
# create an instance of ResourceRemoteInfoTeleportRole from a dict
resource_remote_info_teleport_role_from_dict = ResourceRemoteInfoTeleportRole.from_dict(resource_remote_info_teleport_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


