# Bundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_id** | **str** | The ID of the bundle. | [optional] [readonly] 
**name** | **str** | The name of the bundle. | [optional] 
**description** | **str** | The description of the bundle. | [optional] 
**created_at** | **datetime** | The creation timestamp of the bundle, in ISO 8601 format | [optional] [readonly] 
**updated_at** | **datetime** | The last updated timestamp of the bundle, in ISO 8601 format | [optional] [readonly] 
**admin_owner_id** | **str** | The ID of the owner of the bundle. | [optional] 
**total_num_items** | **int** | The total number of items in the bundle. | [optional] [readonly] 
**total_num_resources** | **int** | The total number of resources in the bundle. | [optional] [readonly] 
**total_num_groups** | **int** | The total number of groups in the bundle. | [optional] [readonly] 

## Example

```python
from opal_security.models.bundle import Bundle

# TODO update the JSON string below
json = "{}"
# create an instance of Bundle from a JSON string
bundle_instance = Bundle.from_json(json)
# print the JSON string representation of the object
print(Bundle.to_json())

# convert the object into a dict
bundle_dict = bundle_instance.to_dict()
# create an instance of Bundle from a dict
bundle_from_dict = Bundle.from_dict(bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


