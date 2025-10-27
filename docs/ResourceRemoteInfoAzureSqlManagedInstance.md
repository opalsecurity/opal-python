# ResourceRemoteInfoAzureSqlManagedInstance

Remote info for Azure SQL managed instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the SQL managed instance. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_sql_managed_instance import ResourceRemoteInfoAzureSqlManagedInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureSqlManagedInstance from a JSON string
resource_remote_info_azure_sql_managed_instance_instance = ResourceRemoteInfoAzureSqlManagedInstance.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureSqlManagedInstance.to_json())

# convert the object into a dict
resource_remote_info_azure_sql_managed_instance_dict = resource_remote_info_azure_sql_managed_instance_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureSqlManagedInstance from a dict
resource_remote_info_azure_sql_managed_instance_from_dict = ResourceRemoteInfoAzureSqlManagedInstance.from_dict(resource_remote_info_azure_sql_managed_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


