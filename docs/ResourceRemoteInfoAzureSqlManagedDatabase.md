# ResourceRemoteInfoAzureSqlManagedDatabase

Remote info for Azure SQL managed database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the SQL managed database. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_sql_managed_database import ResourceRemoteInfoAzureSqlManagedDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureSqlManagedDatabase from a JSON string
resource_remote_info_azure_sql_managed_database_instance = ResourceRemoteInfoAzureSqlManagedDatabase.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureSqlManagedDatabase.to_json())

# convert the object into a dict
resource_remote_info_azure_sql_managed_database_dict = resource_remote_info_azure_sql_managed_database_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureSqlManagedDatabase from a dict
resource_remote_info_azure_sql_managed_database_from_dict = ResourceRemoteInfoAzureSqlManagedDatabase.from_dict(resource_remote_info_azure_sql_managed_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


