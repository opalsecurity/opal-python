# GroupRemoteInfoTableauGroup

Remote info for Tableau group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the Tableau group. | 

## Example

```python
from opal_security.models.group_remote_info_tableau_group import GroupRemoteInfoTableauGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoTableauGroup from a JSON string
group_remote_info_tableau_group_instance = GroupRemoteInfoTableauGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoTableauGroup.to_json())

# convert the object into a dict
group_remote_info_tableau_group_dict = group_remote_info_tableau_group_instance.to_dict()
# create an instance of GroupRemoteInfoTableauGroup from a dict
group_remote_info_tableau_group_from_dict = GroupRemoteInfoTableauGroup.from_dict(group_remote_info_tableau_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


