# ResourceRemoteInfoCoupaRole

Remote info for Coupa role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The id of the role. | 

## Example

```python
from opal_security.models.resource_remote_info_coupa_role import ResourceRemoteInfoCoupaRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoCoupaRole from a JSON string
resource_remote_info_coupa_role_instance = ResourceRemoteInfoCoupaRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoCoupaRole.to_json())

# convert the object into a dict
resource_remote_info_coupa_role_dict = resource_remote_info_coupa_role_instance.to_dict()
# create an instance of ResourceRemoteInfoCoupaRole from a dict
resource_remote_info_coupa_role_from_dict = ResourceRemoteInfoCoupaRole.from_dict(resource_remote_info_coupa_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


