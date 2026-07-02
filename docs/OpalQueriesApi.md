# opal_security.OpalQueriesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_opal_query**](OpalQueriesApi.md#run_opal_query) | **POST** /queries/run | Run an ad-hoc OpalQuery


# **run_opal_query**
> OpalNodeQueryResults run_opal_query(body)

Run an ad-hoc OpalQuery

Runs an ad-hoc OpalQuery and returns the results. Currently supports NODE queries (users, resources, groups). This endpoint is only available to our OpalQuery beta group. Please contact Opal support if you'd like to be added to the beta.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.opal_node_query import OpalNodeQuery
from opal_security.models.opal_node_query_results import OpalNodeQueryResults
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
    body = opal_security.OpalNodeQuery() # OpalNodeQuery | 

    try:
        # Run an ad-hoc OpalQuery
        api_response = api_instance.run_opal_query(body)
        print("The response of OpalQueriesApi->run_opal_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpalQueriesApi->run_opal_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **OpalNodeQuery**|  | 

### Return type

[**OpalNodeQueryResults**](OpalNodeQueryResults.md)

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

