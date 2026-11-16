# McpConfigPlugin

# McpConfigPlugin Object ### Description A Claude Code plugin the machine's settings enable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**marketplace** | **str** |  | [optional] 
**version** | **str** | The installed version, when the kit could read it. | [optional] 
**scope** | **str** | The settings source that enables it: &#x60;managed&#x60;, &#x60;user&#x60;, &#x60;project&#x60; or &#x60;local&#x60;. | [optional] 

## Example

```python
from opal_security.models.mcp_config_plugin import McpConfigPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of McpConfigPlugin from a JSON string
mcp_config_plugin_instance = McpConfigPlugin.from_json(json)
# print the JSON string representation of the object
print(McpConfigPlugin.to_json())

# convert the object into a dict
mcp_config_plugin_dict = mcp_config_plugin_instance.to_dict()
# create an instance of McpConfigPlugin from a dict
mcp_config_plugin_from_dict = McpConfigPlugin.from_dict(mcp_config_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


