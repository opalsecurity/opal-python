# ResourceRemoteInfoDatabricksService

Remote info for Databricks AI Gateway service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metastore_id** | **str** | The ID of the Unity Catalog metastore the service belongs to. | 
**full_name** | **str** | The dot-qualified full name of the service (e.g. \&quot;catalog.schema.service\&quot;). | 

## Example

```python
from opal_security.models.resource_remote_info_databricks_service import ResourceRemoteInfoDatabricksService

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoDatabricksService from a JSON string
resource_remote_info_databricks_service_instance = ResourceRemoteInfoDatabricksService.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoDatabricksService.to_json())

# convert the object into a dict
resource_remote_info_databricks_service_dict = resource_remote_info_databricks_service_instance.to_dict()
# create an instance of ResourceRemoteInfoDatabricksService from a dict
resource_remote_info_databricks_service_from_dict = ResourceRemoteInfoDatabricksService.from_dict(resource_remote_info_databricks_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


