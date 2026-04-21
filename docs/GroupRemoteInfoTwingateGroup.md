# GroupRemoteInfoTwingateGroup

Remote info for Twingate group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Twingate group. | 

## Example

```python
from opal_security.models.group_remote_info_twingate_group import GroupRemoteInfoTwingateGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoTwingateGroup from a JSON string
group_remote_info_twingate_group_instance = GroupRemoteInfoTwingateGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoTwingateGroup.to_json())

# convert the object into a dict
group_remote_info_twingate_group_dict = group_remote_info_twingate_group_instance.to_dict()
# create an instance of GroupRemoteInfoTwingateGroup from a dict
group_remote_info_twingate_group_from_dict = GroupRemoteInfoTwingateGroup.from_dict(group_remote_info_twingate_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


