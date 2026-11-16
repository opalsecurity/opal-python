# SetAgentKillSwitchRequest

# SetAgentKillSwitchRequest Object ### Description Turns the agent kill switch on or off.  Setting `active` to `true` while it is already on supersedes the current activation rather than extending it: the old row keeps its own reason and window as part of the audit trail, and a new one starts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | True denies agent tool calls for this organization; false lifts the denial. | 
**duration_minutes** | **int** | How long the denial lasts, from now. Ignored when &#x60;active&#x60; is false. Capped server-side - a kill switch with no end is how an organization discovers months later that its engineers have been quietly working around it. | [optional] 
**reason** | **str** | Why. Shown verbatim to the developer whose tool call is denied, so write it for them rather than for the audit log - it is the only explanation they get. | [optional] 

## Example

```python
from opal_security.models.set_agent_kill_switch_request import SetAgentKillSwitchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAgentKillSwitchRequest from a JSON string
set_agent_kill_switch_request_instance = SetAgentKillSwitchRequest.from_json(json)
# print the JSON string representation of the object
print(SetAgentKillSwitchRequest.to_json())

# convert the object into a dict
set_agent_kill_switch_request_dict = set_agent_kill_switch_request_instance.to_dict()
# create an instance of SetAgentKillSwitchRequest from a dict
set_agent_kill_switch_request_from_dict = SetAgentKillSwitchRequest.from_dict(set_agent_kill_switch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


