# UpdateGroupResourcesInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[ResourceWithAccessLevel]**](ResourceWithAccessLevel.md) |  | 

## Example

```python
from opal_security.models.update_group_resources_info import UpdateGroupResourcesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupResourcesInfo from a JSON string
update_group_resources_info_instance = UpdateGroupResourcesInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupResourcesInfo.to_json())

# convert the object into a dict
update_group_resources_info_dict = update_group_resources_info_instance.to_dict()
# create an instance of UpdateGroupResourcesInfo from a dict
update_group_resources_info_from_dict = UpdateGroupResourcesInfo.from_dict(update_group_resources_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


