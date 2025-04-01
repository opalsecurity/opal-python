# opal_security.RequestsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_request**](RequestsApi.md#create_request) | **POST** /requests | 
[**get_requests**](RequestsApi.md#get_requests) | **GET** /requests | 


# **create_request**
> CreateRequest200Response create_request(create_request_info)

Create an access request

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_request200_response import CreateRequest200Response
from opal_security.models.create_request_info import CreateRequestInfo
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
    api_instance = opal_security.RequestsApi(api_client)
    create_request_info = opal_security.CreateRequestInfo() # CreateRequestInfo | Resources to be updated

    try:
        api_response = api_instance.create_request(create_request_info)
        print("The response of RequestsApi->create_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->create_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request_info** | [**CreateRequestInfo**](CreateRequestInfo.md)| Resources to be updated | 

### Return type

[**CreateRequest200Response**](CreateRequest200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resulting request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requests**
> RequestList get_requests(cursor=cursor, page_size=page_size, show_pending_only=show_pending_only)

Returns a list of requests for your organization that is visible by the admin.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.request_list import RequestList
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
    api_instance = opal_security.RequestsApi(api_client)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)
    show_pending_only = True # bool | Boolean toggle for if it should only show pending requests. (optional)

    try:
        api_response = api_instance.get_requests(cursor=cursor, page_size=page_size, show_pending_only=show_pending_only)
        print("The response of RequestsApi->get_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 
 **show_pending_only** | **bool**| Boolean toggle for if it should only show pending requests. | [optional] 

### Return type

[**RequestList**](RequestList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requests. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

