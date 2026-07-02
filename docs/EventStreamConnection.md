# EventStreamConnection

The connection configuration for an event stream.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the connection. | 
**connection_type** | [**EventStreamConnectionTypeEnum**](EventStreamConnectionTypeEnum.md) |  | 
**enabled** | **bool** | Whether the connection is enabled. | 
**webhook_url** | **str** | The webhook URL, present when connection_type is WEBHOOK. | [optional] 
**credentials** | [**WebhookCredentials**](WebhookCredentials.md) |  | [optional] 

## Example

```python
from opal_security.models.event_stream_connection import EventStreamConnection

# TODO update the JSON string below
json = "{}"
# create an instance of EventStreamConnection from a JSON string
event_stream_connection_instance = EventStreamConnection.from_json(json)
# print the JSON string representation of the object
print(EventStreamConnection.to_json())

# convert the object into a dict
event_stream_connection_dict = event_stream_connection_instance.to_dict()
# create an instance of EventStreamConnection from a dict
event_stream_connection_from_dict = EventStreamConnection.from_dict(event_stream_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


