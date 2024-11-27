# CreateOwnerInfo

# CreateOwnerInfo Object ### Description The `CreateOwnerInfo` object is used to store creation info for an owner.  ### Usage Example Use in the `POST Owners` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the owner. | 
**description** | **str** | A description of the owner. | [optional] 
**access_request_escalation_period** | **int** | The amount of time (in minutes) before the next reviewer is notified. Use 0 to remove escalation policy. | [optional] 
**user_ids** | **List[str]** | Users to add to the created owner. If setting a source_group_id this list must be empty. | 
**reviewer_message_channel_id** | **str** | The message channel id for the reviewer channel. | [optional] 
**source_group_id** | **str** | Sync this owner&#39;s user list with a source group. | [optional] 

## Example

```python
from opal_security.models.create_owner_info import CreateOwnerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOwnerInfo from a JSON string
create_owner_info_instance = CreateOwnerInfo.from_json(json)
# print the JSON string representation of the object
print(CreateOwnerInfo.to_json())

# convert the object into a dict
create_owner_info_dict = create_owner_info_instance.to_dict()
# create an instance of CreateOwnerInfo from a dict
create_owner_info_from_dict = CreateOwnerInfo.from_dict(create_owner_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


