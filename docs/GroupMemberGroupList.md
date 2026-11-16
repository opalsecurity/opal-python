# GroupMemberGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_groups** | [**List[GroupMemberGroup]**](GroupMemberGroup.md) |  | 

## Example

```python
from opal_security.models.group_member_group_list import GroupMemberGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberGroupList from a JSON string
group_member_group_list_instance = GroupMemberGroupList.from_json(json)
# print the JSON string representation of the object
print(GroupMemberGroupList.to_json())

# convert the object into a dict
group_member_group_list_dict = group_member_group_list_instance.to_dict()
# create an instance of GroupMemberGroupList from a dict
group_member_group_list_from_dict = GroupMemberGroupList.from_dict(group_member_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


