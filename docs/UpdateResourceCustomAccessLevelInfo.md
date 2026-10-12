# UpdateResourceCustomAccessLevelInfo

Info for updating a custom access level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level_name** | **str** | The new human-readable name. | [optional] 
**policy** | **str** | The new policy document. | [optional] 
**requestable_by_default** | **bool** | Whether the role is requestable. | [optional] 
**stackable_sensitivity_index** | **int** | The new sensitivity index. | [optional] 
**clear_stackable_sensitivity_index** | **bool** | Set to true to remove from the hierarchy. | [optional] 

## Example

```python
from opal_security.models.update_resource_custom_access_level_info import UpdateResourceCustomAccessLevelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResourceCustomAccessLevelInfo from a JSON string
update_resource_custom_access_level_info_instance = UpdateResourceCustomAccessLevelInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateResourceCustomAccessLevelInfo.to_json())

# convert the object into a dict
update_resource_custom_access_level_info_dict = update_resource_custom_access_level_info_instance.to_dict()
# create an instance of UpdateResourceCustomAccessLevelInfo from a dict
update_resource_custom_access_level_info_from_dict = UpdateResourceCustomAccessLevelInfo.from_dict(update_resource_custom_access_level_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


