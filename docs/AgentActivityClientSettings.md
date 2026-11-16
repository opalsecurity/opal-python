# AgentActivityClientSettings

# AgentActivityClientSettings Object ### Description How a client should send batched agent activity for this organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_wait_seconds** | **float** | The minimum gap between two sends from one machine. Send at once when the last send was at least this long ago; otherwise wait until this long after the last send, and send what arrived meanwhile as one request. Between 0 and 300. | 
**max_events_per_request** | **int** | The most events one request to &#x60;/agent-activity&#x60; may carry. | 
**max_bytes_per_request** | **int** | The largest body, in bytes, &#x60;/agent-activity&#x60; accepts for a request with more than one event. A request with one event may be up to 1 MiB. | 
**max_requests_per_second** | **float** | The rate of batched requests one client should stay under. Can be below 1. | 
**burst_requests** | **int** | How many batched requests a client may send at once before the rate applies. At least 1. | 
**cache_seconds** | **int** | How long these settings may be kept before asking again. | 
**clients** | [**Dict[str, AgentActivityClientSetting]**](AgentActivityClientSetting.md) | What the organization chose on the Setup tab for each client that runs the hook, keyed by client (claude_code, codex, cursor). A client that is not listed keeps the defaults. | 

## Example

```python
from opal_security.models.agent_activity_client_settings import AgentActivityClientSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivityClientSettings from a JSON string
agent_activity_client_settings_instance = AgentActivityClientSettings.from_json(json)
# print the JSON string representation of the object
print(AgentActivityClientSettings.to_json())

# convert the object into a dict
agent_activity_client_settings_dict = agent_activity_client_settings_instance.to_dict()
# create an instance of AgentActivityClientSettings from a dict
agent_activity_client_settings_from_dict = AgentActivityClientSettings.from_dict(agent_activity_client_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


