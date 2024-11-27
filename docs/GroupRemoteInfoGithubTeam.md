# GroupRemoteInfoGithubTeam

Remote info for GitHub team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** | The id of the GitHub team. | [optional] 
**team_slug** | **str** | The slug of the GitHub team. | 

## Example

```python
from opal_security.models.group_remote_info_github_team import GroupRemoteInfoGithubTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoGithubTeam from a JSON string
group_remote_info_github_team_instance = GroupRemoteInfoGithubTeam.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoGithubTeam.to_json())

# convert the object into a dict
group_remote_info_github_team_dict = group_remote_info_github_team_instance.to_dict()
# create an instance of GroupRemoteInfoGithubTeam from a dict
group_remote_info_github_team_from_dict = GroupRemoteInfoGithubTeam.from_dict(group_remote_info_github_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


