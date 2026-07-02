# GroupRemoteInfoGrafanaTeam

Remote info for Grafana team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** | The ID of the team. | 

## Example

```python
from opal_security.models.group_remote_info_grafana_team import GroupRemoteInfoGrafanaTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoGrafanaTeam from a JSON string
group_remote_info_grafana_team_instance = GroupRemoteInfoGrafanaTeam.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoGrafanaTeam.to_json())

# convert the object into a dict
group_remote_info_grafana_team_dict = group_remote_info_grafana_team_instance.to_dict()
# create an instance of GroupRemoteInfoGrafanaTeam from a dict
group_remote_info_grafana_team_from_dict = GroupRemoteInfoGrafanaTeam.from_dict(group_remote_info_grafana_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


