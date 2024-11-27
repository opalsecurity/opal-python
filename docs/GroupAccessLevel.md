# GroupAccessLevel

# Access Level Object ### Description The `GroupAccessLevel` object is used to represent the level of access that a user has to a group or a group has to a group. The \"default\" access level is a `GroupAccessLevel` object whose fields are all empty strings.  ### Usage Example View the `GroupAccessLevel` of a group/user or group/group pair to see the level of access granted to the group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level_name** | **str** | The human-readable name of the access level. | 
**access_level_remote_id** | **str** | The machine-readable identifier of the access level. | 

## Example

```python
from opal_security.models.group_access_level import GroupAccessLevel

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAccessLevel from a JSON string
group_access_level_instance = GroupAccessLevel.from_json(json)
# print the JSON string representation of the object
print(GroupAccessLevel.to_json())

# convert the object into a dict
group_access_level_dict = group_access_level_instance.to_dict()
# create an instance of GroupAccessLevel from a dict
group_access_level_from_dict = GroupAccessLevel.from_dict(group_access_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


