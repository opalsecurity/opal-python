# GroupRemoteInfoZoomGroup

Remote info for Zoom group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the Zoom group. | 

## Example

```python
from opal_security.models.group_remote_info_zoom_group import GroupRemoteInfoZoomGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoZoomGroup from a JSON string
group_remote_info_zoom_group_instance = GroupRemoteInfoZoomGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoZoomGroup.to_json())

# convert the object into a dict
group_remote_info_zoom_group_dict = group_remote_info_zoom_group_instance.to_dict()
# create an instance of GroupRemoteInfoZoomGroup from a dict
group_remote_info_zoom_group_from_dict = GroupRemoteInfoZoomGroup.from_dict(group_remote_info_zoom_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


