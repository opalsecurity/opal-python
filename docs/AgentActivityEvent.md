# AgentActivityEvent

# AgentActivityEvent Object ### Description One activity event reported by an agent runtime: a Claude Code or Codex hook payload, or a Cursor hook payload the Opal kit rewrote into the same shape, posted either by the hook itself or by a relay that batches them.  Only the fields below are read; everything else in the payload is parsed and **discarded**, never persisted. That includes `transcript_path` / `scratchpad_dir` (absolute paths on an employee's own laptop, which Opal cannot govern and should not be accumulating).  `prompt`, `tool_response` and `last_assistant_message` (the conversation content) are stored only when the sender collects them (`opal_content` on the event, or the `X-Opal-Content` header) and the organization stores content. Secrets in the shapes Opal recognizes are masked and each text is cut to the organization's limit before it is written. Otherwise they are discarded too.  `tool_input` IS now read and stored. It was previously discarded pending a data-handling decision; that decision has since been made, and without arguments no policy can name what a call acted on - a rule about a file path, a command family or a web domain refers to something that exists only inside `tool_input`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hook_event_name** | **str** | Which hook fired, e.g. &#x60;PostToolUse&#x60;, &#x60;PreToolUse&#x60;, &#x60;PermissionDenied&#x60;. Required; an event with no name cannot be interpreted and is rejected. | 
**tool_input** | **Dict[str, object]** | The call&#39;s arguments, as the runtime sent them. Server-defined for an MCP tool; a fixed shape per built-in (&#x60;command&#x60; for Bash, &#x60;file_path&#x60; for Edit, &#x60;url&#x60; for WebFetch).  Stored as sent, and separately reduced to a normalized target the activity feed and policy can match on. The stored copy is the record of fact; the derived target is recomputed whenever the extractor improves.  Capped before storage. A capped payload is no longer valid JSON, so the row records that it was capped rather than leaving each reader to discover it by failing to parse.  A value that is not an object (Codex sends a string when a model&#39;s function arguments are not valid JSON) is stored as &#x60;{\&quot;raw\&quot;: &lt;value&gt;}&#x60; rather than rejected. | [optional] 
**session_id** | **str** | The agent session this event belongs to. Opaque to Opal. | [optional] 
**prompt_id** | **str** | Groups every tool call made under one user instruction, so a run can be read back as the instruction that caused it rather than as unrelated rows. | [optional] 
**turn_id** | **str** | Codex&#39;s id for one user turn. Codex sends no &#x60;prompt_id&#x60;, so for a Codex event this is stored as the prompt id. Together with &#x60;model&#x60;, and with no &#x60;prompt_id&#x60;, it also marks an event as coming from Codex when &#x60;opal_reported.client&#x60; is absent. | [optional] 
**model** | **str** | The model the runtime was using, as Codex reports it. Read only to tell Codex from Claude Code; not stored. | [optional] 
**cursor_version** | **str** | The Cursor version, which Cursor adds to every hook input. Read only to mark an event as coming from Cursor when &#x60;opal_reported.client&#x60; is absent; not stored. A Cursor tool-call event named &#x60;preToolUse&#x60;, &#x60;postToolUse&#x60; or &#x60;postToolUseFailure&#x60; is stored under the Claude Code name for the same event. | [optional] 
**agent_id** | **str** | Set only when the call came from an autonomous subagent rather than the session a person is typing into. Stored as &#x60;subagent_id&#x60; - Opal&#39;s own &#x60;agent_id&#x60; already means something else. | [optional] 
**agent_type** | **str** | The subagent&#39;s type, e.g. &#x60;general-purpose&#x60;. Set alongside &#x60;agent_id&#x60;. | [optional] 
**permission_mode** | **str** | The session&#39;s permission mode, e.g. &#x60;default&#x60;, &#x60;acceptEdits&#x60;, &#x60;bypassPermissions&#x60;. A session running &#x60;bypassPermissions&#x60; had no approval gate in front of any tool call it made. | [optional] 
**actor_email** | **str** | The identity the sender reports for this specific event. **Unverified**, the same as &#x60;X-Opal-Actor&#x60;, and used only when neither the API key nor that header identified a developer. An &#x60;http&#x60; hook cannot populate this; a &#x60;command&#x60;-type hook or a relay can (&#x60;$USER&#x60;, a hostname, &#x60;git config user.email&#x60;), which is why it is per-event rather than per-request - a relay can batch several developers. | [optional] 
**opal_reported** | [**AgentActivityOpalReported**](AgentActivityOpalReported.md) |  | [optional] 
**duration_ms** | **object** |  | [optional] 
**transcript_path** | **str** | Read at ingest **only** to parse an operating-system username out of, as the last-resort attribution step, and then discarded. The path itself is never stored: it is an absolute path on an employee&#39;s laptop and Opal has no business accumulating those. | [optional] 
**tool_name** | **str** | The tool invoked, for tool-scoped events. Empty for session-level events.  An MCP tool is named &#x60;mcp__&lt;server&gt;__&lt;tool&gt;&#x60;. The whole string is stored as sent, and the server and the tool are also stored in their own fields (see &#x60;mcp_server&#x60;). | [optional] 
**mcp_server** | [**AgentActivityMcpServer**](AgentActivityMcpServer.md) |  | [optional] 
**opal_mcp_server** | [**AgentActivityOpalMcpServer**](AgentActivityOpalMcpServer.md) |  | [optional] 
**tool_use_id** | **str** | The tool invocation&#39;s id, used together with &#x60;hook_event_name&#x60; to deduplicate a retried delivery. Absent on events that carry none, which are stored at-least-once unless they are a prompt or the end of a turn with &#x60;session_id&#x60; and &#x60;prompt_id&#x60;, or carry &#x60;opal_event_id&#x60;. | [optional] 
**opal_event_id** | **str** | An id Opal&#39;s hook kit gives each event it holds for sending, so that a retried delivery of an event without a &#x60;tool_use_id&#x60; (a prompt, the end of a turn) is stored once. Used only for an event that has no &#x60;tool_use_id&#x60; and is not a tool-call event, and only when it is 8 to 64 letters, digits and dashes; otherwise ignored. | [optional] 
**cwd** | **str** | The working directory the agent was operating in. | [optional] 
**timestamp** | **datetime** | When the client says the event occurred (RFC 3339). Clamped server-side to a window around receipt, because a client-controlled sort key is otherwise a way to pin rows to the top of every list. Defaults to receipt time when absent or unparseable. | [optional] 
**prompt** | **object** |  | [optional] 
**tool_response** | **object** |  | [optional] 
**last_assistant_message** | **object** |  | [optional] 
**opal_content** | [**AgentActivityContentReport**](AgentActivityContentReport.md) |  | [optional] 

## Example

```python
from opal_security.models.agent_activity_event import AgentActivityEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivityEvent from a JSON string
agent_activity_event_instance = AgentActivityEvent.from_json(json)
# print the JSON string representation of the object
print(AgentActivityEvent.to_json())

# convert the object into a dict
agent_activity_event_dict = agent_activity_event_instance.to_dict()
# create an instance of AgentActivityEvent from a dict
agent_activity_event_from_dict = AgentActivityEvent.from_dict(agent_activity_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


