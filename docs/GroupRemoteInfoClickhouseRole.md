# GroupRemoteInfoClickhouseRole

Remote info for ClickHouse role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The name of the ClickHouse role. | 

## Example

```python
from opal_security.models.group_remote_info_clickhouse_role import GroupRemoteInfoClickhouseRole

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoClickhouseRole from a JSON string
group_remote_info_clickhouse_role_instance = GroupRemoteInfoClickhouseRole.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoClickhouseRole.to_json())

# convert the object into a dict
group_remote_info_clickhouse_role_dict = group_remote_info_clickhouse_role_instance.to_dict()
# create an instance of GroupRemoteInfoClickhouseRole from a dict
group_remote_info_clickhouse_role_from_dict = GroupRemoteInfoClickhouseRole.from_dict(group_remote_info_clickhouse_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


