# Event

# Event Object ### Description The `Event` object is used to represent an event.  ### Usage Example Fetch from the `LIST Events` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | The ID of the event. | 
**actor_user_id** | **str** | The ID of the actor user. | 
**actor_name** | **object** |  | 
**actor_email** | **str** | The email of the actor user. | [optional] 
**event_type** | **str** | The event type. | 
**created_at** | **datetime** | The day and time the event was created. | 
**actor_ip_address** | **str** | The IP address of the event actor. | [optional] 
**api_token_name** | **str** | The name of the API token used to create the event. | [optional] 
**api_token_preview** | **str** | The preview of the API token used to create the event. | [optional] 
**sub_events** | [**List[SubEvent]**](SubEvent.md) |  | [optional] 

## Example

```python
from opal_security.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


