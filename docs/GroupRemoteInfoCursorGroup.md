# GroupRemoteInfoCursorGroup

Remote info for a Cursor group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Cursor group, or team:members / team:admins for the owning team&#39;s built-in groups. | 

## Example

```python
from opal_security.models.group_remote_info_cursor_group import GroupRemoteInfoCursorGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoCursorGroup from a JSON string
group_remote_info_cursor_group_instance = GroupRemoteInfoCursorGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoCursorGroup.to_json())

# convert the object into a dict
group_remote_info_cursor_group_dict = group_remote_info_cursor_group_instance.to_dict()
# create an instance of GroupRemoteInfoCursorGroup from a dict
group_remote_info_cursor_group_from_dict = GroupRemoteInfoCursorGroup.from_dict(group_remote_info_cursor_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


