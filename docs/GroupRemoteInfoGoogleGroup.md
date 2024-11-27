# GroupRemoteInfoGoogleGroup

Remote info for Google group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Google group. | 

## Example

```python
from opal_security.models.group_remote_info_google_group import GroupRemoteInfoGoogleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoGoogleGroup from a JSON string
group_remote_info_google_group_instance = GroupRemoteInfoGoogleGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoGoogleGroup.to_json())

# convert the object into a dict
group_remote_info_google_group_dict = group_remote_info_google_group_instance.to_dict()
# create an instance of GroupRemoteInfoGoogleGroup from a dict
group_remote_info_google_group_from_dict = GroupRemoteInfoGoogleGroup.from_dict(group_remote_info_google_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


