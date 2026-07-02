# GroupRemoteInfoZendeskGroup

Remote info for Zendesk group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the Zendesk group. | 

## Example

```python
from opal_security.models.group_remote_info_zendesk_group import GroupRemoteInfoZendeskGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoZendeskGroup from a JSON string
group_remote_info_zendesk_group_instance = GroupRemoteInfoZendeskGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoZendeskGroup.to_json())

# convert the object into a dict
group_remote_info_zendesk_group_dict = group_remote_info_zendesk_group_instance.to_dict()
# create an instance of GroupRemoteInfoZendeskGroup from a dict
group_remote_info_zendesk_group_from_dict = GroupRemoteInfoZendeskGroup.from_dict(group_remote_info_zendesk_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


