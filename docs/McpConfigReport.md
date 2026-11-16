# McpConfigReport

# McpConfigReport Object ### Description The MCP servers configured in Claude Code on one machine, and what else its configuration lets Claude Code reach: enabled plugins, skills, custom subagents and permission rules. Each of those four lists is optional; a kit that does not send one leaves what Opal has of that kind as it is, and an empty list says the machine has none. Each holds at most 200 entries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | [**List[McpConfigServer]**](McpConfigServer.md) |  | 
**reporter** | [**McpConfigReporter**](McpConfigReporter.md) |  | [optional] 
**plugins** | [**List[McpConfigPlugin]**](McpConfigPlugin.md) |  | [optional] 
**skills** | [**List[McpConfigSkill]**](McpConfigSkill.md) |  | [optional] 
**subagents** | [**List[McpConfigSubagent]**](McpConfigSubagent.md) |  | [optional] 
**permissions** | [**List[McpConfigPermission]**](McpConfigPermission.md) |  | [optional] 

## Example

```python
from opal_security.models.mcp_config_report import McpConfigReport

# TODO update the JSON string below
json = "{}"
# create an instance of McpConfigReport from a JSON string
mcp_config_report_instance = McpConfigReport.from_json(json)
# print the JSON string representation of the object
print(McpConfigReport.to_json())

# convert the object into a dict
mcp_config_report_dict = mcp_config_report_instance.to_dict()
# create an instance of McpConfigReport from a dict
mcp_config_report_from_dict = McpConfigReport.from_dict(mcp_config_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


