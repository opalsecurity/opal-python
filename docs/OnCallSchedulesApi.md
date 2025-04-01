# opal_security.OnCallSchedulesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_on_call_schedule**](OnCallSchedulesApi.md#create_on_call_schedule) | **POST** /on-call-schedules | 
[**get_on_call_schedule**](OnCallSchedulesApi.md#get_on_call_schedule) | **GET** /on-call-schedules/{on_call_schedule_id} | 
[**get_on_call_schedules**](OnCallSchedulesApi.md#get_on_call_schedules) | **GET** /on-call-schedules | 


# **create_on_call_schedule**
> OnCallSchedule create_on_call_schedule(create_on_call_schedule_info)

Creates a `OnCallSchedule` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_on_call_schedule_info import CreateOnCallScheduleInfo
from opal_security.models.on_call_schedule import OnCallSchedule
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
    api_instance = opal_security.OnCallSchedulesApi(api_client)
    create_on_call_schedule_info = opal_security.CreateOnCallScheduleInfo() # CreateOnCallScheduleInfo | The `OnCallSchedule` object to be created.

    try:
        api_response = api_instance.create_on_call_schedule(create_on_call_schedule_info)
        print("The response of OnCallSchedulesApi->create_on_call_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnCallSchedulesApi->create_on_call_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_on_call_schedule_info** | [**CreateOnCallScheduleInfo**](CreateOnCallScheduleInfo.md)| The &#x60;OnCallSchedule&#x60; object to be created. | 

### Return type

[**OnCallSchedule**](OnCallSchedule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The on call schedule that was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_on_call_schedule**
> OnCallSchedule get_on_call_schedule(on_call_schedule_id)

Gets a `OnCallSchedule` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.on_call_schedule import OnCallSchedule
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
    api_instance = opal_security.OnCallSchedulesApi(api_client)
    on_call_schedule_id = '9546209c-42c2-4801-96d7-9ec42df0f59c' # str | The ID of the on_call_schedule.

    try:
        api_response = api_instance.get_on_call_schedule(on_call_schedule_id)
        print("The response of OnCallSchedulesApi->get_on_call_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnCallSchedulesApi->get_on_call_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_call_schedule_id** | **str**| The ID of the on_call_schedule. | 

### Return type

[**OnCallSchedule**](OnCallSchedule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested on call schedule. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_on_call_schedules**
> OnCallScheduleList get_on_call_schedules()

Returns a list of `OnCallSchedule` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.on_call_schedule_list import OnCallScheduleList
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
    api_instance = opal_security.OnCallSchedulesApi(api_client)

    try:
        api_response = api_instance.get_on_call_schedules()
        print("The response of OnCallSchedulesApi->get_on_call_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnCallSchedulesApi->get_on_call_schedules: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OnCallScheduleList**](OnCallScheduleList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of on call schedules for your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

