# opal_security.SessionsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessions**](SessionsApi.md#sessions) | **GET** /sessions | 


# **sessions**
> SessionsList sessions(resource_id, user_id=user_id)

Returns a list of `Session` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.sessions_list import SessionsList
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
    api_instance = opal_security.SessionsApi(api_client)
    resource_id = '1b978423-db0a-4037-a4cf-f79c60cb67b3' # str | The ID of the resource.
    user_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the user you wish to query sessions for. (optional)

    try:
        api_response = api_instance.sessions(resource_id, user_id=user_id)
        print("The response of SessionsApi->sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
 **user_id** | **str**| The ID of the user you wish to query sessions for. | [optional] 

### Return type

[**SessionsList**](SessionsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sessions associated with a resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

