# GroupRemoteInfoSnowflakeRole

Remote info for Snowflake role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The id of the Snowflake role. | 

## Example

```python
from opal_security.models.group_remote_info_snowflake_role import GroupRemoteInfoSnowflakeRole

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoSnowflakeRole from a JSON string
group_remote_info_snowflake_role_instance = GroupRemoteInfoSnowflakeRole.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoSnowflakeRole.to_json())

# convert the object into a dict
group_remote_info_snowflake_role_dict = group_remote_info_snowflake_role_instance.to_dict()
# create an instance of GroupRemoteInfoSnowflakeRole from a dict
group_remote_info_snowflake_role_from_dict = GroupRemoteInfoSnowflakeRole.from_dict(group_remote_info_snowflake_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


