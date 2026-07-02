# GroupRemoteInfoSlackUserGroup

Remote info for Slack user group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Slack user group. | 

## Example

```python
from opal_security.models.group_remote_info_slack_user_group import GroupRemoteInfoSlackUserGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoSlackUserGroup from a JSON string
group_remote_info_slack_user_group_instance = GroupRemoteInfoSlackUserGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoSlackUserGroup.to_json())

# convert the object into a dict
group_remote_info_slack_user_group_dict = group_remote_info_slack_user_group_instance.to_dict()
# create an instance of GroupRemoteInfoSlackUserGroup from a dict
group_remote_info_slack_user_group_from_dict = GroupRemoteInfoSlackUserGroup.from_dict(group_remote_info_slack_user_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


