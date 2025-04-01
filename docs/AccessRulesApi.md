# opal_security.AccessRulesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_rule**](AccessRulesApi.md#get_access_rule) | **GET** /access-rules/{access_rule_id} | 
[**update_access_rule**](AccessRulesApi.md#update_access_rule) | **PUT** /access-rules/{access_rule_id} | 


# **get_access_rule**
> AccessRuleCondition get_access_rule(access_rule_id)

Returns a list of access rule config given the group_id of the access rule.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.access_rule_condition import AccessRuleCondition
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
    api_instance = opal_security.AccessRulesApi(api_client)
    access_rule_id = '1b978423-db0a-4037-a4cf-f79c60cb67b3' # str | The access rule ID (group ID) of the access rule.

    try:
        api_response = api_instance.get_access_rule(access_rule_id)
        print("The response of AccessRulesApi->get_access_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRulesApi->get_access_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_rule_id** | **str**| The access rule ID (group ID) of the access rule. | 

### Return type

[**AccessRuleCondition**](AccessRuleCondition.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access rules for the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_rule**
> AccessRuleCondition update_access_rule(access_rule_id, access_rule_condition)

Updates the access rule config for the given group_id.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.access_rule_condition import AccessRuleCondition
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
    api_instance = opal_security.AccessRulesApi(api_client)
    access_rule_id = '1b978423-db0a-4037-a4cf-f79c60cb67b3' # str | The access rule ID (group ID) of the access rule.
    access_rule_condition = opal_security.AccessRuleCondition() # AccessRuleCondition | 

    try:
        api_response = api_instance.update_access_rule(access_rule_id, access_rule_condition)
        print("The response of AccessRulesApi->update_access_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRulesApi->update_access_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_rule_id** | **str**| The access rule ID (group ID) of the access rule. | 
 **access_rule_condition** | [**AccessRuleCondition**](AccessRuleCondition.md)|  | 

### Return type

[**AccessRuleCondition**](AccessRuleCondition.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated access rule config for the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

