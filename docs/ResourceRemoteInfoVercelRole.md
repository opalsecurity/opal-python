# ResourceRemoteInfoVercelRole

Remote info for Vercel team role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The Vercel team role identifier (e.g. OWNER, MEMBER, CONTRIBUTOR). | 

## Example

```python
from opal_security.models.resource_remote_info_vercel_role import ResourceRemoteInfoVercelRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoVercelRole from a JSON string
resource_remote_info_vercel_role_instance = ResourceRemoteInfoVercelRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoVercelRole.to_json())

# convert the object into a dict
resource_remote_info_vercel_role_dict = resource_remote_info_vercel_role_instance.to_dict()
# create an instance of ResourceRemoteInfoVercelRole from a dict
resource_remote_info_vercel_role_from_dict = ResourceRemoteInfoVercelRole.from_dict(resource_remote_info_vercel_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


