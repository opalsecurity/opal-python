# opal_security.UarsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_uar**](UarsApi.md#create_uar) | **POST** /uar | 
[**get_uar**](UarsApi.md#get_uar) | **GET** /uar/{uar_id} | 
[**get_uars**](UarsApi.md#get_uars) | **GET** /uars | 


# **create_uar**
> UAR create_uar(create_uar_info)

Starts a User Access Review.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_uar_info import CreateUARInfo
from opal_security.models.uar import UAR
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
    api_instance = opal_security.UarsApi(api_client)
    create_uar_info = opal_security.CreateUARInfo() # CreateUARInfo | The settings of the UAR.

    try:
        api_response = api_instance.create_uar(create_uar_info)
        print("The response of UarsApi->create_uar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UarsApi->create_uar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_uar_info** | [**CreateUARInfo**](CreateUARInfo.md)| The settings of the UAR. | 

### Return type

[**UAR**](UAR.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The UAR that was started. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uar**
> UAR get_uar(uar_id)

Retrieves a specific UAR.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.uar import UAR
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
    api_instance = opal_security.UarsApi(api_client)
    uar_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the UAR.

    try:
        api_response = api_instance.get_uar(uar_id)
        print("The response of UarsApi->get_uar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UarsApi->get_uar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uar_id** | **str**| The ID of the UAR. | 

### Return type

[**UAR**](UAR.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The UAR that was requested. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uars**
> PaginatedUARsList get_uars(cursor=cursor, page_size=page_size)

Returns a list of `UAR` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_uars_list import PaginatedUARsList
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
    api_instance = opal_security.UarsApi(api_client)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

    try:
        api_response = api_instance.get_uars(cursor=cursor, page_size=page_size)
        print("The response of UarsApi->get_uars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UarsApi->get_uars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 

### Return type

[**PaginatedUARsList**](PaginatedUARsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of UARs for your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

