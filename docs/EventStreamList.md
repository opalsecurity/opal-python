# EventStreamList

A list of event streams.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_streams** | [**List[EventStream]**](EventStream.md) |  | 

## Example

```python
from opal_security.models.event_stream_list import EventStreamList

# TODO update the JSON string below
json = "{}"
# create an instance of EventStreamList from a JSON string
event_stream_list_instance = EventStreamList.from_json(json)
# print the JSON string representation of the object
print(EventStreamList.to_json())

# convert the object into a dict
event_stream_list_dict = event_stream_list_instance.to_dict()
# create an instance of EventStreamList from a dict
event_stream_list_from_dict = EventStreamList.from_dict(event_stream_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


