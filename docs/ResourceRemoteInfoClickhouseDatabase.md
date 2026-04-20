# ResourceRemoteInfoClickhouseDatabase

Remote info for ClickHouse database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_name** | **str** | The name of the ClickHouse database. | 

## Example

```python
from opal_security.models.resource_remote_info_clickhouse_database import ResourceRemoteInfoClickhouseDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoClickhouseDatabase from a JSON string
resource_remote_info_clickhouse_database_instance = ResourceRemoteInfoClickhouseDatabase.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoClickhouseDatabase.to_json())

# convert the object into a dict
resource_remote_info_clickhouse_database_dict = resource_remote_info_clickhouse_database_instance.to_dict()
# create an instance of ResourceRemoteInfoClickhouseDatabase from a dict
resource_remote_info_clickhouse_database_from_dict = ResourceRemoteInfoClickhouseDatabase.from_dict(resource_remote_info_clickhouse_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


