# GroupUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GroupUser]**](GroupUser.md) |  | [optional] 

## Example

```python
from opal_security.models.group_user_list import GroupUserList

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUserList from a JSON string
group_user_list_instance = GroupUserList.from_json(json)
# print the JSON string representation of the object
print(GroupUserList.to_json())

# convert the object into a dict
group_user_list_dict = group_user_list_instance.to_dict()
# create an instance of GroupUserList from a dict
group_user_list_from_dict = GroupUserList.from_dict(group_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


