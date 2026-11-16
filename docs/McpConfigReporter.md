# McpConfigReporter

# McpConfigReporter Object ### Description Who the reporting machine says it belongs to. Unverified, like `X-Opal-Actor`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured_email** | **str** |  | [optional] 
**claude_account_email** | **str** |  | [optional] 
**git_email** | **str** |  | [optional] 
**os_user** | **str** |  | [optional] 

## Example

```python
from opal_security.models.mcp_config_reporter import McpConfigReporter

# TODO update the JSON string below
json = "{}"
# create an instance of McpConfigReporter from a JSON string
mcp_config_reporter_instance = McpConfigReporter.from_json(json)
# print the JSON string representation of the object
print(McpConfigReporter.to_json())

# convert the object into a dict
mcp_config_reporter_dict = mcp_config_reporter_instance.to_dict()
# create an instance of McpConfigReporter from a dict
mcp_config_reporter_from_dict = McpConfigReporter.from_dict(mcp_config_reporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


