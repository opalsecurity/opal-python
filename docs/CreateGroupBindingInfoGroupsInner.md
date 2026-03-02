# CreateGroupBindingInfoGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the group. | 

## Example

```python
from opal_security.models.create_group_binding_info_groups_inner import CreateGroupBindingInfoGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupBindingInfoGroupsInner from a JSON string
create_group_binding_info_groups_inner_instance = CreateGroupBindingInfoGroupsInner.from_json(json)
# print the JSON string representation of the object
print(CreateGroupBindingInfoGroupsInner.to_json())

# convert the object into a dict
create_group_binding_info_groups_inner_dict = create_group_binding_info_groups_inner_instance.to_dict()
# create an instance of CreateGroupBindingInfoGroupsInner from a dict
create_group_binding_info_groups_inner_from_dict = CreateGroupBindingInfoGroupsInner.from_dict(create_group_binding_info_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


