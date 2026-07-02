# CreateEventStreamInfo

Information needed to create an event stream.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the event stream. | 
**connection_type** | [**EventStreamConnectionTypeEnum**](EventStreamConnectionTypeEnum.md) |  | 
**webhook_url** | **str** | The webhook URL. Required when connection_type is WEBHOOK. | [optional] 
**credentials** | [**WebhookCredentials**](WebhookCredentials.md) |  | [optional] 

## Example

```python
from opal_security.models.create_event_stream_info import CreateEventStreamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventStreamInfo from a JSON string
create_event_stream_info_instance = CreateEventStreamInfo.from_json(json)
# print the JSON string representation of the object
print(CreateEventStreamInfo.to_json())

# convert the object into a dict
create_event_stream_info_dict = create_event_stream_info_instance.to_dict()
# create an instance of CreateEventStreamInfo from a dict
create_event_stream_info_from_dict = CreateEventStreamInfo.from_dict(create_event_stream_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


