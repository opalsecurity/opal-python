# GroupContainingGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containing_groups** | [**List[GroupContainingGroup]**](GroupContainingGroup.md) |  | 

## Example

```python
from opal_security.models.group_containing_group_list import GroupContainingGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of GroupContainingGroupList from a JSON string
group_containing_group_list_instance = GroupContainingGroupList.from_json(json)
# print the JSON string representation of the object
print(GroupContainingGroupList.to_json())

# convert the object into a dict
group_containing_group_list_dict = group_containing_group_list_instance.to_dict()
# create an instance of GroupContainingGroupList from a dict
group_containing_group_list_from_dict = GroupContainingGroupList.from_dict(group_containing_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


