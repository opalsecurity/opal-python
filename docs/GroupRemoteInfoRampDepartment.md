# GroupRemoteInfoRampDepartment

Remote info for Ramp department.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**department_id** | **str** | The ID of the Ramp department. | 

## Example

```python
from opal_security.models.group_remote_info_ramp_department import GroupRemoteInfoRampDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoRampDepartment from a JSON string
group_remote_info_ramp_department_instance = GroupRemoteInfoRampDepartment.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoRampDepartment.to_json())

# convert the object into a dict
group_remote_info_ramp_department_dict = group_remote_info_ramp_department_instance.to_dict()
# create an instance of GroupRemoteInfoRampDepartment from a dict
group_remote_info_ramp_department_from_dict = GroupRemoteInfoRampDepartment.from_dict(group_remote_info_ramp_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


