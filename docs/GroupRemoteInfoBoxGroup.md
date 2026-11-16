# GroupRemoteInfoBoxGroup

Remote info for Box Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The group id of the Box Group. | 

## Example

```python
from opal_security.models.group_remote_info_box_group import GroupRemoteInfoBoxGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoBoxGroup from a JSON string
group_remote_info_box_group_instance = GroupRemoteInfoBoxGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoBoxGroup.to_json())

# convert the object into a dict
group_remote_info_box_group_dict = group_remote_info_box_group_instance.to_dict()
# create an instance of GroupRemoteInfoBoxGroup from a dict
group_remote_info_box_group_from_dict = GroupRemoteInfoBoxGroup.from_dict(group_remote_info_box_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


