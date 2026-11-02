# GroupMemberGroup

# GroupMemberGroup Object ### Description The `GroupMemberGroup` object is used to represent a group that is nested directly in another group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_group_id** | **UUID** | The ID of the member group. | 

## Example

```python
from opal_security.models.group_member_group import GroupMemberGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberGroup from a JSON string
group_member_group_instance = GroupMemberGroup.from_json(json)
# print the JSON string representation of the object
print(GroupMemberGroup.to_json())

# convert the object into a dict
group_member_group_dict = group_member_group_instance.to_dict()
# create an instance of GroupMemberGroup from a dict
group_member_group_from_dict = GroupMemberGroup.from_dict(group_member_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


