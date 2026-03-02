# GroupWithAccessLevel

Information about a group and corresponding access level

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the group. | 
**access_level_remote_id** | **str** | The ID of the resource. | [optional] 

## Example

```python
from opal_security.models.group_with_access_level import GroupWithAccessLevel

# TODO update the JSON string below
json = "{}"
# create an instance of GroupWithAccessLevel from a JSON string
group_with_access_level_instance = GroupWithAccessLevel.from_json(json)
# print the JSON string representation of the object
print(GroupWithAccessLevel.to_json())

# convert the object into a dict
group_with_access_level_dict = group_with_access_level_instance.to_dict()
# create an instance of GroupWithAccessLevel from a dict
group_with_access_level_from_dict = GroupWithAccessLevel.from_dict(group_with_access_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


