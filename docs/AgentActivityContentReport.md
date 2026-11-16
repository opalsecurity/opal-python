# AgentActivityContentReport

# AgentActivityContentReport Object ### Description What Opal's hook kit adds to an event when it collects conversation content. Its presence means the sender collects content, like the `X-Opal-Content` header. The kit has already masked secrets in the texts and cut them to its own limit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistant_text** | **str** | Every text the model wrote in the turn, read from the session&#39;s transcript (&#x60;Stop&#x60;, &#x60;SubagentStop&#x60;). Preferred over &#x60;last_assistant_message&#x60;, which holds only the final message. | [optional] 
**thinking** | **str** | The model&#39;s thinking in the turn, when the transcript holds it as plain text. | [optional] 
**images** | [**AgentActivityImages**](AgentActivityImages.md) |  | [optional] 
**truncated** | **Dict[str, int]** | The fields the kit cut (&#x60;prompt&#x60;, &#x60;tool_response&#x60;, &#x60;assistant_text&#x60;, &#x60;last_assistant_message&#x60;, &#x60;thinking&#x60;), each with its size in bytes before the cut. A prompt or a tool result keeps its start; a turn&#39;s text and thinking keep their end. Sizes are stored up to 2147483647. | [optional] 

## Example

```python
from opal_security.models.agent_activity_content_report import AgentActivityContentReport

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivityContentReport from a JSON string
agent_activity_content_report_instance = AgentActivityContentReport.from_json(json)
# print the JSON string representation of the object
print(AgentActivityContentReport.to_json())

# convert the object into a dict
agent_activity_content_report_dict = agent_activity_content_report_instance.to_dict()
# create an instance of AgentActivityContentReport from a dict
agent_activity_content_report_from_dict = AgentActivityContentReport.from_dict(agent_activity_content_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


