# UpdateGroupInfoList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[UpdateGroupInfo]**](UpdateGroupInfo.md) | A list of groups with information to update. | 

## Example

```python
from opal_security.models.update_group_info_list import UpdateGroupInfoList

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupInfoList from a JSON string
update_group_info_list_instance = UpdateGroupInfoList.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupInfoList.to_json())

# convert the object into a dict
update_group_info_list_dict = update_group_info_list_instance.to_dict()
# create an instance of UpdateGroupInfoList from a dict
update_group_info_list_from_dict = UpdateGroupInfoList.from_dict(update_group_info_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


