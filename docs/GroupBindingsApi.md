# opal_security.GroupBindingsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_binding**](GroupBindingsApi.md#create_group_binding) | **POST** /group-bindings | 
[**delete_group_binding**](GroupBindingsApi.md#delete_group_binding) | **DELETE** /group-bindings/{group_binding_id} | 
[**get_group_binding**](GroupBindingsApi.md#get_group_binding) | **GET** /group-bindings/{group_binding_id} | 
[**get_group_bindings**](GroupBindingsApi.md#get_group_bindings) | **GET** /group-bindings | 
[**update_group_bindings**](GroupBindingsApi.md#update_group_bindings) | **PUT** /group-bindings | 


# **create_group_binding**
> GroupBinding create_group_binding(create_group_binding_info)

Creates a group binding.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_group_binding_info import CreateGroupBindingInfo
from opal_security.models.group_binding import GroupBinding
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
    api_instance = opal_security.GroupBindingsApi(api_client)
    create_group_binding_info = opal_security.CreateGroupBindingInfo() # CreateGroupBindingInfo | 

    try:
        api_response = api_instance.create_group_binding(create_group_binding_info)
        print("The response of GroupBindingsApi->create_group_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupBindingsApi->create_group_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_binding_info** | [**CreateGroupBindingInfo**](CreateGroupBindingInfo.md)|  | 

### Return type

[**GroupBinding**](GroupBinding.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group binding just created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_binding**
> delete_group_binding(group_binding_id)

Deletes a group binding.

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
    api_instance = opal_security.GroupBindingsApi(api_client)
    group_binding_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group binding.

    try:
        api_instance.delete_group_binding(group_binding_id)
    except Exception as e:
        print("Exception when calling GroupBindingsApi->delete_group_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_binding_id** | **str**| The ID of the group binding. | 

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
**200** | The group binding was successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_binding**
> GroupBinding get_group_binding(group_binding_id)

Returns a `GroupBinding` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.group_binding import GroupBinding
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
    api_instance = opal_security.GroupBindingsApi(api_client)
    group_binding_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the group binding.

    try:
        api_response = api_instance.get_group_binding(group_binding_id)
        print("The response of GroupBindingsApi->get_group_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupBindingsApi->get_group_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_binding_id** | **str**| The ID of the group binding. | 

### Return type

[**GroupBinding**](GroupBinding.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested &#x60;GroupBinding&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_bindings**
> PaginatedGroupBindingsList get_group_bindings(cursor=cursor, page_size=page_size)

Returns a list of `GroupBinding` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_group_bindings_list import PaginatedGroupBindingsList
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
    api_instance = opal_security.GroupBindingsApi(api_client)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

    try:
        api_response = api_instance.get_group_bindings(cursor=cursor, page_size=page_size)
        print("The response of GroupBindingsApi->get_group_bindings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupBindingsApi->get_group_bindings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 

### Return type

[**PaginatedGroupBindingsList**](PaginatedGroupBindingsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page worth of group bindings for your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_bindings**
> update_group_bindings(update_group_binding_info_list)

Bulk updates a list of group bindings.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.update_group_binding_info_list import UpdateGroupBindingInfoList
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
    api_instance = opal_security.GroupBindingsApi(api_client)
    update_group_binding_info_list = opal_security.UpdateGroupBindingInfoList() # UpdateGroupBindingInfoList | Group bindings to be updated

    try:
        api_instance.update_group_bindings(update_group_binding_info_list)
    except Exception as e:
        print("Exception when calling GroupBindingsApi->update_group_bindings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_group_binding_info_list** | [**UpdateGroupBindingInfoList**](UpdateGroupBindingInfoList.md)| Group bindings to be updated | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group bindings were successfully updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

