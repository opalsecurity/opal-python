# GroupRemoteInfoAsanaTeam

Remote info for Asana Team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_gid** | **str** | The team gid of the Asana Team. | 
**workspace_gid** | **str** | The workspace gid of the Asana Team. | [optional] 

## Example

```python
from opal_security.models.group_remote_info_asana_team import GroupRemoteInfoAsanaTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoAsanaTeam from a JSON string
group_remote_info_asana_team_instance = GroupRemoteInfoAsanaTeam.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoAsanaTeam.to_json())

# convert the object into a dict
group_remote_info_asana_team_dict = group_remote_info_asana_team_instance.to_dict()
# create an instance of GroupRemoteInfoAsanaTeam from a dict
group_remote_info_asana_team_from_dict = GroupRemoteInfoAsanaTeam.from_dict(group_remote_info_asana_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


