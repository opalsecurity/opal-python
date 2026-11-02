# ResourceRemoteInfoCalendlyEventType

Remote info for Calendly Event Type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The resource id of the Calendly Event Type. | 

## Example

```python
from opal_security.models.resource_remote_info_calendly_event_type import ResourceRemoteInfoCalendlyEventType

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoCalendlyEventType from a JSON string
resource_remote_info_calendly_event_type_instance = ResourceRemoteInfoCalendlyEventType.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoCalendlyEventType.to_json())

# convert the object into a dict
resource_remote_info_calendly_event_type_dict = resource_remote_info_calendly_event_type_instance.to_dict()
# create an instance of ResourceRemoteInfoCalendlyEventType from a dict
resource_remote_info_calendly_event_type_from_dict = ResourceRemoteInfoCalendlyEventType.from_dict(resource_remote_info_calendly_event_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


