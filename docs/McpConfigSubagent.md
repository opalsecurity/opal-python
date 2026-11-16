# McpConfigSubagent

# McpConfigSubagent Object ### Description A custom subagent defined on the machine. A plugin's is named `<plugin>:<name>`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**scope** | **str** | &#x60;user&#x60;, &#x60;project&#x60;, &#x60;plugin&#x60; or &#x60;managed&#x60;. | [optional] 
**tools** | **List[str]** | The tools its file lists. Absent when the file lists none, which lets the subagent use every tool of the session, MCP tools included. | [optional] 

## Example

```python
from opal_security.models.mcp_config_subagent import McpConfigSubagent

# TODO update the JSON string below
json = "{}"
# create an instance of McpConfigSubagent from a JSON string
mcp_config_subagent_instance = McpConfigSubagent.from_json(json)
# print the JSON string representation of the object
print(McpConfigSubagent.to_json())

# convert the object into a dict
mcp_config_subagent_dict = mcp_config_subagent_instance.to_dict()
# create an instance of McpConfigSubagent from a dict
mcp_config_subagent_from_dict = McpConfigSubagent.from_dict(mcp_config_subagent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


