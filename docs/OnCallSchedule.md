# OnCallSchedule

# OnCallSchedule Object ### Description The `OnCallSchedule` object is used to represent an on call schedule.  ### Usage Example Update a groups on call schedule from the `UPDATE Groups` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_call_schedule_id** | **str** | The ID of the on-call schedule. | [optional] 
**third_party_provider** | [**OnCallScheduleProviderEnum**](OnCallScheduleProviderEnum.md) |  | [optional] 
**remote_id** | **str** | The remote ID of the on call schedule | [optional] 
**name** | **str** | The name of the on call schedule. | [optional] 

## Example

```python
from opal_security.models.on_call_schedule import OnCallSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of OnCallSchedule from a JSON string
on_call_schedule_instance = OnCallSchedule.from_json(json)
# print the JSON string representation of the object
print(OnCallSchedule.to_json())

# convert the object into a dict
on_call_schedule_dict = on_call_schedule_instance.to_dict()
# create an instance of OnCallSchedule from a dict
on_call_schedule_from_dict = OnCallSchedule.from_dict(on_call_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


