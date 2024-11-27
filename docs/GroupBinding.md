# GroupBinding

# Group Binding Object ### Description The `GroupBinding` object is used to represent a group binding.  ### Usage Example Get group bindings from the `GET Group Bindings` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_binding_id** | **str** | The ID of the group binding. | 
**created_by_id** | **str** | The ID of the user that created the group binding. | 
**created_at** | **datetime** | The date the group binding was created. | 
**source_group_id** | **str** | The ID of the source group. | 
**groups** | [**List[GroupBindingGroup]**](GroupBindingGroup.md) | The list of groups. | 

## Example

```python
from opal_security.models.group_binding import GroupBinding

# TODO update the JSON string below
json = "{}"
# create an instance of GroupBinding from a JSON string
group_binding_instance = GroupBinding.from_json(json)
# print the JSON string representation of the object
print(GroupBinding.to_json())

# convert the object into a dict
group_binding_dict = group_binding_instance.to_dict()
# create an instance of GroupBinding from a dict
group_binding_from_dict = GroupBinding.from_dict(group_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


