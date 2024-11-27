# ResourceRemoteInfoOktaCustomRole

Remote info for Okta directory custom role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The id of the custom role. | 

## Example

```python
from opal_security.models.resource_remote_info_okta_custom_role import ResourceRemoteInfoOktaCustomRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoOktaCustomRole from a JSON string
resource_remote_info_okta_custom_role_instance = ResourceRemoteInfoOktaCustomRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoOktaCustomRole.to_json())

# convert the object into a dict
resource_remote_info_okta_custom_role_dict = resource_remote_info_okta_custom_role_instance.to_dict()
# create an instance of ResourceRemoteInfoOktaCustomRole from a dict
resource_remote_info_okta_custom_role_from_dict = ResourceRemoteInfoOktaCustomRole.from_dict(resource_remote_info_okta_custom_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


