# GroupContainingGroup

# GroupContainingGroup Object ### Description The `GroupContainingGroup` object is used to represent a relationship between a group and a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containing_group_id** | **UUID** | The groupID of the containing group. | 
**duration_minutes** | **int** | The updated duration for which the group can be accessed (in minutes). Use 0 for indefinite. | [optional] 
**access_level_remote_id** | **str** | The updated remote ID of the access level granted to this group. | [optional] 

## Example

```python
from opal_security.models.group_containing_group import GroupContainingGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupContainingGroup from a JSON string
group_containing_group_instance = GroupContainingGroup.from_json(json)
# print the JSON string representation of the object
print(GroupContainingGroup.to_json())

# convert the object into a dict
group_containing_group_dict = group_containing_group_instance.to_dict()
# create an instance of GroupContainingGroup from a dict
group_containing_group_from_dict = GroupContainingGroup.from_dict(group_containing_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


