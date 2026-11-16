# ResourceRemoteInfoTrayWorkspace

Remote info for Tray Workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The workspace id of the Tray Workspace. | 

## Example

```python
from opal_security.models.resource_remote_info_tray_workspace import ResourceRemoteInfoTrayWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoTrayWorkspace from a JSON string
resource_remote_info_tray_workspace_instance = ResourceRemoteInfoTrayWorkspace.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoTrayWorkspace.to_json())

# convert the object into a dict
resource_remote_info_tray_workspace_dict = resource_remote_info_tray_workspace_instance.to_dict()
# create an instance of ResourceRemoteInfoTrayWorkspace from a dict
resource_remote_info_tray_workspace_from_dict = ResourceRemoteInfoTrayWorkspace.from_dict(resource_remote_info_tray_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


