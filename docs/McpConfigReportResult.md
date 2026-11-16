# McpConfigReportResult

# McpConfigReportResult Object ### Description What one configuration report did.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**received** | **int** | Servers in the report. | 
**recorded** | **int** | Servers recorded in the registry. Lower than &#x60;received&#x60; when an entry had neither a name Opal could use nor a URL or command hash. | 

## Example

```python
from opal_security.models.mcp_config_report_result import McpConfigReportResult

# TODO update the JSON string below
json = "{}"
# create an instance of McpConfigReportResult from a JSON string
mcp_config_report_result_instance = McpConfigReportResult.from_json(json)
# print the JSON string representation of the object
print(McpConfigReportResult.to_json())

# convert the object into a dict
mcp_config_report_result_dict = mcp_config_report_result_instance.to_dict()
# create an instance of McpConfigReportResult from a dict
mcp_config_report_result_from_dict = McpConfigReportResult.from_dict(mcp_config_report_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


