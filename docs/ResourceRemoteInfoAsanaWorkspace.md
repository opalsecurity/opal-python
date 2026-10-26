# ResourceRemoteInfoAsanaWorkspace

Remote info for Asana Workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_gid** | **str** | The workspace gid of the Asana Workspace. | 

## Example

```python
from opal_security.models.resource_remote_info_asana_workspace import ResourceRemoteInfoAsanaWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAsanaWorkspace from a JSON string
resource_remote_info_asana_workspace_instance = ResourceRemoteInfoAsanaWorkspace.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAsanaWorkspace.to_json())

# convert the object into a dict
resource_remote_info_asana_workspace_dict = resource_remote_info_asana_workspace_instance.to_dict()
# create an instance of ResourceRemoteInfoAsanaWorkspace from a dict
resource_remote_info_asana_workspace_from_dict = ResourceRemoteInfoAsanaWorkspace.from_dict(resource_remote_info_asana_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


