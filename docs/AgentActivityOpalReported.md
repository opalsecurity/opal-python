# AgentActivityOpalReported

# AgentActivityOpalReported Object ### Description What the sending machine says about who and what it is, added by the Opal hook script. Every field is optional and **unverified**: whoever controls the machine controls them. They can disagree, and Opal keeps every one that is present, each cut to a fixed length (254 characters for an email, 64 for `os_user`, 255 for `hostname`) with control characters removed.  The emails are also tried, in the order below and after the `X-Opal-Actor` header, to find the agent, so a person without a git email can still match through their Claude account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured_email** | **str** | An email set by an administrator, an MDM profile or the installer. | [optional] 
**claude_account_email** | **str** | The email of the account Claude Code is signed in with. | [optional] 
**codex_account_email** | **str** | The email of the ChatGPT account Codex is signed in with. | [optional] 
**codex_auth_mode** | **str** | How Codex is signed in, from &#x60;auth_mode&#x60; in its &#x60;auth.json&#x60;: &#x60;chatgpt&#x60; for a ChatGPT sign-in, &#x60;apikey&#x60; for an API key. In an organization that has turned on person agents, a Codex call from a person who owns no OpenAI agent creates \&quot;&lt;Name&gt;&#39;s ChatGPT\&quot; for a ChatGPT sign-in and \&quot;&lt;Name&gt;&#39;s OpenAI\&quot; for an API key. Without it, no agent is created. | [optional] 
**chatgpt_account_email** | **str** | The email of the ChatGPT account the sending runtime is signed in with. | [optional] 
**cursor_account_email** | **str** | The email of the account Cursor is signed in with, from the &#x60;user_email&#x60; of Cursor&#39;s hook input. Tried before the other emails here. | [optional] 
**client** | **str** | Which agent runtime sent the event: &#x60;claude_code&#x60;, &#x60;codex&#x60;, &#x60;cursor&#x60;, &#x60;openai_agents_python&#x60;, &#x60;openai_agents_js&#x60;, &#x60;chatgpt&#x60; or &#x60;chatgpt_workspace_agent&#x60;. Any other value is stored as &#x60;unknown&#x60;. When absent, an event carrying &#x60;cursor_version&#x60; is Cursor, one carrying &#x60;turn_id&#x60; and &#x60;model&#x60; and no &#x60;prompt_id&#x60; is Codex, and anything else is Claude Code. | [optional] 
**git_email** | **str** | The machine&#39;s global &#x60;git config user.email&#x60;. | [optional] 
**os_user** | **str** | The operating-system username. Not used to find an agent. | [optional] 
**hostname** | **str** | The machine&#39;s name. The &#x60;X-Opal-Host&#x60; header wins when it names a different machine. | [optional] 

## Example

```python
from opal_security.models.agent_activity_opal_reported import AgentActivityOpalReported

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivityOpalReported from a JSON string
agent_activity_opal_reported_instance = AgentActivityOpalReported.from_json(json)
# print the JSON string representation of the object
print(AgentActivityOpalReported.to_json())

# convert the object into a dict
agent_activity_opal_reported_dict = agent_activity_opal_reported_instance.to_dict()
# create an instance of AgentActivityOpalReported from a dict
agent_activity_opal_reported_from_dict = AgentActivityOpalReported.from_dict(agent_activity_opal_reported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


