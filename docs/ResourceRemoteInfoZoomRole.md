# ResourceRemoteInfoZoomRole

Remote info for Zoom role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The ID of the Zoom role. | 

## Example

```python
from opal_security.models.resource_remote_info_zoom_role import ResourceRemoteInfoZoomRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoZoomRole from a JSON string
resource_remote_info_zoom_role_instance = ResourceRemoteInfoZoomRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoZoomRole.to_json())

# convert the object into a dict
resource_remote_info_zoom_role_dict = resource_remote_info_zoom_role_instance.to_dict()
# create an instance of ResourceRemoteInfoZoomRole from a dict
resource_remote_info_zoom_role_from_dict = ResourceRemoteInfoZoomRole.from_dict(resource_remote_info_zoom_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


