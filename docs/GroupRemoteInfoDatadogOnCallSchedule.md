# GroupRemoteInfoDatadogOnCallSchedule

Remote info for Datadog on-call schedule group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** | The id of the Datadog on-call schedule. | 

## Example

```python
from opal_security.models.group_remote_info_datadog_on_call_schedule import GroupRemoteInfoDatadogOnCallSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoDatadogOnCallSchedule from a JSON string
group_remote_info_datadog_on_call_schedule_instance = GroupRemoteInfoDatadogOnCallSchedule.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoDatadogOnCallSchedule.to_json())

# convert the object into a dict
group_remote_info_datadog_on_call_schedule_dict = group_remote_info_datadog_on_call_schedule_instance.to_dict()
# create an instance of GroupRemoteInfoDatadogOnCallSchedule from a dict
group_remote_info_datadog_on_call_schedule_from_dict = GroupRemoteInfoDatadogOnCallSchedule.from_dict(group_remote_info_datadog_on_call_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


