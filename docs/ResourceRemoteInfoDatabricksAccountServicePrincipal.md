# ResourceRemoteInfoDatabricksAccountServicePrincipal

Remote info for Databricks account service principal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The application ID of the service principal. | 
**resource_id** | **str** | The resource ID of the service principal. | 

## Example

```python
from opal_security.models.resource_remote_info_databricks_account_service_principal import ResourceRemoteInfoDatabricksAccountServicePrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoDatabricksAccountServicePrincipal from a JSON string
resource_remote_info_databricks_account_service_principal_instance = ResourceRemoteInfoDatabricksAccountServicePrincipal.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoDatabricksAccountServicePrincipal.to_json())

# convert the object into a dict
resource_remote_info_databricks_account_service_principal_dict = resource_remote_info_databricks_account_service_principal_instance.to_dict()
# create an instance of ResourceRemoteInfoDatabricksAccountServicePrincipal from a dict
resource_remote_info_databricks_account_service_principal_from_dict = ResourceRemoteInfoDatabricksAccountServicePrincipal.from_dict(resource_remote_info_databricks_account_service_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


