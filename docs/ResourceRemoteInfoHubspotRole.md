# ResourceRemoteInfoHubspotRole

Remote info for HubSpot role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The ID of the HubSpot role. | 

## Example

```python
from opal_security.models.resource_remote_info_hubspot_role import ResourceRemoteInfoHubspotRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoHubspotRole from a JSON string
resource_remote_info_hubspot_role_instance = ResourceRemoteInfoHubspotRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoHubspotRole.to_json())

# convert the object into a dict
resource_remote_info_hubspot_role_dict = resource_remote_info_hubspot_role_instance.to_dict()
# create an instance of ResourceRemoteInfoHubspotRole from a dict
resource_remote_info_hubspot_role_from_dict = ResourceRemoteInfoHubspotRole.from_dict(resource_remote_info_hubspot_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


