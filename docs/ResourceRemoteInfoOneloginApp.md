# ResourceRemoteInfoOneloginApp

Remote info for OneLogin App.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The resource id of the OneLogin App. | 

## Example

```python
from opal_security.models.resource_remote_info_onelogin_app import ResourceRemoteInfoOneloginApp

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoOneloginApp from a JSON string
resource_remote_info_onelogin_app_instance = ResourceRemoteInfoOneloginApp.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoOneloginApp.to_json())

# convert the object into a dict
resource_remote_info_onelogin_app_dict = resource_remote_info_onelogin_app_instance.to_dict()
# create an instance of ResourceRemoteInfoOneloginApp from a dict
resource_remote_info_onelogin_app_from_dict = ResourceRemoteInfoOneloginApp.from_dict(resource_remote_info_onelogin_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


