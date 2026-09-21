# ResourceRemoteInfoDatabricksSchema

Remote info for Databricks Unity Catalog schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metastore_id** | **str** | The ID of the Unity Catalog metastore the schema belongs to. | 
**full_name** | **str** | The dot-qualified full name of the schema (e.g. \&quot;catalog.schema\&quot;). | 

## Example

```python
from opal_security.models.resource_remote_info_databricks_schema import ResourceRemoteInfoDatabricksSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoDatabricksSchema from a JSON string
resource_remote_info_databricks_schema_instance = ResourceRemoteInfoDatabricksSchema.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoDatabricksSchema.to_json())

# convert the object into a dict
resource_remote_info_databricks_schema_dict = resource_remote_info_databricks_schema_instance.to_dict()
# create an instance of ResourceRemoteInfoDatabricksSchema from a dict
resource_remote_info_databricks_schema_from_dict = ResourceRemoteInfoDatabricksSchema.from_dict(resource_remote_info_databricks_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


