# ResourceRemoteInfoZendeskRole

Remote info for Zendesk custom role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The ID of the Zendesk custom role. | 

## Example

```python
from opal_security.models.resource_remote_info_zendesk_role import ResourceRemoteInfoZendeskRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoZendeskRole from a JSON string
resource_remote_info_zendesk_role_instance = ResourceRemoteInfoZendeskRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoZendeskRole.to_json())

# convert the object into a dict
resource_remote_info_zendesk_role_dict = resource_remote_info_zendesk_role_instance.to_dict()
# create an instance of ResourceRemoteInfoZendeskRole from a dict
resource_remote_info_zendesk_role_from_dict = ResourceRemoteInfoZendeskRole.from_dict(resource_remote_info_zendesk_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


