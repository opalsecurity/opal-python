# GroupAccessLevelList

A list of access levels defined for a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GroupAccessLevel]**](GroupAccessLevel.md) |  | [optional] 

## Example

```python
from opal_security.models.group_access_level_list import GroupAccessLevelList

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAccessLevelList from a JSON string
group_access_level_list_instance = GroupAccessLevelList.from_json(json)
# print the JSON string representation of the object
print(GroupAccessLevelList.to_json())

# convert the object into a dict
group_access_level_list_dict = group_access_level_list_instance.to_dict()
# create an instance of GroupAccessLevelList from a dict
group_access_level_list_from_dict = GroupAccessLevelList.from_dict(group_access_level_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


