# ResourceRemoteInfoRampRole

Remote info for Ramp built-in role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The Ramp built-in role enum (e.g. BUSINESS_USER). | 

## Example

```python
from opal_security.models.resource_remote_info_ramp_role import ResourceRemoteInfoRampRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoRampRole from a JSON string
resource_remote_info_ramp_role_instance = ResourceRemoteInfoRampRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoRampRole.to_json())

# convert the object into a dict
resource_remote_info_ramp_role_dict = resource_remote_info_ramp_role_instance.to_dict()
# create an instance of ResourceRemoteInfoRampRole from a dict
resource_remote_info_ramp_role_from_dict = ResourceRemoteInfoRampRole.from_dict(resource_remote_info_ramp_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


