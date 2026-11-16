# McpConfigSkill

# McpConfigSkill Object ### Description A skill (or legacy command) Claude Code loads on the machine. A plugin's is named `<plugin>:<name>`. Only its name is sent, never the file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**source** | **str** | &#x60;user&#x60;, &#x60;project&#x60;, &#x60;plugin&#x60; or &#x60;managed&#x60;. | [optional] 

## Example

```python
from opal_security.models.mcp_config_skill import McpConfigSkill

# TODO update the JSON string below
json = "{}"
# create an instance of McpConfigSkill from a JSON string
mcp_config_skill_instance = McpConfigSkill.from_json(json)
# print the JSON string representation of the object
print(McpConfigSkill.to_json())

# convert the object into a dict
mcp_config_skill_dict = mcp_config_skill_instance.to_dict()
# create an instance of McpConfigSkill from a dict
mcp_config_skill_from_dict = McpConfigSkill.from_dict(mcp_config_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


