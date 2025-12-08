# ResourceRemoteInfoSnowflakeDatabase

Remote info for Snowflake database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_name** | **str** | The name of the database. | 

## Example

```python
from opal_security.models.resource_remote_info_snowflake_database import ResourceRemoteInfoSnowflakeDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoSnowflakeDatabase from a JSON string
resource_remote_info_snowflake_database_instance = ResourceRemoteInfoSnowflakeDatabase.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoSnowflakeDatabase.to_json())

# convert the object into a dict
resource_remote_info_snowflake_database_dict = resource_remote_info_snowflake_database_instance.to_dict()
# create an instance of ResourceRemoteInfoSnowflakeDatabase from a dict
resource_remote_info_snowflake_database_from_dict = ResourceRemoteInfoSnowflakeDatabase.from_dict(resource_remote_info_snowflake_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


