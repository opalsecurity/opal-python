# opal_security.AppsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app**](AppsApi.md#get_app) | **GET** /apps/{app_id} | 
[**get_apps**](AppsApi.md#get_apps) | **GET** /apps | 
[**get_sync_errors**](AppsApi.md#get_sync_errors) | **GET** /sync_errors | 


# **get_app**
> App get_app(app_id)

Returns an `App` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.app import App
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
    api_instance = opal_security.AppsApi(api_client)
    app_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the app.

    try:
        api_response = api_instance.get_app(app_id)
        print("The response of AppsApi->get_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The ID of the app. | 

### Return type

[**App**](App.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested &#x60;App&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apps**
> AppsList get_apps(app_type_filter=app_type_filter, owner_filter=owner_filter)

Returns a list of `App` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.app_type_enum import AppTypeEnum
from opal_security.models.apps_list import AppsList
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
    api_instance = opal_security.AppsApi(api_client)
    app_type_filter = [opal_security.AppTypeEnum()] # List[AppTypeEnum] | A list of app types to filter by. (optional)
    owner_filter = '29827fb8-f2dd-4e80-9576-28e31e9934ac' # str | An owner ID to filter by. (optional)

    try:
        api_response = api_instance.get_apps(app_type_filter=app_type_filter, owner_filter=owner_filter)
        print("The response of AppsApi->get_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_type_filter** | [**List[AppTypeEnum]**](AppTypeEnum.md)| A list of app types to filter by. | [optional] 
 **owner_filter** | **str**| An owner ID to filter by. | [optional] 

### Return type

[**AppsList**](AppsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of apps for your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_errors**
> List[SyncErrorList] get_sync_errors(app_id=app_id, resource_id=resource_id, group_id=group_id)

Returns a list of recent sync errors that have occurred since the last successful sync.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.sync_error_list import SyncErrorList
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
    api_instance = opal_security.AppsApi(api_client)
    app_id = '29827fb8-f2dd-4e80-9576-28e31e9934ac' # str | The ID of the app to list sync errors for. (optional)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource to list sync errors for. (optional)
    group_id = '9546209c-42c2-4801-96d7-9ec42df0f59c' # str | The ID of the group to list sync errors for. (optional)

    try:
        api_response = api_instance.get_sync_errors(app_id=app_id, resource_id=resource_id, group_id=group_id)
        print("The response of AppsApi->get_sync_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_sync_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The ID of the app to list sync errors for. | [optional] 
 **resource_id** | **str**| The ID of the resource to list sync errors for. | [optional] 
 **group_id** | **str**| The ID of the group to list sync errors for. | [optional] 

### Return type

[**List[SyncErrorList]**](SyncErrorList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sync errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

