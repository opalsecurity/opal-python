# GroupRemoteInfoGitlabGroup

Remote info for Gitlab group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Gitlab group. | 

## Example

```python
from opal_security.models.group_remote_info_gitlab_group import GroupRemoteInfoGitlabGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoGitlabGroup from a JSON string
group_remote_info_gitlab_group_instance = GroupRemoteInfoGitlabGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoGitlabGroup.to_json())

# convert the object into a dict
group_remote_info_gitlab_group_dict = group_remote_info_gitlab_group_instance.to_dict()
# create an instance of GroupRemoteInfoGitlabGroup from a dict
group_remote_info_gitlab_group_from_dict = GroupRemoteInfoGitlabGroup.from_dict(group_remote_info_gitlab_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


