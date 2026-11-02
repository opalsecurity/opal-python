# AgentActivityIngestResult

# AgentActivityIngestResult Object ### Description What one ingest request actually did.  `received` and `stored` differ when a delivery was retried and deduplicated. `attributed` and `unattributed` sum to `received` rather than to `stored`, because attribution happens before deduplication. Unattributed events are kept, not dropped: activity Opal cannot tie to a governed agent is itself a governance finding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**received** | **int** | Events parsed out of the request body. | 
**stored** | **int** | Rows actually written. Lower than &#x60;received&#x60; when a retried delivery was deduplicated on &#x60;tool_use_id&#x60;. | 
**attributed** | **int** | Events that resolved to an agent in this organization. | 
**unattributed** | **int** | Events that resolved to no agent, and are therefore visible only in the unattributed activity list. A persistently high value means the reporting clients are not sending an identity Opal can resolve. | 

## Example

```python
from opal_security.models.agent_activity_ingest_result import AgentActivityIngestResult

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivityIngestResult from a JSON string
agent_activity_ingest_result_instance = AgentActivityIngestResult.from_json(json)
# print the JSON string representation of the object
print(AgentActivityIngestResult.to_json())

# convert the object into a dict
agent_activity_ingest_result_dict = agent_activity_ingest_result_instance.to_dict()
# create an instance of AgentActivityIngestResult from a dict
agent_activity_ingest_result_from_dict = AgentActivityIngestResult.from_dict(agent_activity_ingest_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


