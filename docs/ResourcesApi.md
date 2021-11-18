# opal.ResourcesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_user_access_status_retrieve**](ResourcesApi.md#resource_user_access_status_retrieve) | **GET** /resource-user-access-status/{resource_id}/{user_id} | 
[**resource_users**](ResourcesApi.md#resource_users) | **GET** /resource-users | 


# **resource_user_access_status_retrieve**
> ResourceUserAccessStatus resource_user_access_status_retrieve(resource_id, user_id)



Get user's access status to a resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import resources_api
from opal.model.resource_user_access_status import ResourceUserAccessStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with opal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)
    resource_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the resource.
    user_id = "29827fb8-f2dd-4e80-9576-28e31e9934ac" # str | The ID of the user.
    access_level_remote_id = "arn:aws:iam::590304332660:role/AdministratorAccess" # str | The remote ID of the access level that you wish to query for the resource. If omitted, the default access level remote ID value (empty string) is used. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.resource_user_access_status_retrieve(resource_id, user_id)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->resource_user_access_status_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.resource_user_access_status_retrieve(resource_id, user_id, access_level_remote_id=access_level_remote_id, cursor=cursor, page_size=page_size)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->resource_user_access_status_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. |
 **user_id** | **str**| The ID of the user. |
 **access_level_remote_id** | **str**| The remote ID of the access level that you wish to query for the resource. If omitted, the default access level remote ID value (empty string) is used. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**ResourceUserAccessStatus**](ResourceUserAccessStatus.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access status reflecting the user&#39;s access to the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_users**
> PaginatedResourceUserList resource_users(resource_id)



Returns a list of `ResourceUser` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import resources_api
from opal.model.paginated_resource_user_list import PaginatedResourceUserList
from pprint import pprint
# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with opal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)
    resource_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the resource.
    access_level_remote_id = "arn:aws:iam::590304332660:role/AdministratorAccess" # str | The remote ID of the access level that you wish to query for the resource. If omitted, the default access level remote ID value (empty string) is used. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.resource_users(resource_id)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->resource_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.resource_users(resource_id, access_level_remote_id=access_level_remote_id, cursor=cursor, page_size=page_size)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->resource_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. |
 **access_level_remote_id** | **str**| The remote ID of the access level that you wish to query for the resource. If omitted, the default access level remote ID value (empty string) is used. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**PaginatedResourceUserList**](PaginatedResourceUserList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page worth of users with access to this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

