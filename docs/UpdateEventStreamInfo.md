# UpdateEventStreamInfo

Information needed to update an event stream.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated name for the event stream. | [optional] 
**enabled** | **bool** | Whether the event stream should be enabled. | [optional] 
**webhook_url** | **str** | Updated webhook URL. | [optional] 
**credentials** | [**WebhookCredentials**](WebhookCredentials.md) |  | [optional] 

## Example

```python
from opal_security.models.update_event_stream_info import UpdateEventStreamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEventStreamInfo from a JSON string
update_event_stream_info_instance = UpdateEventStreamInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateEventStreamInfo.to_json())

# convert the object into a dict
update_event_stream_info_dict = update_event_stream_info_instance.to_dict()
# create an instance of UpdateEventStreamInfo from a dict
update_event_stream_info_from_dict = UpdateEventStreamInfo.from_dict(update_event_stream_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


