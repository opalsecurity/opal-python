# OnCallScheduleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_call_schedules** | [**List[OnCallSchedule]**](OnCallSchedule.md) |  | 

## Example

```python
from opal_security.models.on_call_schedule_list import OnCallScheduleList

# TODO update the JSON string below
json = "{}"
# create an instance of OnCallScheduleList from a JSON string
on_call_schedule_list_instance = OnCallScheduleList.from_json(json)
# print the JSON string representation of the object
print(OnCallScheduleList.to_json())

# convert the object into a dict
on_call_schedule_list_dict = on_call_schedule_list_instance.to_dict()
# create an instance of OnCallScheduleList from a dict
on_call_schedule_list_from_dict = OnCallScheduleList.from_dict(on_call_schedule_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


