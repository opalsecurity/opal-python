# opal_security.AgentActivityApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_kill_switch**](AgentActivityApi.md#get_agent_kill_switch) | **GET** /agent-kill-switch | Get the agent kill switch
[**report_agent_activity**](AgentActivityApi.md#report_agent_activity) | **POST** /agent-activity | Report agent activity
[**set_agent_kill_switch**](AgentActivityApi.md#set_agent_kill_switch) | **PUT** /agent-kill-switch | Set the agent kill switch


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
> AgentActivityIngestResult report_agent_activity(agent_activity_ingest_request, x_opal_actor=x_opal_actor)

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
    x_opal_actor = 'x_opal_actor_example' # str | The identity the reporting client claims this activity belongs to - an email or an Anthropic user id. **Unverified**: a Claude Code hook payload contains no user identity, so this has to be injected by whoever deploys the hook (via the http handler's `headers` map and `allowedEnvVars` interpolation), and whoever controls the machine controls the header. Used only when the API key itself does not identify a developer. Omitting it is valid. (optional)

    try:
        # Report agent activity
        api_response = api_instance.report_agent_activity(agent_activity_ingest_request, x_opal_actor=x_opal_actor)
        print("The response of AgentActivityApi->report_agent_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentActivityApi->report_agent_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_activity_ingest_request** | [**AgentActivityIngestRequest**](AgentActivityIngestRequest.md)|  | 
 **x_opal_actor** | **str**| The identity the reporting client claims this activity belongs to - an email or an Anthropic user id. **Unverified**: a Claude Code hook payload contains no user identity, so this has to be injected by whoever deploys the hook (via the http handler&#39;s &#x60;headers&#x60; map and &#x60;allowedEnvVars&#x60; interpolation), and whoever controls the machine controls the header. Used only when the API key itself does not identify a developer. Omitting it is valid. | [optional] 

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
**200** | A per-batch accounting of what was accepted, stored, and attributed. |  -  |
**400** | The body was unparseable, empty, or carried more events than one request may. |  -  |
**403** | Agent activity ingest is not enabled for this organization. |  -  |
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

