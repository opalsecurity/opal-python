# ResourceRemoteInfoDatabricksVolume

Remote info for Databricks Unity Catalog volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metastore_id** | **str** | The ID of the Unity Catalog metastore the volume belongs to. | 
**full_name** | **str** | The dot-qualified full name of the volume (e.g. \&quot;catalog.schema.volume\&quot;). | 

## Example

```python
from opal_security.models.resource_remote_info_databricks_volume import ResourceRemoteInfoDatabricksVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoDatabricksVolume from a JSON string
resource_remote_info_databricks_volume_instance = ResourceRemoteInfoDatabricksVolume.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoDatabricksVolume.to_json())

# convert the object into a dict
resource_remote_info_databricks_volume_dict = resource_remote_info_databricks_volume_instance.to_dict()
# create an instance of ResourceRemoteInfoDatabricksVolume from a dict
resource_remote_info_databricks_volume_from_dict = ResourceRemoteInfoDatabricksVolume.from_dict(resource_remote_info_databricks_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


