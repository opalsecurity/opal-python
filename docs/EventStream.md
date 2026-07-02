# EventStream

An event streaming connection that publishes events to an external system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_stream_id** | **UUID** | The ID of the event stream. | 
**connection** | [**EventStreamConnection**](EventStreamConnection.md) |  | 

## Example

```python
from opal_security.models.event_stream import EventStream

# TODO update the JSON string below
json = "{}"
# create an instance of EventStream from a JSON string
event_stream_instance = EventStream.from_json(json)
# print the JSON string representation of the object
print(EventStream.to_json())

# convert the object into a dict
event_stream_dict = event_stream_instance.to_dict()
# create an instance of EventStream from a dict
event_stream_from_dict = EventStream.from_dict(event_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


