# CreateGroupBindingInfo

# CreateGroupBindingInfo Object ### Description The `CreateGroupBindingInfo` object is used as an input to the CreateGroupBinding API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_group_id** | **str** | The ID of the source group. | 
**groups** | [**List[CreateGroupBindingInfoGroupsInner]**](CreateGroupBindingInfoGroupsInner.md) | The list of groups. | 

## Example

```python
from opal_security.models.create_group_binding_info import CreateGroupBindingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupBindingInfo from a JSON string
create_group_binding_info_instance = CreateGroupBindingInfo.from_json(json)
# print the JSON string representation of the object
print(CreateGroupBindingInfo.to_json())

# convert the object into a dict
create_group_binding_info_dict = create_group_binding_info_instance.to_dict()
# create an instance of CreateGroupBindingInfo from a dict
create_group_binding_info_from_dict = CreateGroupBindingInfo.from_dict(create_group_binding_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


