# UpdateOwnerInfo

# UpdateOwnerInfo Object ### Description The `UpdateOwnerInfo` object is used as an input to the UpdateOwner API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** | The ID of the owner. | 
**name** | **str** | The name of the owner. | [optional] 
**description** | **str** | A description of the owner. | [optional] 
**access_request_escalation_period** | **int** | The amount of time (in minutes) before the next reviewer is notified. Use 0 to remove escalation policy. | [optional] 
**reviewer_message_channel_id** | **str** | The message channel id for the reviewer channel. Use \&quot;\&quot; to remove an existing message channel. | [optional] 
**source_group_id** | **str** | Sync this owner&#39;s user list with a source group. Use \&quot;\&quot; to remove an existing source group. | [optional] 

## Example

```python
from opal_security.models.update_owner_info import UpdateOwnerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOwnerInfo from a JSON string
update_owner_info_instance = UpdateOwnerInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateOwnerInfo.to_json())

# convert the object into a dict
update_owner_info_dict = update_owner_info_instance.to_dict()
# create an instance of UpdateOwnerInfo from a dict
update_owner_info_from_dict = UpdateOwnerInfo.from_dict(update_owner_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


