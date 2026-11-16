# AgentActivityClientSetting

# AgentActivityClientSetting Object ### Description What the organization chose for one client that runs the hook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports_tool_calls** | **bool** | Whether the client reports tool calls. When false its hook sends nothing and lets every tool call run, and Opal stores nothing the client still sends. | 
**conversation_content** | **str** | Who decides whether the client&#39;s conversation content (prompts, what each tool returned, the model&#39;s replies) is sent and stored. &#x60;always&#x60; sends it from every machine; &#x60;never&#x60; sends none, even from a machine installed with --content, and Opal stores none; &#x60;person_decides&#x60; leaves it to whether the machine was installed with --content. Absent for a client whose hook sends no conversation content (codex). | [optional] 

## Example

```python
from opal_security.models.agent_activity_client_setting import AgentActivityClientSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivityClientSetting from a JSON string
agent_activity_client_setting_instance = AgentActivityClientSetting.from_json(json)
# print the JSON string representation of the object
print(AgentActivityClientSetting.to_json())

# convert the object into a dict
agent_activity_client_setting_dict = agent_activity_client_setting_instance.to_dict()
# create an instance of AgentActivityClientSetting from a dict
agent_activity_client_setting_from_dict = AgentActivityClientSetting.from_dict(agent_activity_client_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


