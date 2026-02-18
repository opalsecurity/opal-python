# ResourceRemoteInfoSnowflakeTable

Remote info for Snowflake table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_name** | **str** | The name of the database the table is in. | 
**schema_name** | **str** | The name of the schema the table is in. | 
**table_name** | **str** | The name of the table. | 

## Example

```python
from opal_security.models.resource_remote_info_snowflake_table import ResourceRemoteInfoSnowflakeTable

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoSnowflakeTable from a JSON string
resource_remote_info_snowflake_table_instance = ResourceRemoteInfoSnowflakeTable.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoSnowflakeTable.to_json())

# convert the object into a dict
resource_remote_info_snowflake_table_dict = resource_remote_info_snowflake_table_instance.to_dict()
# create an instance of ResourceRemoteInfoSnowflakeTable from a dict
resource_remote_info_snowflake_table_from_dict = ResourceRemoteInfoSnowflakeTable.from_dict(resource_remote_info_snowflake_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


