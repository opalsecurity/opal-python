# GroupRemoteInfoRootlyOnCallSchedule

Remote info for Rootly on-call schedule group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** | The id of the Rootly on-call schedule. | 

## Example

```python
from opal_security.models.group_remote_info_rootly_on_call_schedule import GroupRemoteInfoRootlyOnCallSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoRootlyOnCallSchedule from a JSON string
group_remote_info_rootly_on_call_schedule_instance = GroupRemoteInfoRootlyOnCallSchedule.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoRootlyOnCallSchedule.to_json())

# convert the object into a dict
group_remote_info_rootly_on_call_schedule_dict = group_remote_info_rootly_on_call_schedule_instance.to_dict()
# create an instance of GroupRemoteInfoRootlyOnCallSchedule from a dict
group_remote_info_rootly_on_call_schedule_from_dict = GroupRemoteInfoRootlyOnCallSchedule.from_dict(group_remote_info_rootly_on_call_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


