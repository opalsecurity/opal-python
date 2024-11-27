# UpdateResourceInfoList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[UpdateResourceInfo]**](UpdateResourceInfo.md) | A list of resources with information to update. | 

## Example

```python
from opal_security.models.update_resource_info_list import UpdateResourceInfoList

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResourceInfoList from a JSON string
update_resource_info_list_instance = UpdateResourceInfoList.from_json(json)
# print the JSON string representation of the object
print(UpdateResourceInfoList.to_json())

# convert the object into a dict
update_resource_info_list_dict = update_resource_info_list_instance.to_dict()
# create an instance of UpdateResourceInfoList from a dict
update_resource_info_list_from_dict = UpdateResourceInfoList.from_dict(update_resource_info_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


