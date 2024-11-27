# GroupRemoteInfoDuoGroup

Remote info for Duo Security group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Duo Security group. | 

## Example

```python
from opal_security.models.group_remote_info_duo_group import GroupRemoteInfoDuoGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoDuoGroup from a JSON string
group_remote_info_duo_group_instance = GroupRemoteInfoDuoGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoDuoGroup.to_json())

# convert the object into a dict
group_remote_info_duo_group_dict = group_remote_info_duo_group_instance.to_dict()
# create an instance of GroupRemoteInfoDuoGroup from a dict
group_remote_info_duo_group_from_dict = GroupRemoteInfoDuoGroup.from_dict(group_remote_info_duo_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


