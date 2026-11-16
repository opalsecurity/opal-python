# opal_security.AgentActivityApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anthropic_inference_hook**](AgentActivityApi.md#anthropic_inference_hook) | **POST** /inference-hooks/anthropic | Anthropic inference hook verdict
[**get_agent_activity_client_settings**](AgentActivityApi.md#get_agent_activity_client_settings) | **GET** /agent-activity/client-settings | Get agent activity client settings
[**get_agent_kill_switch**](AgentActivityApi.md#get_agent_kill_switch) | **GET** /agent-kill-switch | Get the agent kill switch
[**report_agent_activity**](AgentActivityApi.md#report_agent_activity) | **POST** /agent-activity | Report agent activity
[**report_mcp_config**](AgentActivityApi.md#report_mcp_config) | **POST** /agent-activity/mcp-config | Report MCP server configuration
[**set_agent_kill_switch**](AgentActivityApi.md#set_agent_kill_switch) | **PUT** /agent-kill-switch | Set the agent kill switch


# **anthropic_inference_hook**
> AnthropicInferenceHookVerdict anthropic_inference_hook(request_body)

Anthropic inference hook verdict

**Prototype (AG-336).** The AI security server endpoint for Anthropic Inference hooks. Anthropic POSTs each governed frame here and waits for an allow or deny verdict. Configure it in claude.ai with this URL and a custom `Authorization: Bearer <Opal API key>` request header.

`tool_call` frames are evaluated against the organization's runtime policy rules. One verdict covers every tool call in the frame. Every other frame type, including `prompt`, is allowed without inspection. Any non-200 response is a webhook failure, so the organization's Anthropic failure-handling setting decides the outcome.

Once the organization saves its Anthropic signing secret in Opal, a `tool_call` frame must carry a valid Standard Webhooks signature (`webhook-id`, `webhook-timestamp`, `webhook-signature`), or it is answered with a 401.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.anthropic_inference_hook_verdict import AnthropicInferenceHookVerdict
from opal_security.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal_security.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal_security.AgentActivityApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Anthropic inference hook verdict
        api_response = api_instance.anthropic_inference_hook(request_body)
        print("The response of AgentActivityApi->anthropic_inference_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentActivityApi->anthropic_inference_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AnthropicInferenceHookVerdict**](AnthropicInferenceHookVerdict.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The verdict for the frame. |  -  |
**401** | The frame is unsigned or its signature does not verify. Anthropic applies the organization&#39;s failure handling. |  -  |
**500** | The frame could not be evaluated. Anthropic applies the organization&#39;s failure handling. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_activity_client_settings**
> AgentActivityClientSettings get_agent_activity_client_settings()

Get agent activity client settings

**Prototype.** Returns how a client that reports agent activity (today, the Claude Code hook kit on a developer's machine) should send batched events for this organization: the minimum gap between two sends from one machine, the most events and bytes one request to `/agent-activity` may carry, the request rate to stay under, and how long the answer may be cached.

The rate is derived from the organization's own rate limit for `POST /agent-activity`, which every client in the organization shares: the clients that asked for these settings in the last cache period or two share half of it evenly, and the checks before tool calls keep the other half. A check before a tool call is not batched and should not be held back by this rate. A client is counted by its `X-Opal-Host` and `X-Opal-Actor` headers, so it should send the same ones it sends to `/agent-activity`.

A client should ask for these at most once per `cache_seconds`, and keep using its last answer, or its own defaults, when it cannot get one.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.agent_activity_client_settings import AgentActivityClientSettings
from opal_security.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal_security.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal_security.AgentActivityApi(api_client)

    try:
        # Get agent activity client settings
        api_response = api_instance.get_agent_activity_client_settings()
        print("The response of AgentActivityApi->get_agent_activity_client_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentActivityApi->get_agent_activity_client_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AgentActivityClientSettings**](AgentActivityClientSettings.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The settings for this organization. |  -  |
**403** | Agent activity ingest is not enabled for this organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_kill_switch**
> AgentKillSwitch get_agent_kill_switch()

Get the agent kill switch

**Prototype (AG-297).** Returns whether agent tool calls are currently being denied for this organization, and the activation that is in force or that last was.

`active` is evaluated against the clock on every read, so an activation past its `expires_at` reads as inactive without anything having swept it.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.agent_kill_switch import AgentKillSwitch
from opal_security.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal_security.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal_security.AgentActivityApi(api_client)

    try:
        # Get the agent kill switch
        api_response = api_instance.get_agent_kill_switch()
        print("The response of AgentActivityApi->get_agent_kill_switch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentActivityApi->get_agent_kill_switch: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AgentKillSwitch**](AgentKillSwitch.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current state of the kill switch. |  -  |
**403** | The caller is not an admin, or the agent kill switch is not enabled for this organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_agent_activity**
> AgentActivityIngestResult report_agent_activity(agent_activity_ingest_request, x_opal_actor=x_opal_actor, x_opal_host=x_opal_host, x_opal_content=x_opal_content)

Report agent activity

**Prototype (AG-285).** Reports activity observed by an agent runtime on a developer's machine - today, Claude Code hook events.

This is **telemetry from cooperating machines, not attestation**. Opal can only see what a configured, consenting client chooses to send, cannot verify that a fleet is configured at all, and has no way to detect a machine that is reporting nothing. Absence of activity for an agent therefore means "nothing was reported", never "the agent did nothing".

The request body is either a batch envelope (`{"events": [...]}`), a bare JSON array of events, or a single raw Claude Code hook payload - the last so a hook can POST here directly with no relay in between.

The bearer token establishes the **organization** and nothing finer. No field in the payload is treated as an identity claim Opal trusts: the actor headers below are used for best-effort attribution and display only. Events that cannot be attributed to an agent are retained and surfaced as unattributed activity rather than dropped.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.agent_activity_ingest_request import AgentActivityIngestRequest
from opal_security.models.agent_activity_ingest_result import AgentActivityIngestResult
from opal_security.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal_security.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal_security.AgentActivityApi(api_client)
    agent_activity_ingest_request = opal_security.AgentActivityIngestRequest() # AgentActivityIngestRequest | 
    x_opal_actor = 'x_opal_actor_example' # str | The identity the reporting client claims this activity belongs to - an email or an Anthropic user id. **Unverified**: a Claude Code hook payload contains no user identity, so this has to be injected by whoever deploys the hook (via the http handler's `headers` map and `allowedEnvVars` interpolation), and whoever controls the machine controls the header. Used only when the API key itself does not identify a developer. When the email belongs to a person in the organization, that person is recorded as who the activity was reported for (always as a claim), and the activity is attributed to the one Claude agent they own, if they own exactly one. The API key's own email is never treated this way: a key belongs to whoever created it, which with a shared key is not who is at the keyboard. Omitting it is valid. When an event's `opal_reported` object carries other emails, Opal also tries them, in the order `configured_email`, `claude_account_email`, `git_email`, after this header and skipping any that repeat it. The first one that resolves to an agent wins. (optional)
    x_opal_host = 'x_opal_host_example' # str | The name of the machine that sent this request, as that machine reports it (`hostname -s`). **Unverified**: two machines can share a name, and whoever controls the machine controls the header. Stored with each event, so a reader can tell which machine reported it. When an event's own `opal_reported.hostname` names a different machine, this header wins and the body's value is kept beside it. Omitting it is valid. (optional)
    x_opal_content = 'x_opal_content_example' # str | `1` when the sender collects conversation content: the prompt of a `UserPromptSubmit` event, the `tool_response` of a `PostToolUse` event and the `last_assistant_message` of a `Stop` or `SubagentStop` event. Without it (or an event's own `opal_content`) those fields are read and discarded, as before. An `http` hook sets it in its `headers` map, because it cannot change the payload. Opal stores the content only when the organization stores content as well. (optional)

    try:
        # Report agent activity
        api_response = api_instance.report_agent_activity(agent_activity_ingest_request, x_opal_actor=x_opal_actor, x_opal_host=x_opal_host, x_opal_content=x_opal_content)
        print("The response of AgentActivityApi->report_agent_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentActivityApi->report_agent_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_activity_ingest_request** | [**AgentActivityIngestRequest**](AgentActivityIngestRequest.md)|  | 
 **x_opal_actor** | **str**| The identity the reporting client claims this activity belongs to - an email or an Anthropic user id. **Unverified**: a Claude Code hook payload contains no user identity, so this has to be injected by whoever deploys the hook (via the http handler&#39;s &#x60;headers&#x60; map and &#x60;allowedEnvVars&#x60; interpolation), and whoever controls the machine controls the header. Used only when the API key itself does not identify a developer. When the email belongs to a person in the organization, that person is recorded as who the activity was reported for (always as a claim), and the activity is attributed to the one Claude agent they own, if they own exactly one. The API key&#39;s own email is never treated this way: a key belongs to whoever created it, which with a shared key is not who is at the keyboard. Omitting it is valid. When an event&#39;s &#x60;opal_reported&#x60; object carries other emails, Opal also tries them, in the order &#x60;configured_email&#x60;, &#x60;claude_account_email&#x60;, &#x60;git_email&#x60;, after this header and skipping any that repeat it. The first one that resolves to an agent wins. | [optional] 
 **x_opal_host** | **str**| The name of the machine that sent this request, as that machine reports it (&#x60;hostname -s&#x60;). **Unverified**: two machines can share a name, and whoever controls the machine controls the header. Stored with each event, so a reader can tell which machine reported it. When an event&#39;s own &#x60;opal_reported.hostname&#x60; names a different machine, this header wins and the body&#39;s value is kept beside it. Omitting it is valid. | [optional] 
 **x_opal_content** | **str**| &#x60;1&#x60; when the sender collects conversation content: the prompt of a &#x60;UserPromptSubmit&#x60; event, the &#x60;tool_response&#x60; of a &#x60;PostToolUse&#x60; event and the &#x60;last_assistant_message&#x60; of a &#x60;Stop&#x60; or &#x60;SubagentStop&#x60; event. Without it (or an event&#39;s own &#x60;opal_content&#x60;) those fields are read and discarded, as before. An &#x60;http&#x60; hook sets it in its &#x60;headers&#x60; map, because it cannot change the payload. Opal stores the content only when the organization stores content as well. | [optional] 

### Return type

[**AgentActivityIngestResult**](AgentActivityIngestResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A per-batch accounting of what was accepted, stored, and attributed. An organization that has agent activity turned off gets a 200 with an empty body for every body shape, so a sender does not keep the events and try again. |  -  |
**400** | The body was unparseable, empty, or carried more events than one request may. |  -  |
**413** | The request body exceeded the maximum accepted size. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_mcp_config**
> McpConfigReportResult report_mcp_config(mcp_config_report, x_opal_actor=x_opal_actor, x_opal_host=x_opal_host)

Report MCP server configuration

**Prototype.** Reports the MCP servers configured in Claude Code on one developer's machine, as the Opal hook kit read them: user-level and per-project servers in `~/.claude.json`, a project's `.mcp.json`, `managed-mcp.json`, and servers a plugin provides when they can be found.

For each server the kit sends its name, the scope it was configured in, its transport, and either its URL (`http`, `sse`) or a hash of its command's shape (`stdio`). It never sends environment values, headers or command arguments, which can hold secrets. Opal adds each server to the organization's MCP server registry and records that this person has it configured. Nothing on the machine is changed.

Like `/agent-activity`, this is **telemetry from cooperating machines**: the identity and the list are what the machine says. The bearer token establishes the organization and nothing finer.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.mcp_config_report import McpConfigReport
from opal_security.models.mcp_config_report_result import McpConfigReportResult
from opal_security.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal_security.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal_security.AgentActivityApi(api_client)
    mcp_config_report = opal_security.McpConfigReport() # McpConfigReport | 
    x_opal_actor = 'x_opal_actor_example' # str | The identity the reporting client claims - an email, or an operating-system user name. **Unverified**, used the same way as on `/agent-activity`. (optional)
    x_opal_host = 'x_opal_host_example' # str | The name of the machine that sent the report, as that machine reports it (`hostname -s`). **Unverified.** A server this machine listed before and this report leaves out is marked removed for the reporting person, unless another of their machines still lists it. Omitting it is valid: the reports without one count as one machine. (optional)

    try:
        # Report MCP server configuration
        api_response = api_instance.report_mcp_config(mcp_config_report, x_opal_actor=x_opal_actor, x_opal_host=x_opal_host)
        print("The response of AgentActivityApi->report_mcp_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentActivityApi->report_mcp_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_config_report** | [**McpConfigReport**](McpConfigReport.md)|  | 
 **x_opal_actor** | **str**| The identity the reporting client claims - an email, or an operating-system user name. **Unverified**, used the same way as on &#x60;/agent-activity&#x60;. | [optional] 
 **x_opal_host** | **str**| The name of the machine that sent the report, as that machine reports it (&#x60;hostname -s&#x60;). **Unverified.** A server this machine listed before and this report leaves out is marked removed for the reporting person, unless another of their machines still lists it. Omitting it is valid: the reports without one count as one machine. | [optional] 

### Return type

[**McpConfigReportResult**](McpConfigReportResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | How many servers were read and recorded. |  -  |
**400** | The body was unparseable, or carried more servers than one report may. |  -  |
**403** | The MCP server registry is not enabled for this organization. |  -  |
**413** | The request body exceeded the maximum accepted size. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_agent_kill_switch**
> AgentKillSwitch set_agent_kill_switch(set_agent_kill_switch_request)

Set the agent kill switch

**Prototype (AG-297).** Turns the org-level agent kill switch on or off. Admin only.

While it is on, Opal answers every `PreToolUse` hook POST to `/agent-activity` with a `deny` decision, so a cooperating Claude Code client stops running tools.

**It is not a security boundary, and it fails open.** It reaches only clients that are configured to POST to `/agent-activity` and that honour the answer; a client on a non-default base URL, an older build, or with no hook deployed is unaffected. If Opal is unreachable or slow the tool call proceeds, because Claude Code treats a failed `PreToolUse` hook as a non-blocking error by design.

Activation is always time-bound: `duration_minutes` is capped, and an activation that reaches `expires_at` stops denying on its own.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.agent_kill_switch import AgentKillSwitch
from opal_security.models.set_agent_kill_switch_request import SetAgentKillSwitchRequest
from opal_security.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal_security.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal_security.AgentActivityApi(api_client)
    set_agent_kill_switch_request = opal_security.SetAgentKillSwitchRequest() # SetAgentKillSwitchRequest | 

    try:
        # Set the agent kill switch
        api_response = api_instance.set_agent_kill_switch(set_agent_kill_switch_request)
        print("The response of AgentActivityApi->set_agent_kill_switch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentActivityApi->set_agent_kill_switch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_agent_kill_switch_request** | [**SetAgentKillSwitchRequest**](SetAgentKillSwitchRequest.md)|  | 

### Return type

[**AgentKillSwitch**](AgentKillSwitch.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the kill switch after the change. |  -  |
**400** | The body was unparseable, or &#x60;duration_minutes&#x60; was out of range. |  -  |
**403** | The caller is not an admin, or the agent kill switch is not enabled for this organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

