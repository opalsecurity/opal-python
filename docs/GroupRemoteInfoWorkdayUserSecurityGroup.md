# GroupRemoteInfoWorkdayUserSecurityGroup

Remote info for Workday User Security group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Workday User Security group. | 

## Example

```python
from opal_security.models.group_remote_info_workday_user_security_group import GroupRemoteInfoWorkdayUserSecurityGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoWorkdayUserSecurityGroup from a JSON string
group_remote_info_workday_user_security_group_instance = GroupRemoteInfoWorkdayUserSecurityGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoWorkdayUserSecurityGroup.to_json())

# convert the object into a dict
group_remote_info_workday_user_security_group_dict = group_remote_info_workday_user_security_group_instance.to_dict()
# create an instance of GroupRemoteInfoWorkdayUserSecurityGroup from a dict
group_remote_info_workday_user_security_group_from_dict = GroupRemoteInfoWorkdayUserSecurityGroup.from_dict(group_remote_info_workday_user_security_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


