# ResourceCustomAccessLevelList

A list of custom access levels.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_access_levels** | [**List[ResourceCustomAccessLevelResponse]**](ResourceCustomAccessLevelResponse.md) |  | 

## Example

```python
from opal_security.models.resource_custom_access_level_list import ResourceCustomAccessLevelList

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCustomAccessLevelList from a JSON string
resource_custom_access_level_list_instance = ResourceCustomAccessLevelList.from_json(json)
# print the JSON string representation of the object
print(ResourceCustomAccessLevelList.to_json())

# convert the object into a dict
resource_custom_access_level_list_dict = resource_custom_access_level_list_instance.to_dict()
# create an instance of ResourceCustomAccessLevelList from a dict
resource_custom_access_level_list_from_dict = ResourceCustomAccessLevelList.from_dict(resource_custom_access_level_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


