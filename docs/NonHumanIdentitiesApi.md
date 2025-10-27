# opal_security.NonHumanIdentitiesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nhis**](NonHumanIdentitiesApi.md#get_nhis) | **GET** /non-human-identities | 


# **get_nhis**
> PaginatedResourcesList get_nhis(cursor=cursor, page_size=page_size)

Returns a list of non-human identities for your organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_resources_list import PaginatedResourcesList
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
    api_instance = opal_security.NonHumanIdentitiesApi(api_client)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

    try:
        api_response = api_instance.get_nhis(cursor=cursor, page_size=page_size)
        print("The response of NonHumanIdentitiesApi->get_nhis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonHumanIdentitiesApi->get_nhis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 

### Return type

[**PaginatedResourcesList**](PaginatedResourcesList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page worth non-human identities in your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

