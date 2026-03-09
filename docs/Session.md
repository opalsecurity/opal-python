# Session

# Session Object ### Description The `Session` object is used to represent an access session. Some resources can be accessed temporarily via a time-bounded session.  ### Usage Example Fetch from the `LIST Sessions` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | The ID of the connection. | 
**user_id** | **str** | The ID of the user. | 
**resource_id** | **str** | The ID of the resource. | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | 
**expiration_date** | **datetime** | The day and time the user&#39;s access will expire. | 

## Example

```python
from opal_security.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print(Session.to_json())

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_from_dict = Session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


