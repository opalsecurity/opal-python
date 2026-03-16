# BundleResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_id** | **str** | The ID of the bundle containing the resource. | [optional] [readonly] 
**resource_id** | **str** | The ID of the resource within a bundle. | [optional] [readonly] 
**access_level_name** | **str** | The access level of the resource within a bundle. | [optional] 
**access_level_remote_id** | **str** | The remote ID of the access level of the resource within a bundle. | [optional] 

## Example

```python
from opal_security.models.bundle_resource import BundleResource

# TODO update the JSON string below
json = "{}"
# create an instance of BundleResource from a JSON string
bundle_resource_instance = BundleResource.from_json(json)
# print the JSON string representation of the object
print(BundleResource.to_json())

# convert the object into a dict
bundle_resource_dict = bundle_resource_instance.to_dict()
# create an instance of BundleResource from a dict
bundle_resource_from_dict = BundleResource.from_dict(bundle_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


