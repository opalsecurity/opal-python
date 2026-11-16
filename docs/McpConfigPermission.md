# McpConfigPermission

# McpConfigPermission Object ### Description One permission rule or default mode of one settings source. The kit masks secrets in a rule with the same redaction it uses for conversation content, and Opal masks it again.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | &#x60;managed&#x60;, &#x60;user&#x60;, &#x60;project&#x60; or &#x60;local&#x60;. | [optional] 
**kind** | **str** | &#x60;allow&#x60;, &#x60;ask&#x60;, &#x60;deny&#x60; or &#x60;default_mode&#x60;. | 
**value** | **str** | The rule, such as &#x60;Bash(npm run test *)&#x60;, or the mode, such as &#x60;acceptEdits&#x60;. | 

## Example

```python
from opal_security.models.mcp_config_permission import McpConfigPermission

# TODO update the JSON string below
json = "{}"
# create an instance of McpConfigPermission from a JSON string
mcp_config_permission_instance = McpConfigPermission.from_json(json)
# print the JSON string representation of the object
print(McpConfigPermission.to_json())

# convert the object into a dict
mcp_config_permission_dict = mcp_config_permission_instance.to_dict()
# create an instance of McpConfigPermission from a dict
mcp_config_permission_from_dict = McpConfigPermission.from_dict(mcp_config_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


