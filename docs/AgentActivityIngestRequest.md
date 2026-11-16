# AgentActivityIngestRequest

# AgentActivityIngestRequest Object ### Description A batch of agent activity events.  Three body shapes are accepted: this envelope (`{\"events\": [...]}`), a bare JSON array of `AgentActivityEvent`, and a single `AgentActivityEvent` object. The last exists so a Claude Code hook can POST here directly, since a hook sends one bare payload per event and cannot wrap it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AgentActivityEvent]**](AgentActivityEvent.md) |  | [optional] 

## Example

```python
from opal_security.models.agent_activity_ingest_request import AgentActivityIngestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivityIngestRequest from a JSON string
agent_activity_ingest_request_instance = AgentActivityIngestRequest.from_json(json)
# print the JSON string representation of the object
print(AgentActivityIngestRequest.to_json())

# convert the object into a dict
agent_activity_ingest_request_dict = agent_activity_ingest_request_instance.to_dict()
# create an instance of AgentActivityIngestRequest from a dict
agent_activity_ingest_request_from_dict = AgentActivityIngestRequest.from_dict(agent_activity_ingest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


