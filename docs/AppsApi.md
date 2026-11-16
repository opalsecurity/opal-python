# opal_security.AppsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](AppsApi.md#create_app) | **POST** /apps | Create app
[**delete_app**](AppsApi.md#delete_app) | **DELETE** /apps/{app_id} | Delete app
[**get_app**](AppsApi.md#get_app) | **GET** /apps/{app_id} | Get app by ID
[**get_app_visibility**](AppsApi.md#get_app_visibility) | **GET** /apps/{app_id}/visibility | Get app visibility
[**get_apps**](AppsApi.md#get_apps) | **GET** /apps | Get apps
[**get_sync_errors**](AppsApi.md#get_sync_errors) | **GET** /sync_errors | 
[**set_app_visibility**](AppsApi.md#set_app_visibility) | **PUT** /apps/{app_id}/visibility | Set app visibility
[**update_app**](AppsApi.md#update_app) | **PUT** /apps/{app_id} | Update app


# **create_app**
> App create_app(create_app_info)

Create app

Creates an `App` in Opal. Currently supports only Push-only apps (`CUSTOM`)
and Custom Connector apps (`CUSTOM_CONNECTOR`).

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.app import App
from opal_security.models.create_app_info import CreateAppInfo
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
    create_app_info = opal_security.CreateAppInfo() # CreateAppInfo | 

    try:
        # Create app
        api_response = api_instance.create_app(create_app_info)
        print("The response of AppsApi->create_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->create_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_app_info** | [**CreateAppInfo**](CreateAppInfo.md)|  | 

### Return type

[**App**](App.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The app that was created. |  -  |
**400** | Invalid request body — for example, &#x60;visibility_group_ids&#x60; is non-empty while &#x60;visibility&#x60; is &#x60;GLOBAL&#x60;, an unsupported &#x60;app_type&#x60;, or a missing/invalid &#x60;custom_connector&#x60; configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app**
> delete_app(app_id)

Delete app

Deletes an `App`. Currently supports only Push-only apps (`CUSTOM`) and
Custom Connector apps (`CUSTOM_CONNECTOR`). Matches the UI: soft-deletes
the app and cleans up its resources, groups, and users.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
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
    app_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the app.

    try:
        # Delete app
        api_instance.delete_app(app_id)
    except Exception as e:
        print("Exception when calling AppsApi->delete_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **UUID**| The ID of the app. | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The app was successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> App get_app(app_id)

Get app by ID

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
    app_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the app.

    try:
        # Get app by ID
        api_response = api_instance.get_app(app_id)
        print("The response of AppsApi->get_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **UUID**| The ID of the app. | 

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

# **get_app_visibility**
> AppVisibilityInfo get_app_visibility(app_id)

Get app visibility

Returns the visibility of this app.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.app_visibility_info import AppVisibilityInfo
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
    app_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the app.

    try:
        # Get app visibility
        api_response = api_instance.get_app_visibility(app_id)
        print("The response of AppsApi->get_app_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **UUID**| The ID of the app. | 

### Return type

[**AppVisibilityInfo**](AppVisibilityInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The visibility info of this app. |  -  |
**400** | This endpoint only supports apps whose type is managed via &#x60;POST /v1/apps&#x60; and &#x60;PATCH /v1/apps/{id}&#x60; (&#x60;CUSTOM&#x60;, &#x60;OPAL_*&#x60;, and similar). Discovery-sourced app types (for example &#x60;AWS_SSO&#x60;) are rejected with 400. |  -  |
**403** | The caller is not authorized to view this app&#39;s visibility. |  -  |
**404** | The app was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apps**
> AppsList get_apps(app_type_filter=app_type_filter, owner_filter=owner_filter)

Get apps

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
    owner_filter = UUID('29827fb8-f2dd-4e80-9576-28e31e9934ac') # UUID | An owner ID to filter by. (optional)

    try:
        # Get apps
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
 **owner_filter** | **UUID**| An owner ID to filter by. | [optional] 

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
    app_id = UUID('29827fb8-f2dd-4e80-9576-28e31e9934ac') # UUID | The ID of the app to list sync errors for. (optional)
    resource_id = UUID('4baf8423-db0a-4037-a4cf-f79c60cb67a5') # UUID | The ID of the resource to list sync errors for. (optional)
    group_id = UUID('9546209c-42c2-4801-96d7-9ec42df0f59c') # UUID | The ID of the group to list sync errors for. (optional)

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
 **app_id** | **UUID**| The ID of the app to list sync errors for. | [optional] 
 **resource_id** | **UUID**| The ID of the resource to list sync errors for. | [optional] 
 **group_id** | **UUID**| The ID of the group to list sync errors for. | [optional] 

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

# **set_app_visibility**
> AppVisibilityInfo set_app_visibility(app_id, app_visibility_info)

Set app visibility

Sets the visibility of this app. Preferred over setting
`visibility` / `visibility_group_ids` / `import_visibility` inline on
`POST /apps` or `PATCH /apps/{app_id}` for drift-sensitive callers
(Terraform, GitOps). Semantics are a replace, not a merge:
`visibility_group_ids` is written to exactly what the request sends
(an omitted or empty array clears all groups), and `import_visibility`
is updated only when present.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.app_visibility_info import AppVisibilityInfo
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
    app_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the app.
    app_visibility_info = opal_security.AppVisibilityInfo() # AppVisibilityInfo | 

    try:
        # Set app visibility
        api_response = api_instance.set_app_visibility(app_id, app_visibility_info)
        print("The response of AppsApi->set_app_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->set_app_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **UUID**| The ID of the app. | 
 **app_visibility_info** | [**AppVisibilityInfo**](AppVisibilityInfo.md)|  | 

### Return type

[**AppVisibilityInfo**](AppVisibilityInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated visibility info of this app. |  -  |
**400** | Invalid request body or app state. Returned for any of: a malformed JSON body, an unknown field, an invalid &#x60;visibility&#x60; or &#x60;import_visibility&#x60; enum value, a &#x60;visibility_group_ids&#x60; entry that does not resolve to a group in the caller&#39;s org, a &#x60;visibility_group_ids&#x60; value that is non-empty while the effective &#x60;visibility&#x60; is &#x60;GLOBAL&#x60; (either sent on this request or already stored on the app), or an app whose type does not support visibility writes (only &#x60;CUSTOM&#x60; and &#x60;CUSTOM_CONNECTOR&#x60; do).  |  -  |
**403** | The caller is not authorized to edit this app&#39;s visibility. |  -  |
**404** | The app was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> App update_app(app_id, update_app_info)

Update app

Updates an `App`. Currently supports only Push-only apps (`CUSTOM`) and
Custom Connector apps (`CUSTOM_CONNECTOR`).

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.app import App
from opal_security.models.update_app_info import UpdateAppInfo
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
    app_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the app.
    update_app_info = opal_security.UpdateAppInfo() # UpdateAppInfo | 

    try:
        # Update app
        api_response = api_instance.update_app(app_id, update_app_info)
        print("The response of AppsApi->update_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->update_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **UUID**| The ID of the app. | 
 **update_app_info** | [**UpdateAppInfo**](UpdateAppInfo.md)|  | 

### Return type

[**App**](App.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated app. |  -  |
**400** | Invalid request body — for example, &#x60;visibility_group_ids&#x60; is non-empty while the effective visibility is &#x60;GLOBAL&#x60; (either explicitly on this request or already stored on the app), or a &#x60;custom_connector&#x60; field is invalid for this app type.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

