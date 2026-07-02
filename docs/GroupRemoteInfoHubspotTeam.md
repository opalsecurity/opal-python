# GroupRemoteInfoHubspotTeam

Remote info for HubSpot team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** | The ID of the HubSpot team. | 

## Example

```python
from opal_security.models.group_remote_info_hubspot_team import GroupRemoteInfoHubspotTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoHubspotTeam from a JSON string
group_remote_info_hubspot_team_instance = GroupRemoteInfoHubspotTeam.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoHubspotTeam.to_json())

# convert the object into a dict
group_remote_info_hubspot_team_dict = group_remote_info_hubspot_team_instance.to_dict()
# create an instance of GroupRemoteInfoHubspotTeam from a dict
group_remote_info_hubspot_team_from_dict = GroupRemoteInfoHubspotTeam.from_dict(group_remote_info_hubspot_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


