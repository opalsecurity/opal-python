# ResourceAccessLevelList

A list of access levels defined for a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ResourceAccessLevel]**](ResourceAccessLevel.md) |  | [optional] 

## Example

```python
from opal_security.models.resource_access_level_list import ResourceAccessLevelList

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAccessLevelList from a JSON string
resource_access_level_list_instance = ResourceAccessLevelList.from_json(json)
# print the JSON string representation of the object
print(ResourceAccessLevelList.to_json())

# convert the object into a dict
resource_access_level_list_dict = resource_access_level_list_instance.to_dict()
# create an instance of ResourceAccessLevelList from a dict
resource_access_level_list_from_dict = ResourceAccessLevelList.from_dict(resource_access_level_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


