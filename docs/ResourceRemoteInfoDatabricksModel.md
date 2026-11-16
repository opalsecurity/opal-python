# ResourceRemoteInfoDatabricksModel

Remote info for Databricks Unity Catalog registered model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metastore_id** | **str** | The ID of the Unity Catalog metastore the model belongs to. | 
**full_name** | **str** | The dot-qualified full name of the model (e.g. \&quot;catalog.schema.model\&quot;). | 

## Example

```python
from opal_security.models.resource_remote_info_databricks_model import ResourceRemoteInfoDatabricksModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoDatabricksModel from a JSON string
resource_remote_info_databricks_model_instance = ResourceRemoteInfoDatabricksModel.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoDatabricksModel.to_json())

# convert the object into a dict
resource_remote_info_databricks_model_dict = resource_remote_info_databricks_model_instance.to_dict()
# create an instance of ResourceRemoteInfoDatabricksModel from a dict
resource_remote_info_databricks_model_from_dict = ResourceRemoteInfoDatabricksModel.from_dict(resource_remote_info_databricks_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


