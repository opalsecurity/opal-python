# ResourceRemoteInfoDatabricksFunction

Remote info for Databricks Unity Catalog function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metastore_id** | **str** | The ID of the Unity Catalog metastore the function belongs to. | 
**full_name** | **str** | The dot-qualified full name of the function (e.g. \&quot;catalog.schema.function\&quot;). | 

## Example

```python
from opal_security.models.resource_remote_info_databricks_function import ResourceRemoteInfoDatabricksFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoDatabricksFunction from a JSON string
resource_remote_info_databricks_function_instance = ResourceRemoteInfoDatabricksFunction.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoDatabricksFunction.to_json())

# convert the object into a dict
resource_remote_info_databricks_function_dict = resource_remote_info_databricks_function_instance.to_dict()
# create an instance of ResourceRemoteInfoDatabricksFunction from a dict
resource_remote_info_databricks_function_from_dict = ResourceRemoteInfoDatabricksFunction.from_dict(resource_remote_info_databricks_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


