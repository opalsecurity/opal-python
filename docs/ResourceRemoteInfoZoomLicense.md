# ResourceRemoteInfoZoomLicense

Remote info for Zoom license (user type).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_type** | **str** | The Zoom user type representing the license (e.g. \&quot;2\&quot; for Licensed). | 

## Example

```python
from opal_security.models.resource_remote_info_zoom_license import ResourceRemoteInfoZoomLicense

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoZoomLicense from a JSON string
resource_remote_info_zoom_license_instance = ResourceRemoteInfoZoomLicense.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoZoomLicense.to_json())

# convert the object into a dict
resource_remote_info_zoom_license_dict = resource_remote_info_zoom_license_instance.to_dict()
# create an instance of ResourceRemoteInfoZoomLicense from a dict
resource_remote_info_zoom_license_from_dict = ResourceRemoteInfoZoomLicense.from_dict(resource_remote_info_zoom_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


