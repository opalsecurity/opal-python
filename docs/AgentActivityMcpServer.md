# AgentActivityMcpServer

# AgentActivityMcpServer Object ### Description The MCP server behind a tool call, as Claude Code reports it. Claude Code v2.1.274 and later adds this object to the hook input of an MCP tool call; an older client does not send it, and it is never present for a built-in tool such as `Bash`.  When `name` is present it is stored as the call's server. When this object is absent, the server is read from `tool_name` instead: the part after the `mcp__` prefix and before the next `__`. The tool is always read from `tool_name`.  Only `name` is read. `source` says where the server's definition came from (`plugin`, `sdk`, or a configuration scope such as `user` or `project`) and is parsed and **discarded**. Neither field is an identity: `name` is whatever the user called the server in their own configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The server&#39;s name. | [optional] 
**source** | **str** | Where the server&#39;s definition came from, such as &#x60;plugin&#x60;, &#x60;sdk&#x60;, &#x60;user&#x60; or &#x60;project&#x60;. Not stored. | [optional] 

## Example

```python
from opal_security.models.agent_activity_mcp_server import AgentActivityMcpServer

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivityMcpServer from a JSON string
agent_activity_mcp_server_instance = AgentActivityMcpServer.from_json(json)
# print the JSON string representation of the object
print(AgentActivityMcpServer.to_json())

# convert the object into a dict
agent_activity_mcp_server_dict = agent_activity_mcp_server_instance.to_dict()
# create an instance of AgentActivityMcpServer from a dict
agent_activity_mcp_server_from_dict = AgentActivityMcpServer.from_dict(agent_activity_mcp_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


