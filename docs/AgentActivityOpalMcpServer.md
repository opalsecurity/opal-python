# AgentActivityOpalMcpServer

# AgentActivityOpalMcpServer Object ### Description Where the MCP server behind a tool call connects, as the Opal hook kit read it from the developer's own Claude Code configuration. Claude Code's hook payload names the server but not where it connects, so the kit adds this for an `mcp__<server>__<tool>` call when it finds the server in the configuration.  Opal uses it to identify the server in the organization's MCP server registry: by its URL, or by the hash of its command. The URL is stored without its query, fragment or user name and password.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The server&#39;s URL, for an &#x60;http&#x60; or &#x60;sse&#x60; server. | [optional] 
**transport** | **str** | &#x60;http&#x60;, &#x60;sse&#x60; or &#x60;stdio&#x60;. | [optional] 
**command_hash** | **str** | For a &#x60;stdio&#x60; server, a SHA-256 of its command&#39;s shape, in hex. Arguments that can hold a secret are replaced before hashing, and the command itself is never sent. | [optional] 
**scope** | **str** | The configuration the server was found in, such as &#x60;user&#x60;, &#x60;project&#x60;, &#x60;local&#x60;, &#x60;managed&#x60; or &#x60;plugin&#x60;. | [optional] 

## Example

```python
from opal_security.models.agent_activity_opal_mcp_server import AgentActivityOpalMcpServer

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivityOpalMcpServer from a JSON string
agent_activity_opal_mcp_server_instance = AgentActivityOpalMcpServer.from_json(json)
# print the JSON string representation of the object
print(AgentActivityOpalMcpServer.to_json())

# convert the object into a dict
agent_activity_opal_mcp_server_dict = agent_activity_opal_mcp_server_instance.to_dict()
# create an instance of AgentActivityOpalMcpServer from a dict
agent_activity_opal_mcp_server_from_dict = AgentActivityOpalMcpServer.from_dict(agent_activity_opal_mcp_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


