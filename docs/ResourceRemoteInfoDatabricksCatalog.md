# ResourceRemoteInfoDatabricksCatalog

Remote info for Databricks Unity Catalog catalog.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metastore_id** | **str** | The ID of the Unity Catalog metastore the catalog belongs to. | 
**full_name** | **str** | The dot-qualified full name of the catalog (e.g. \&quot;catalog\&quot;). | 

## Example

```python
from opal_security.models.resource_remote_info_databricks_catalog import ResourceRemoteInfoDatabricksCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoDatabricksCatalog from a JSON string
resource_remote_info_databricks_catalog_instance = ResourceRemoteInfoDatabricksCatalog.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoDatabricksCatalog.to_json())

# convert the object into a dict
resource_remote_info_databricks_catalog_dict = resource_remote_info_databricks_catalog_instance.to_dict()
# create an instance of ResourceRemoteInfoDatabricksCatalog from a dict
resource_remote_info_databricks_catalog_from_dict = ResourceRemoteInfoDatabricksCatalog.from_dict(resource_remote_info_databricks_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


