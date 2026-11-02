# AgentKillSwitch

# AgentKillSwitch Object ### Description The org-level agent kill switch, and the activation that is in force or last was.  `active` is what matters; the rest is the record of how it got that way. An activation is in force only while it has not been deactivated AND `expires_at` is still in the future, and that is evaluated on every read - so `active` can be `false` on a row that was never explicitly turned off.  Everything below `active` describes the LATEST activation whether or not it is still in force, so an admin reading an inactive switch can still see who last turned it on and when it ended.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether agent tool calls are being denied right now. This is the field to read; it already accounts for expiry. | 
**activated_at** | **datetime** | When the latest activation was turned on. Absent if it never has been. | [optional] 
**activated_by_user_id** | **UUID** | The admin who turned it on. Absent when that user has since been hard-deleted - the activation record outlives them deliberately. | [optional] 
**expires_at** | **datetime** | When the latest activation stops denying on its own. In the past for an activation that already ran out. | [optional] 
**deactivated_at** | **datetime** | When the latest activation was turned off before its expiry, either by an admin or by being superseded. Absent when it ended at &#x60;expires_at&#x60;, or has not ended. | [optional] 
**reason** | **str** | The admin&#39;s stated reason. Not an internal note - it is shown to the developer whose tool call is denied, in their own terminal. | [optional] 

## Example

```python
from opal_security.models.agent_kill_switch import AgentKillSwitch

# TODO update the JSON string below
json = "{}"
# create an instance of AgentKillSwitch from a JSON string
agent_kill_switch_instance = AgentKillSwitch.from_json(json)
# print the JSON string representation of the object
print(AgentKillSwitch.to_json())

# convert the object into a dict
agent_kill_switch_dict = agent_kill_switch_instance.to_dict()
# create an instance of AgentKillSwitch from a dict
agent_kill_switch_from_dict = AgentKillSwitch.from_dict(agent_kill_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


