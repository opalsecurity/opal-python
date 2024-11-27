# ResourceRemoteInfoOktaApp

Remote info for Okta directory app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The id of the app. | 

## Example

```python
from opal_security.models.resource_remote_info_okta_app import ResourceRemoteInfoOktaApp

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoOktaApp from a JSON string
resource_remote_info_okta_app_instance = ResourceRemoteInfoOktaApp.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoOktaApp.to_json())

# convert the object into a dict
resource_remote_info_okta_app_dict = resource_remote_info_okta_app_instance.to_dict()
# create an instance of ResourceRemoteInfoOktaApp from a dict
resource_remote_info_okta_app_from_dict = ResourceRemoteInfoOktaApp.from_dict(resource_remote_info_okta_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


