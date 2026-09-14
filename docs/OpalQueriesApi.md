# opal_security.OpalQueriesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_opal_query**](OpalQueriesApi.md#run_opal_query) | **POST** /queries/run | Run an ad-hoc OpalQuery


# **run_opal_query**
> OpalQueryResults run_opal_query(run_opal_query_request)

Run an ad-hoc OpalQuery

Executes an ad-hoc OpalQuery and returns paginated results. Two query types are supported: a **Node** query filters and returns entities (users, resources, or groups); an **Access Path** query returns the access edges between principals and their entitlements. Set `type` to `NODE` or `ACCESS_PATH` in the request body to select the query type.

This endpoint is available to OpalQuery beta participants. To request access, contact Opal support.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.opal_query_results import OpalQueryResults
from opal_security.models.run_opal_query_request import RunOpalQueryRequest
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
    api_instance = opal_security.OpalQueriesApi(api_client)
    run_opal_query_request = opal_security.RunOpalQueryRequest() # RunOpalQueryRequest | 

    try:
        # Run an ad-hoc OpalQuery
        api_response = api_instance.run_opal_query(run_opal_query_request)
        print("The response of OpalQueriesApi->run_opal_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpalQueriesApi->run_opal_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_opal_query_request** | [**RunOpalQueryRequest**](RunOpalQueryRequest.md)|  | 

### Return type

[**OpalQueryResults**](OpalQueryResults.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The results of the OpalQuery. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

