# GroupBindingGroup

# Group Binding Group Object ### Description The `GroupBindingGroup` object is used to represent a group binding group.  ### Usage Example Get group binding groups from the `GET Group Bindings` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the group. | 
**group_type** | [**GroupTypeEnum**](GroupTypeEnum.md) |  | 

## Example

```python
from opal_security.models.group_binding_group import GroupBindingGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupBindingGroup from a JSON string
group_binding_group_instance = GroupBindingGroup.from_json(json)
# print the JSON string representation of the object
print(GroupBindingGroup.to_json())

# convert the object into a dict
group_binding_group_dict = group_binding_group_instance.to_dict()
# create an instance of GroupBindingGroup from a dict
group_binding_group_from_dict = GroupBindingGroup.from_dict(group_binding_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


