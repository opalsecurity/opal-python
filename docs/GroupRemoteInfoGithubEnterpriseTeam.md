# GroupRemoteInfoGithubEnterpriseTeam

Remote info for GitHub Enterprise team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_slug** | **str** | The slug of the GitHub Enterprise team. | 

## Example

```python
from opal_security.models.group_remote_info_github_enterprise_team import GroupRemoteInfoGithubEnterpriseTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoGithubEnterpriseTeam from a JSON string
group_remote_info_github_enterprise_team_instance = GroupRemoteInfoGithubEnterpriseTeam.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoGithubEnterpriseTeam.to_json())

# convert the object into a dict
group_remote_info_github_enterprise_team_dict = group_remote_info_github_enterprise_team_instance.to_dict()
# create an instance of GroupRemoteInfoGithubEnterpriseTeam from a dict
group_remote_info_github_enterprise_team_from_dict = GroupRemoteInfoGithubEnterpriseTeam.from_dict(group_remote_info_github_enterprise_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


