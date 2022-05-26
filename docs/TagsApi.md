# opal.TagsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_tag**](TagsApi.md#add_group_tag) | **POST** /tags/{tag_id}/groups/{group_id} | 
[**add_resource_tag**](TagsApi.md#add_resource_tag) | **POST** /tags/{tag_id}/resources/{resource_id} | 
[**add_user_tag**](TagsApi.md#add_user_tag) | **POST** /tags/{tag_id}/users/{user_id} | 
[**create_tag**](TagsApi.md#create_tag) | **POST** /tag | 
[**get_tag**](TagsApi.md#get_tag) | **GET** /tag | 
[**remove_group_tag**](TagsApi.md#remove_group_tag) | **DELETE** /tags/{tag_id}/groups/{group_id} | 
[**remove_resource_tag**](TagsApi.md#remove_resource_tag) | **DELETE** /tags/{tag_id}/resources/{resource_id} | 
[**remove_user_tag**](TagsApi.md#remove_user_tag) | **DELETE** /tags/{tag_id}/users/{user_id} | 


# **add_group_tag**
> add_group_tag(tag_id, group_id)



Applies a tag to a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    tag_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the tag to apply.
    group_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the group to apply the tag to.

    # example passing only required values which don't have defaults set
    try:
        api_instance.add_group_tag(tag_id, group_id)
    except opal.ApiException as e:
        print("Exception when calling TagsApi->add_group_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The ID of the tag to apply. |
 **group_id** | **str**| The ID of the group to apply the tag to. |

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
**200** | Tag applied to group successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_resource_tag**
> add_resource_tag(tag_id, resource_id)



Applies a tag to a resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    tag_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the tag to apply.
    resource_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the resource to apply the tag to.

    # example passing only required values which don't have defaults set
    try:
        api_instance.add_resource_tag(tag_id, resource_id)
    except opal.ApiException as e:
        print("Exception when calling TagsApi->add_resource_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The ID of the tag to apply. |
 **resource_id** | **str**| The ID of the resource to apply the tag to. |

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
**200** | Tag applied to resource successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_tag**
> add_user_tag(tag_id, user_id)



Applies a tag to a user.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    tag_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the tag to apply.
    user_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the user to apply the tag to.

    # example passing only required values which don't have defaults set
    try:
        api_instance.add_user_tag(tag_id, user_id)
    except opal.ApiException as e:
        print("Exception when calling TagsApi->add_user_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The ID of the tag to apply. |
 **user_id** | **str**| The ID of the user to apply the tag to. |

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
**200** | Tag applied to user successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag**
> Tag create_tag(tag_key, tag_value, tag_owner_team_id)



Creates a tag with the given key and value.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import tags_api
from opal.model.tag import Tag
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
    api_instance = tags_api.TagsApi(api_client)
    tag_key = "api-scope" # str | The key of the tag to create.
    tag_value = "production" # str | The value of the tag to create.
    tag_owner_team_id = "f92aa855-cea9-4814-b9d8-f2a60d3e4a06" # str | The ID of the team that owns the tag.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_tag(tag_key, tag_value, tag_owner_team_id)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling TagsApi->create_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_key** | **str**| The key of the tag to create. |
 **tag_value** | **str**| The value of the tag to create. |
 **tag_owner_team_id** | **str**| The ID of the team that owns the tag. |

### Return type

[**Tag**](Tag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag that was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> Tag get_tag(tag_key, tag_value)



Gets a tag with the given key and value.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import tags_api
from opal.model.tag import Tag
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
    api_instance = tags_api.TagsApi(api_client)
    tag_key = "api-scope" # str | The key of the tag to get.
    tag_value = "production" # str | The value of the tag to get.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tag(tag_key, tag_value)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling TagsApi->get_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_key** | **str**| The key of the tag to get. |
 **tag_value** | **str**| The value of the tag to get. |

### Return type

[**Tag**](Tag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag requested. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_tag**
> remove_group_tag(tag_id, group_id)



Removes a tag from a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    tag_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the tag to remove.
    group_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the group to remove the tag from.

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_group_tag(tag_id, group_id)
    except opal.ApiException as e:
        print("Exception when calling TagsApi->remove_group_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The ID of the tag to remove. |
 **group_id** | **str**| The ID of the group to remove the tag from. |

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
**200** | Tag removed from group successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_resource_tag**
> remove_resource_tag(tag_id, resource_id)



Removes a tag from a resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    tag_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the tag to remove.
    resource_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the resource to remove the tag from.

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_resource_tag(tag_id, resource_id)
    except opal.ApiException as e:
        print("Exception when calling TagsApi->remove_resource_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The ID of the tag to remove. |
 **resource_id** | **str**| The ID of the resource to remove the tag from. |

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
**200** | Tag removed from resource successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_tag**
> remove_user_tag(tag_id, user_id)



Removes a tag from a user.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    tag_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the tag to remove.
    user_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the user to remove the tag from.

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_user_tag(tag_id, user_id)
    except opal.ApiException as e:
        print("Exception when calling TagsApi->remove_user_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The ID of the tag to remove. |
 **user_id** | **str**| The ID of the user to remove the tag from. |

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
**200** | Tag removed from user successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

