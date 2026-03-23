# OnCallScheduleIDList

A list of on call schedule Opal UUIDs. To get the matching remote IDs, use the /on-call-schedules endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_call_schedule_ids** | **List[str]** |  | 

## Example

```python
from opal_security.models.on_call_schedule_id_list import OnCallScheduleIDList

# TODO update the JSON string below
json = "{}"
# create an instance of OnCallScheduleIDList from a JSON string
on_call_schedule_id_list_instance = OnCallScheduleIDList.from_json(json)
# print the JSON string representation of the object
print(OnCallScheduleIDList.to_json())

# convert the object into a dict
on_call_schedule_id_list_dict = on_call_schedule_id_list_instance.to_dict()
# create an instance of OnCallScheduleIDList from a dict
on_call_schedule_id_list_from_dict = OnCallScheduleIDList.from_dict(on_call_schedule_id_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


