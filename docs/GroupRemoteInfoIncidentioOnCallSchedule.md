# GroupRemoteInfoIncidentioOnCallSchedule

Remote info for Incident.io on-call schedule group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** | The id of the Incident.io on-call schedule. | 

## Example

```python
from opal_security.models.group_remote_info_incidentio_on_call_schedule import GroupRemoteInfoIncidentioOnCallSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoIncidentioOnCallSchedule from a JSON string
group_remote_info_incidentio_on_call_schedule_instance = GroupRemoteInfoIncidentioOnCallSchedule.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoIncidentioOnCallSchedule.to_json())

# convert the object into a dict
group_remote_info_incidentio_on_call_schedule_dict = group_remote_info_incidentio_on_call_schedule_instance.to_dict()
# create an instance of GroupRemoteInfoIncidentioOnCallSchedule from a dict
group_remote_info_incidentio_on_call_schedule_from_dict = GroupRemoteInfoIncidentioOnCallSchedule.from_dict(group_remote_info_incidentio_on_call_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


