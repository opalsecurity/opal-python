# UpdateGroupBindingInfoList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_bindings** | [**List[UpdateGroupBindingInfo]**](UpdateGroupBindingInfo.md) | A list of group bindings with information to update. | 

## Example

```python
from opal_security.models.update_group_binding_info_list import UpdateGroupBindingInfoList

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupBindingInfoList from a JSON string
update_group_binding_info_list_instance = UpdateGroupBindingInfoList.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupBindingInfoList.to_json())

# convert the object into a dict
update_group_binding_info_list_dict = update_group_binding_info_list_instance.to_dict()
# create an instance of UpdateGroupBindingInfoList from a dict
update_group_binding_info_list_from_dict = UpdateGroupBindingInfoList.from_dict(update_group_binding_info_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


