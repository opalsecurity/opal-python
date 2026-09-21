# GroupRemoteInfoWrikeGroup

Remote info for Wrike group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the Wrike group. | 

## Example

```python
from opal_security.models.group_remote_info_wrike_group import GroupRemoteInfoWrikeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoWrikeGroup from a JSON string
group_remote_info_wrike_group_instance = GroupRemoteInfoWrikeGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoWrikeGroup.to_json())

# convert the object into a dict
group_remote_info_wrike_group_dict = group_remote_info_wrike_group_instance.to_dict()
# create an instance of GroupRemoteInfoWrikeGroup from a dict
group_remote_info_wrike_group_from_dict = GroupRemoteInfoWrikeGroup.from_dict(group_remote_info_wrike_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


