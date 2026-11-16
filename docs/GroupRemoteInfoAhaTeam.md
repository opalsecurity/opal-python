# GroupRemoteInfoAhaTeam

Remote info for Aha Team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The group id of the Aha Team. | 

## Example

```python
from opal_security.models.group_remote_info_aha_team import GroupRemoteInfoAhaTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoAhaTeam from a JSON string
group_remote_info_aha_team_instance = GroupRemoteInfoAhaTeam.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoAhaTeam.to_json())

# convert the object into a dict
group_remote_info_aha_team_dict = group_remote_info_aha_team_instance.to_dict()
# create an instance of GroupRemoteInfoAhaTeam from a dict
group_remote_info_aha_team_from_dict = GroupRemoteInfoAhaTeam.from_dict(group_remote_info_aha_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


