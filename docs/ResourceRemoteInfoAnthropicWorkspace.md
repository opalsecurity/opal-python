# ResourceRemoteInfoAnthropicWorkspace

Remote info for Anthropic workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The id of the workspace. | 

## Example

```python
from opal_security.models.resource_remote_info_anthropic_workspace import ResourceRemoteInfoAnthropicWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAnthropicWorkspace from a JSON string
resource_remote_info_anthropic_workspace_instance = ResourceRemoteInfoAnthropicWorkspace.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAnthropicWorkspace.to_json())

# convert the object into a dict
resource_remote_info_anthropic_workspace_dict = resource_remote_info_anthropic_workspace_instance.to_dict()
# create an instance of ResourceRemoteInfoAnthropicWorkspace from a dict
resource_remote_info_anthropic_workspace_from_dict = ResourceRemoteInfoAnthropicWorkspace.from_dict(resource_remote_info_anthropic_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


