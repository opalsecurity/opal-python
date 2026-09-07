# CreateResourceCustomAccessLevelInfo

Info for creating a custom access level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | 
**policy** | **str** | The policy document. | [optional] 
**requestable_by_default** | **bool** | Whether the role is requestable. Defaults to false. | [optional] 
**stackable_sensitivity_index** | **int** | The sensitivity index. Null to leave unranked. | [optional] 

## Example

```python
from opal_security.models.create_resource_custom_access_level_info import CreateResourceCustomAccessLevelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourceCustomAccessLevelInfo from a JSON string
create_resource_custom_access_level_info_instance = CreateResourceCustomAccessLevelInfo.from_json(json)
# print the JSON string representation of the object
print(CreateResourceCustomAccessLevelInfo.to_json())

# convert the object into a dict
create_resource_custom_access_level_info_dict = create_resource_custom_access_level_info_instance.to_dict()
# create an instance of CreateResourceCustomAccessLevelInfo from a dict
create_resource_custom_access_level_info_from_dict = CreateResourceCustomAccessLevelInfo.from_dict(create_resource_custom_access_level_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


