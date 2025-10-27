# ResourceRemoteInfoAzureSqlServer

Remote info for Azure SQL server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the SQL server. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_sql_server import ResourceRemoteInfoAzureSqlServer

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureSqlServer from a JSON string
resource_remote_info_azure_sql_server_instance = ResourceRemoteInfoAzureSqlServer.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureSqlServer.to_json())

# convert the object into a dict
resource_remote_info_azure_sql_server_dict = resource_remote_info_azure_sql_server_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureSqlServer from a dict
resource_remote_info_azure_sql_server_from_dict = ResourceRemoteInfoAzureSqlServer.from_dict(resource_remote_info_azure_sql_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


