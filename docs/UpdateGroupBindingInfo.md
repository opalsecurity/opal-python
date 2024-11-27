# UpdateGroupBindingInfo

# UpdateGroupBindingInfo Object ### Description The `UpdateGroupBindingInfo` object is used as an input to the UpdateGroupBinding API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_binding_id** | **str** | The ID of the group binding. | 
**source_group_id** | **str** | The ID of the source group. | 
**groups** | [**List[CreateGroupBindingInfoGroupsInner]**](CreateGroupBindingInfoGroupsInner.md) | The list of groups. | 

## Example

```python
from opal_security.models.update_group_binding_info import UpdateGroupBindingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupBindingInfo from a JSON string
update_group_binding_info_instance = UpdateGroupBindingInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupBindingInfo.to_json())

# convert the object into a dict
update_group_binding_info_dict = update_group_binding_info_instance.to_dict()
# create an instance of UpdateGroupBindingInfo from a dict
update_group_binding_info_from_dict = UpdateGroupBindingInfo.from_dict(update_group_binding_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


