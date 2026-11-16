# GroupRemoteInfoOneloginRole

Remote info for OneLogin Role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The group id of the OneLogin Role. | 

## Example

```python
from opal_security.models.group_remote_info_onelogin_role import GroupRemoteInfoOneloginRole

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoOneloginRole from a JSON string
group_remote_info_onelogin_role_instance = GroupRemoteInfoOneloginRole.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoOneloginRole.to_json())

# convert the object into a dict
group_remote_info_onelogin_role_dict = group_remote_info_onelogin_role_instance.to_dict()
# create an instance of GroupRemoteInfoOneloginRole from a dict
group_remote_info_onelogin_role_from_dict = GroupRemoteInfoOneloginRole.from_dict(group_remote_info_onelogin_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


