# BundleGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_id** | **str** | The ID of the bundle containing the group. | [optional] [readonly] 
**group_id** | **str** | The ID of the group within a bundle. | [optional] [readonly] 

## Example

```python
from opal_security.models.bundle_group import BundleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of BundleGroup from a JSON string
bundle_group_instance = BundleGroup.from_json(json)
# print the JSON string representation of the object
print(BundleGroup.to_json())

# convert the object into a dict
bundle_group_dict = bundle_group_instance.to_dict()
# create an instance of BundleGroup from a dict
bundle_group_from_dict = BundleGroup.from_dict(bundle_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


