# GroupRemoteInfoJiraGroup

Remote info for Jira group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the Jira group. | 

## Example

```python
from opal_security.models.group_remote_info_jira_group import GroupRemoteInfoJiraGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoJiraGroup from a JSON string
group_remote_info_jira_group_instance = GroupRemoteInfoJiraGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoJiraGroup.to_json())

# convert the object into a dict
group_remote_info_jira_group_dict = group_remote_info_jira_group_instance.to_dict()
# create an instance of GroupRemoteInfoJiraGroup from a dict
group_remote_info_jira_group_from_dict = GroupRemoteInfoJiraGroup.from_dict(group_remote_info_jira_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


