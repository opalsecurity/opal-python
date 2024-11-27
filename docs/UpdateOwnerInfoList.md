# UpdateOwnerInfoList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**List[UpdateOwnerInfo]**](UpdateOwnerInfo.md) | A list of owners with information to update. | 

## Example

```python
from opal_security.models.update_owner_info_list import UpdateOwnerInfoList

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOwnerInfoList from a JSON string
update_owner_info_list_instance = UpdateOwnerInfoList.from_json(json)
# print the JSON string representation of the object
print(UpdateOwnerInfoList.to_json())

# convert the object into a dict
update_owner_info_list_dict = update_owner_info_list_instance.to_dict()
# create an instance of UpdateOwnerInfoList from a dict
update_owner_info_list_from_dict = UpdateOwnerInfoList.from_dict(update_owner_info_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


