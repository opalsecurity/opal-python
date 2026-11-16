# ResourceRemoteInfoSlackWorkspace

Remote info for Slack workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the Slack workspace (team ID). | 

## Example

```python
from opal_security.models.resource_remote_info_slack_workspace import ResourceRemoteInfoSlackWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoSlackWorkspace from a JSON string
resource_remote_info_slack_workspace_instance = ResourceRemoteInfoSlackWorkspace.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoSlackWorkspace.to_json())

# convert the object into a dict
resource_remote_info_slack_workspace_dict = resource_remote_info_slack_workspace_instance.to_dict()
# create an instance of ResourceRemoteInfoSlackWorkspace from a dict
resource_remote_info_slack_workspace_from_dict = ResourceRemoteInfoSlackWorkspace.from_dict(resource_remote_info_slack_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


