# ResourceRemoteInfoCalendlyRole

Remote info for Calendly Role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The resource id of the Calendly Role. | 

## Example

```python
from opal_security.models.resource_remote_info_calendly_role import ResourceRemoteInfoCalendlyRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoCalendlyRole from a JSON string
resource_remote_info_calendly_role_instance = ResourceRemoteInfoCalendlyRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoCalendlyRole.to_json())

# convert the object into a dict
resource_remote_info_calendly_role_dict = resource_remote_info_calendly_role_instance.to_dict()
# create an instance of ResourceRemoteInfoCalendlyRole from a dict
resource_remote_info_calendly_role_from_dict = ResourceRemoteInfoCalendlyRole.from_dict(resource_remote_info_calendly_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


