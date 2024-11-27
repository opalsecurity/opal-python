# GroupRemoteInfoActiveDirectoryGroup

Remote info for Active Directory group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Google group. | 

## Example

```python
from opal_security.models.group_remote_info_active_directory_group import GroupRemoteInfoActiveDirectoryGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoActiveDirectoryGroup from a JSON string
group_remote_info_active_directory_group_instance = GroupRemoteInfoActiveDirectoryGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoActiveDirectoryGroup.to_json())

# convert the object into a dict
group_remote_info_active_directory_group_dict = group_remote_info_active_directory_group_instance.to_dict()
# create an instance of GroupRemoteInfoActiveDirectoryGroup from a dict
group_remote_info_active_directory_group_from_dict = GroupRemoteInfoActiveDirectoryGroup.from_dict(group_remote_info_active_directory_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


