# opal_security.EventsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events**](EventsApi.md#events) | **GET** /events | 


# **events**
> PaginatedEventList events(start_date_filter=start_date_filter, end_date_filter=end_date_filter, actor_filter=actor_filter, object_filter=object_filter, event_type_filter=event_type_filter, api_token_filter=api_token_filter, cursor=cursor, page_size=page_size)

Returns a list of `Event` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_event_list import PaginatedEventList
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
    api_instance = opal_security.EventsApi(api_client)
    start_date_filter = '2021-11-01' # str | A start date filter for the events. (optional)
    end_date_filter = '2021-11-12' # str | An end date filter for the events. (optional)
    actor_filter = '29827fb8-f2dd-4e80-9576-28e31e9934ac' # str | An actor filter for the events. Supply the ID of the actor. (optional)
    object_filter = '29827fb8-f2dd-4e80-9576-28e31e9934ac' # str | An object filter for the events. Supply the ID of the object. (optional)
    event_type_filter = 'USER_MFA_RESET' # str | An event type filter for the events. (optional)
    api_token_filter = 'fullaccess:**************************M_g==' # str | An API filter for the events. Supply the name and preview of the API token. (optional)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

    try:
        api_response = api_instance.events(start_date_filter=start_date_filter, end_date_filter=end_date_filter, actor_filter=actor_filter, object_filter=object_filter, event_type_filter=event_type_filter, api_token_filter=api_token_filter, cursor=cursor, page_size=page_size)
        print("The response of EventsApi->events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_filter** | **str**| A start date filter for the events. | [optional] 
 **end_date_filter** | **str**| An end date filter for the events. | [optional] 
 **actor_filter** | **str**| An actor filter for the events. Supply the ID of the actor. | [optional] 
 **object_filter** | **str**| An object filter for the events. Supply the ID of the object. | [optional] 
 **event_type_filter** | **str**| An event type filter for the events. | [optional] 
 **api_token_filter** | **str**| An API filter for the events. Supply the name and preview of the API token. | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 

### Return type

[**PaginatedEventList**](PaginatedEventList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page worth of events with the appropriate filters applied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

