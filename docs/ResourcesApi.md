# opal.ResourcesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_resource**](ResourcesApi.md#delete_resource) | **DELETE** /resources/{resource_id} | 
[**get_resource_message_channels**](ResourcesApi.md#get_resource_message_channels) | **GET** /resources/{resource_id}/message-channels | 
[**get_resource_reviewers**](ResourcesApi.md#get_resource_reviewers) | **GET** /resources/{resource_id}/reviewers | 
[**get_resource_tags**](ResourcesApi.md#get_resource_tags) | **GET** /resources/{resource_id}/tags | 
[**get_resources**](ResourcesApi.md#get_resources) | **GET** /resources | 
[**resource_user_access_status_retrieve**](ResourcesApi.md#resource_user_access_status_retrieve) | **GET** /resource-user-access-status/{resource_id}/{user_id} | 
[**resource_users**](ResourcesApi.md#resource_users) | **GET** /resource-users | 
[**set_resource_message_channels**](ResourcesApi.md#set_resource_message_channels) | **PUT** /resources/{resource_id}/message-channels | 
[**set_resource_reviewers**](ResourcesApi.md#set_resource_reviewers) | **PUT** /resources/{resource_id}/reviewers | 
[**update_resources**](ResourcesApi.md#update_resources) | **PUT** /resources | 


# **delete_resource**
> delete_resource(resource_id)



Deletes a resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import resources_api
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
    resource_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the resource.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_resource(resource_id)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->delete_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. |

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
**200** | The resource was successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_message_channels**
> MessageChannelList get_resource_message_channels(resource_id)



Gets the list of message channels attached to a resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import resources_api
from opal.model.message_channel_list import MessageChannelList
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
    resource_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the resource.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_resource_message_channels(resource_id)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->get_resource_message_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. |

### Return type

[**MessageChannelList**](MessageChannelList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The message channels attached to the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_reviewers**
> [str] get_resource_reviewers(resource_id)



Gets the list of team/user IDs of the reviewers for a resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import resources_api
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
    resource_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the resource.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_resource_reviewers(resource_id)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->get_resource_reviewers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. |

### Return type

**[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The IDs of teams that are reviewers for this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_tags**
> TagsList get_resource_tags(resource_id)



Returns all tags applied to the resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import resources_api
from opal.model.tags_list import TagsList
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
    resource_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the resource whose tags to return.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_resource_tags(resource_id)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->get_resource_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource whose tags to return. |

### Return type

[**TagsList**](TagsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tags applied to the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> PaginatedResourcesList get_resources()



Returns a list of resources for your organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import resources_api
from opal.model.resource_type_enum import ResourceTypeEnum
from opal.model.paginated_resources_list import PaginatedResourcesList
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
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)
    resource_type_filter = ResourceTypeEnum("AWS_IAM_ROLE") # ResourceTypeEnum | The resource type to filter by. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_resources(cursor=cursor, page_size=page_size, resource_type_filter=resource_type_filter)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->get_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional]
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional]
 **resource_type_filter** | **ResourceTypeEnum**| The resource type to filter by. | [optional]

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
**200** | One page worth resources associated with your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

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
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional]

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
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

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
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional]

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

# **set_resource_message_channels**
> [str] set_resource_message_channels(resource_id, message_channel_id_list)



Sets the list of message channels attached to a resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import resources_api
from opal.model.message_channel_id_list import MessageChannelIDList
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
    resource_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the resource.
    message_channel_id_list = MessageChannelIDList(
        message_channel_ids=[
            "message_channel_ids_example",
        ],
    ) # MessageChannelIDList | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_resource_message_channels(resource_id, message_channel_id_list)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->set_resource_message_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. |
 **message_channel_id_list** | [**MessageChannelIDList**](MessageChannelIDList.md)|  |

### Return type

**[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated message channel IDs for the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_resource_reviewers**
> [str] set_resource_reviewers(resource_id, reviewer_id_list)



Sets the list of reviewers for a resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import resources_api
from opal.model.reviewer_id_list import ReviewerIDList
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
    resource_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the resource.
    reviewer_id_list = ReviewerIDList(
        reviewer_ids=[
            "reviewer_ids_example",
        ],
    ) # ReviewerIDList | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_resource_reviewers(resource_id, reviewer_id_list)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->set_resource_reviewers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. |
 **reviewer_id_list** | [**ReviewerIDList**](ReviewerIDList.md)|  |

### Return type

**[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated IDs of teams that are reviewers for this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resources**
> UpdateResourceInfoList update_resources(update_resource_info_list)



Bulk updates a list of resources.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import resources_api
from opal.model.update_resource_info_list import UpdateResourceInfoList
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
    update_resource_info_list = UpdateResourceInfoList(
        resources=[
            UpdateResourceInfo(
                resource_id="f454d283-ca87-4a8a-bdbb-df212eca5353",
                name="my-mongo-db",
                description="This resource represents AWS IAM role "SupportUser".",
                owner_team_id="7c86c85d-0651-43e2-a748-d69d658418e8",
                visibility=VisibilityEnum("GLOBAL"),
                max_duration=120,
                require_manager_approval=False,
                require_support_ticket=False,
                folder_id="e27cb7b0-98e2-4555-9916-9e6d8ca6b079",
            ),
        ],
    ) # UpdateResourceInfoList | Resources to be updated

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_resources(update_resource_info_list)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling ResourcesApi->update_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_resource_info_list** | [**UpdateResourceInfoList**](UpdateResourceInfoList.md)| Resources to be updated |

### Return type

[**UpdateResourceInfoList**](UpdateResourceInfoList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resulting updated resource infos. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

