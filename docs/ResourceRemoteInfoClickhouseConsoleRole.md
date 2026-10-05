# ResourceRemoteInfoClickhouseConsoleRole

Remote info for ClickHouse Cloud console role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The UUID of the ClickHouse Cloud console role. | 

## Example

```python
from opal_security.models.resource_remote_info_clickhouse_console_role import ResourceRemoteInfoClickhouseConsoleRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoClickhouseConsoleRole from a JSON string
resource_remote_info_clickhouse_console_role_instance = ResourceRemoteInfoClickhouseConsoleRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoClickhouseConsoleRole.to_json())

# convert the object into a dict
resource_remote_info_clickhouse_console_role_dict = resource_remote_info_clickhouse_console_role_instance.to_dict()
# create an instance of ResourceRemoteInfoClickhouseConsoleRole from a dict
resource_remote_info_clickhouse_console_role_from_dict = ResourceRemoteInfoClickhouseConsoleRole.from_dict(resource_remote_info_clickhouse_console_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


