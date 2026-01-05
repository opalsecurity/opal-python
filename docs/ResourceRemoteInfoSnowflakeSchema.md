# ResourceRemoteInfoSnowflakeSchema

Remote info for Snowflake schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_name** | **str** | The name of the database the schema is in. | 
**schema_name** | **str** | The name of the schema. | 

## Example

```python
from opal_security.models.resource_remote_info_snowflake_schema import ResourceRemoteInfoSnowflakeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoSnowflakeSchema from a JSON string
resource_remote_info_snowflake_schema_instance = ResourceRemoteInfoSnowflakeSchema.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoSnowflakeSchema.to_json())

# convert the object into a dict
resource_remote_info_snowflake_schema_dict = resource_remote_info_snowflake_schema_instance.to_dict()
# create an instance of ResourceRemoteInfoSnowflakeSchema from a dict
resource_remote_info_snowflake_schema_from_dict = ResourceRemoteInfoSnowflakeSchema.from_dict(resource_remote_info_snowflake_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


