# ResourceRemoteInfoAzureSqlDatabase

Remote info for Azure SQL database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the SQL database. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_sql_database import ResourceRemoteInfoAzureSqlDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureSqlDatabase from a JSON string
resource_remote_info_azure_sql_database_instance = ResourceRemoteInfoAzureSqlDatabase.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureSqlDatabase.to_json())

# convert the object into a dict
resource_remote_info_azure_sql_database_dict = resource_remote_info_azure_sql_database_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureSqlDatabase from a dict
resource_remote_info_azure_sql_database_from_dict = ResourceRemoteInfoAzureSqlDatabase.from_dict(resource_remote_info_azure_sql_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


