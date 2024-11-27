# ResourceRemoteInfoOktaStandardRole

Remote info for Okta directory standard role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_type** | **str** | The type of the standard role. | 

## Example

```python
from opal_security.models.resource_remote_info_okta_standard_role import ResourceRemoteInfoOktaStandardRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoOktaStandardRole from a JSON string
resource_remote_info_okta_standard_role_instance = ResourceRemoteInfoOktaStandardRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoOktaStandardRole.to_json())

# convert the object into a dict
resource_remote_info_okta_standard_role_dict = resource_remote_info_okta_standard_role_instance.to_dict()
# create an instance of ResourceRemoteInfoOktaStandardRole from a dict
resource_remote_info_okta_standard_role_from_dict = ResourceRemoteInfoOktaStandardRole.from_dict(resource_remote_info_okta_standard_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


