# GroupRemoteInfoOneloginGroup

Remote info for OneLogin Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The group id of the OneLogin Group. | 

## Example

```python
from opal_security.models.group_remote_info_onelogin_group import GroupRemoteInfoOneloginGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoOneloginGroup from a JSON string
group_remote_info_onelogin_group_instance = GroupRemoteInfoOneloginGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoOneloginGroup.to_json())

# convert the object into a dict
group_remote_info_onelogin_group_dict = group_remote_info_onelogin_group_instance.to_dict()
# create an instance of GroupRemoteInfoOneloginGroup from a dict
group_remote_info_onelogin_group_from_dict = GroupRemoteInfoOneloginGroup.from_dict(group_remote_info_onelogin_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


