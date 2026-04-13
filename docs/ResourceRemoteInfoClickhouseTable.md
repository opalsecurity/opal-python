# ResourceRemoteInfoClickhouseTable

Remote info for ClickHouse table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_name** | **str** | The name of the ClickHouse database containing the table. | 
**table_name** | **str** | The name of the ClickHouse table. | 

## Example

```python
from opal_security.models.resource_remote_info_clickhouse_table import ResourceRemoteInfoClickhouseTable

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoClickhouseTable from a JSON string
resource_remote_info_clickhouse_table_instance = ResourceRemoteInfoClickhouseTable.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoClickhouseTable.to_json())

# convert the object into a dict
resource_remote_info_clickhouse_table_dict = resource_remote_info_clickhouse_table_instance.to_dict()
# create an instance of ResourceRemoteInfoClickhouseTable from a dict
resource_remote_info_clickhouse_table_from_dict = ResourceRemoteInfoClickhouseTable.from_dict(resource_remote_info_clickhouse_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


