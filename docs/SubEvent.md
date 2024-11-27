# SubEvent

# Sub event Object ### Description The `SubEvent` object is used to represent a subevent.  ### Usage Example Fetch from the `LIST Events` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_event_type** | **str** | The subevent type. | 

## Example

```python
from opal_security.models.sub_event import SubEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SubEvent from a JSON string
sub_event_instance = SubEvent.from_json(json)
# print the JSON string representation of the object
print(SubEvent.to_json())

# convert the object into a dict
sub_event_dict = sub_event_instance.to_dict()
# create an instance of SubEvent from a dict
sub_event_from_dict = SubEvent.from_dict(sub_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


