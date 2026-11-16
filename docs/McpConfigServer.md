# McpConfigServer

# McpConfigServer Object ### Description One MCP server in a machine's Claude Code configuration. Exactly what the hook kit sends: no environment values, headers or command arguments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The server&#39;s name in the configuration. | 
**scope** | **str** | &#x60;user&#x60;, &#x60;project&#x60;, &#x60;local&#x60;, &#x60;managed&#x60; or &#x60;plugin&#x60;. | [optional] 
**transport** | **str** | &#x60;http&#x60;, &#x60;sse&#x60; or &#x60;stdio&#x60;. | [optional] 
**url** | **str** | The server&#39;s URL, for an &#x60;http&#x60; or &#x60;sse&#x60; server. | [optional] 
**command_hash** | **str** | For a &#x60;stdio&#x60; server, a SHA-256 of its command&#39;s shape, in hex. | [optional] 

## Example

```python
from opal_security.models.mcp_config_server import McpConfigServer

# TODO update the JSON string below
json = "{}"
# create an instance of McpConfigServer from a JSON string
mcp_config_server_instance = McpConfigServer.from_json(json)
# print the JSON string representation of the object
print(McpConfigServer.to_json())

# convert the object into a dict
mcp_config_server_dict = mcp_config_server_instance.to_dict()
# create an instance of McpConfigServer from a dict
mcp_config_server_from_dict = McpConfigServer.from_dict(mcp_config_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


