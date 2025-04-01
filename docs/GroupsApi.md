# opal_security.GroupsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_containing_group**](GroupsApi.md#add_group_containing_group) | **POST** /groups/{group_id}/containing-groups | 
[**add_group_resource**](GroupsApi.md#add_group_resource) | **POST** /groups/{group_id}/resources/{resource_id} | 
[**add_group_user**](GroupsApi.md#add_group_user) | **POST** /groups/{group_id}/users/{user_id} | 
[**create_group**](GroupsApi.md#create_group) | **POST** /groups | 
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /groups/{group_id} | 
[**delete_group_user**](GroupsApi.md#delete_group_user) | **DELETE** /groups/{group_id}/users/{user_id} | 
[**get_group**](GroupsApi.md#get_group) | **GET** /groups/{group_id} | 
[**get_group_containing_group**](GroupsApi.md#get_group_containing_group) | **GET** /groups/{group_id}/containing-groups/{containing_group_id} | 
[**get_group_containing_groups**](GroupsApi.md#get_group_containing_groups) | **GET** /groups/{group_id}/containing-groups | 
[**get_group_message_channels**](GroupsApi.md#get_group_message_channels) | **GET** /groups/{group_id}/message-channels | 
[**get_group_on_call_schedules**](GroupsApi.md#get_group_on_call_schedules) | **GET** /groups/{group_id}/on-call-schedules | 
[**get_group_resources**](GroupsApi.md#get_group_resources) | **GET** /groups/{group_id}/resources | 
[**get_group_reviewer_stages**](GroupsApi.md#get_group_reviewer_stages) | **GET** /groups/{group_id}/reviewer-stages | 
[**get_group_reviewers**](GroupsApi.md#get_group_reviewers) | **GET** /groups/{group_id}/reviewers | 
[**get_group_tags**](GroupsApi.md#get_group_tags) | **GET** /groups/{group_id}/tags | 
[**get_group_users**](GroupsApi.md#get_group_users) | **GET** /groups/{group_id}/users | 
[**get_group_visibility**](GroupsApi.md#get_group_visibility) | **GET** /groups/{group_id}/visibility | 
[**get_groups**](GroupsApi.md#get_groups) | **GET** /groups | 
[**remove_group_containing_group**](GroupsApi.md#remove_group_containing_group) | **DELETE** /groups/{group_id}/containing-groups/{containing_group_id} | 
[**set_group_message_channels**](GroupsApi.md#set_group_message_channels) | **PUT** /groups/{group_id}/message-channels | 
[**set_group_on_call_schedules**](GroupsApi.md#set_group_on_call_schedules) | **PUT** /groups/{group_id}/on-call-schedules | 
[**set_group_resources**](GroupsApi.md#set_group_resources) | **PUT** /groups/{group_id}/resources | 
[**set_group_reviewer_stages**](GroupsApi.md#set_group_reviewer_stages) | **PUT** /groups/{group_id}/reviewer-stages | 
[**set_group_reviewers**](GroupsApi.md#set_group_reviewers) | **PUT** /groups/{group_id}/reviewers | 
[**set_group_visibility**](GroupsApi.md#set_group_visibility) | **PUT** /groups/{group_id}/visibility | 
[**update_groups**](GroupsApi.md#update_groups) | **PUT** /groups | 


# **add_group_containing_group**
> GroupContainingGroup add_group_containing_group(group_id, group_containing_group)

Creates a new containing group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.group_containing_group import GroupContainingGroup
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    group_containing_group = opal_security.GroupContainingGroup() # GroupContainingGroup | 

    try:
        api_response = api_instance.add_group_containing_group(group_id, group_containing_group)
        print("The response of GroupsApi->add_group_containing_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_group_containing_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **group_containing_group** | [**GroupContainingGroup**](GroupContainingGroup.md)|  | 

### Return type

[**GroupContainingGroup**](GroupContainingGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created &#x60;GroupContainingGroup&#x60; object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_resource**
> GroupResource add_group_resource(group_id, resource_id, access_level_remote_id=access_level_remote_id, add_group_resource_request=add_group_resource_request)

Adds a resource to a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.add_group_resource_request import AddGroupResourceRequest
from opal_security.models.group_resource import GroupResource
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    access_level_remote_id = 'arn:aws:iam::590304332660:role/AdministratorAccess' # str | The remote ID of the access level to grant to this user. If omitted, the default access level remote ID value (empty string) is used. (optional)
    add_group_resource_request = opal_security.AddGroupResourceRequest() # AddGroupResourceRequest |  (optional)

    try:
        api_response = api_instance.add_group_resource(group_id, resource_id, access_level_remote_id=access_level_remote_id, add_group_resource_request=add_group_resource_request)
        print("The response of GroupsApi->add_group_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_group_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **resource_id** | **str**| The ID of the resource. | 
 **access_level_remote_id** | **str**| The remote ID of the access level to grant to this user. If omitted, the default access level remote ID value (empty string) is used. | [optional] 
 **add_group_resource_request** | [**AddGroupResourceRequest**](AddGroupResourceRequest.md)|  | [optional] 

### Return type

[**GroupResource**](GroupResource.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created &#x60;GroupResource&#x60; object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_user**
> GroupUser add_group_user(group_id, user_id, duration_minutes=duration_minutes, access_level_remote_id=access_level_remote_id, add_group_user_request=add_group_user_request)

Adds a user to this group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.add_group_user_request import AddGroupUserRequest
from opal_security.models.group_user import GroupUser
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    user_id = 'f92aa855-cea9-4814-b9d8-f2a60d3e4a06' # str | The ID of the user to add.
    duration_minutes = 60 # int | The duration for which the group can be accessed (in minutes). Use 0 to set to indefinite. (optional)
    access_level_remote_id = 'arn:aws:iam::590304332660:role/AdministratorAccess' # str | The remote ID of the access level to grant to this user. If omitted, the default access level remote ID value (empty string) is used. (optional)
    add_group_user_request = opal_security.AddGroupUserRequest() # AddGroupUserRequest |  (optional)

    try:
        api_response = api_instance.add_group_user(group_id, user_id, duration_minutes=duration_minutes, access_level_remote_id=access_level_remote_id, add_group_user_request=add_group_user_request)
        print("The response of GroupsApi->add_group_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_group_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **user_id** | **str**| The ID of the user to add. | 
 **duration_minutes** | **int**| The duration for which the group can be accessed (in minutes). Use 0 to set to indefinite. | [optional] 
 **access_level_remote_id** | **str**| The remote ID of the access level to grant to this user. If omitted, the default access level remote ID value (empty string) is used. | [optional] 
 **add_group_user_request** | [**AddGroupUserRequest**](AddGroupUserRequest.md)|  | [optional] 

### Return type

[**GroupUser**](GroupUser.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The GroupUser that was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> Group create_group(create_group_info)

Creates an Opal group or [imports a remote group](https://docs.opal.dev/reference/end-system-objects).

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_group_info import CreateGroupInfo
from opal_security.models.group import Group
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
    api_instance = opal_security.GroupsApi(api_client)
    create_group_info = opal_security.CreateGroupInfo() # CreateGroupInfo | 

    try:
        api_response = api_instance.create_group(create_group_info)
        print("The response of GroupsApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_info** | [**CreateGroupInfo**](CreateGroupInfo.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group just created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id)

Deletes a group.

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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.

    try:
        api_instance.delete_group(group_id)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 

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
**200** | The group was successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_user**
> delete_group_user(group_id, user_id)

Removes a user's access from this group.

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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    user_id = 'f92aa855-cea9-4814-b9d8-f2a60d3e4a06' # str | The ID of a user to remove from this group.

    try:
        api_instance.delete_group_user(group_id, user_id)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_group_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **user_id** | **str**| The ID of a user to remove from this group. | 

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
**200** | This user&#39;s access was successfully removed from this group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(group_id)

Returns a `Group` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.group import Group
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the group.

    try:
        api_response = api_instance.get_group(group_id)
        print("The response of GroupsApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 

### Return type

[**Group**](Group.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested &#x60;Group&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_containing_group**
> GroupContainingGroup get_group_containing_group(group_id, containing_group_id)

Gets a specific containing group for a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.group_containing_group import GroupContainingGroup
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    containing_group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the containing group.

    try:
        api_response = api_instance.get_group_containing_group(group_id, containing_group_id)
        print("The response of GroupsApi->get_group_containing_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_containing_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **containing_group_id** | **str**| The ID of the containing group. | 

### Return type

[**GroupContainingGroup**](GroupContainingGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created &#x60;GroupContainingGroup&#x60; object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_containing_groups**
> GroupContainingGroupList get_group_containing_groups(group_id)

Gets the list of groups that the group gives access to.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.group_containing_group_list import GroupContainingGroupList
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.

    try:
        api_response = api_instance.get_group_containing_groups(group_id)
        print("The response of GroupsApi->get_group_containing_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_containing_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 

### Return type

[**GroupContainingGroupList**](GroupContainingGroupList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resources that the group gives access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_message_channels**
> MessageChannelList get_group_message_channels(group_id)

Gets the list of audit and reviewer message channels attached to a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.message_channel_list import MessageChannelList
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.

    try:
        api_response = api_instance.get_group_message_channels(group_id)
        print("The response of GroupsApi->get_group_message_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_message_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 

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
**200** | The audit and reviewer message channels attached to the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_on_call_schedules**
> OnCallScheduleList get_group_on_call_schedules(group_id)

Gets the list of on call schedules attached to a group.

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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.

    try:
        api_response = api_instance.get_group_on_call_schedules(group_id)
        print("The response of GroupsApi->get_group_on_call_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_on_call_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 

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
**200** | The on call schedules attached to the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_resources**
> GroupResourceList get_group_resources(group_id)

Gets the list of resources that the group gives access to.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.group_resource_list import GroupResourceList
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.

    try:
        api_response = api_instance.get_group_resources(group_id)
        print("The response of GroupsApi->get_group_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 

### Return type

[**GroupResourceList**](GroupResourceList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resources that the group gives access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_reviewer_stages**
> List[ReviewerStage] get_group_reviewer_stages(group_id)

Gets the list of reviewer stages for a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.reviewer_stage import ReviewerStage
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.

    try:
        api_response = api_instance.get_group_reviewer_stages(group_id)
        print("The response of GroupsApi->get_group_reviewer_stages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_reviewer_stages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 

### Return type

[**List[ReviewerStage]**](ReviewerStage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reviewer stages for this group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_reviewers**
> List[str] get_group_reviewers(group_id)

Gets the list of owner IDs of the reviewers for a group.

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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.

    try:
        api_response = api_instance.get_group_reviewers(group_id)
        print("The response of GroupsApi->get_group_reviewers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_reviewers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The IDs of owners that are reviewers for this group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_tags**
> TagsList get_group_tags(group_id)

Returns all tags applied to the group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.tags_list import TagsList
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '1b978423-db0a-4037-a4cf-f79c60cb67b3' # str | The ID of the group whose tags to return.

    try:
        api_response = api_instance.get_group_tags(group_id)
        print("The response of GroupsApi->get_group_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group whose tags to return. | 

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
**200** | The tags applied to the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_users**
> GroupUserList get_group_users(group_id)

Gets the list of users for this group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.group_user_list import GroupUserList
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.

    try:
        api_response = api_instance.get_group_users(group_id)
        print("The response of GroupsApi->get_group_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 

### Return type

[**GroupUserList**](GroupUserList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with access to this group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_visibility**
> VisibilityInfo get_group_visibility(group_id)

Gets the visibility of this group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.visibility_info import VisibilityInfo
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.

    try:
        api_response = api_instance.get_group_visibility(group_id)
        print("The response of GroupsApi->get_group_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 

### Return type

[**VisibilityInfo**](VisibilityInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The visibility info of this group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> PaginatedGroupsList get_groups(cursor=cursor, page_size=page_size, group_type_filter=group_type_filter, group_ids=group_ids, group_name=group_name)

Returns a list of groups for your organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.group_type_enum import GroupTypeEnum
from opal_security.models.paginated_groups_list import PaginatedGroupsList
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
    api_instance = opal_security.GroupsApi(api_client)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)
    group_type_filter = opal_security.GroupTypeEnum() # GroupTypeEnum | The group type to filter by. (optional)
    group_ids = ['[\"4baf8423-db0a-4037-a4cf-f79c60cb67a5\",\"1b978423-db0a-4037-a4cf-f79c60cb67b3\"]'] # List[str] | The group ids to filter by. (optional)
    group_name = 'example-name' # str | Group name. (optional)

    try:
        api_response = api_instance.get_groups(cursor=cursor, page_size=page_size, group_type_filter=group_type_filter, group_ids=group_ids, group_name=group_name)
        print("The response of GroupsApi->get_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 
 **group_type_filter** | [**GroupTypeEnum**](.md)| The group type to filter by. | [optional] 
 **group_ids** | [**List[str]**](str.md)| The group ids to filter by. | [optional] 
 **group_name** | **str**| Group name. | [optional] 

### Return type

[**PaginatedGroupsList**](PaginatedGroupsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page worth groups associated with your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_containing_group**
> remove_group_containing_group(group_id, containing_group_id)

Removes a containing group from a group.

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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    containing_group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the containing group.

    try:
        api_instance.remove_group_containing_group(group_id, containing_group_id)
    except Exception as e:
        print("Exception when calling GroupsApi->remove_group_containing_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **containing_group_id** | **str**| The ID of the containing group. | 

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
**204** | The containing group was successfully removed from the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group_message_channels**
> List[str] set_group_message_channels(group_id, message_channel_id_list)

Sets the list of audit message channels attached to a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.message_channel_id_list import MessageChannelIDList
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    message_channel_id_list = opal_security.MessageChannelIDList() # MessageChannelIDList | 

    try:
        api_response = api_instance.set_group_message_channels(group_id, message_channel_id_list)
        print("The response of GroupsApi->set_group_message_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->set_group_message_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **message_channel_id_list** | [**MessageChannelIDList**](MessageChannelIDList.md)|  | 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated audit message channel IDs for the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group_on_call_schedules**
> List[str] set_group_on_call_schedules(group_id, on_call_schedule_id_list)

Sets the list of on call schedules attached to a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.on_call_schedule_id_list import OnCallScheduleIDList
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    on_call_schedule_id_list = opal_security.OnCallScheduleIDList() # OnCallScheduleIDList | 

    try:
        api_response = api_instance.set_group_on_call_schedules(group_id, on_call_schedule_id_list)
        print("The response of GroupsApi->set_group_on_call_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->set_group_on_call_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **on_call_schedule_id_list** | [**OnCallScheduleIDList**](OnCallScheduleIDList.md)|  | 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated on call schedule IDs for the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group_resources**
> set_group_resources(group_id, update_group_resources_info)

Sets the list of resources that the group gives access to.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.update_group_resources_info import UpdateGroupResourcesInfo
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    update_group_resources_info = opal_security.UpdateGroupResourcesInfo() # UpdateGroupResourcesInfo | 

    try:
        api_instance.set_group_resources(group_id, update_group_resources_info)
    except Exception as e:
        print("Exception when calling GroupsApi->set_group_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **update_group_resources_info** | [**UpdateGroupResourcesInfo**](UpdateGroupResourcesInfo.md)|  | 

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
**200** | The group resource were successfully set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group_reviewer_stages**
> List[ReviewerStage] set_group_reviewer_stages(group_id, reviewer_stage_list)

Sets the list of reviewer stages for a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.reviewer_stage import ReviewerStage
from opal_security.models.reviewer_stage_list import ReviewerStageList
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    reviewer_stage_list = opal_security.ReviewerStageList() # ReviewerStageList | 

    try:
        api_response = api_instance.set_group_reviewer_stages(group_id, reviewer_stage_list)
        print("The response of GroupsApi->set_group_reviewer_stages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->set_group_reviewer_stages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **reviewer_stage_list** | [**ReviewerStageList**](ReviewerStageList.md)|  | 

### Return type

[**List[ReviewerStage]**](ReviewerStage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated reviewer stages for this group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group_reviewers**
> List[str] set_group_reviewers(group_id, reviewer_id_list)

Sets the list of reviewers for a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.reviewer_id_list import ReviewerIDList
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    reviewer_id_list = opal_security.ReviewerIDList() # ReviewerIDList | 

    try:
        api_response = api_instance.set_group_reviewers(group_id, reviewer_id_list)
        print("The response of GroupsApi->set_group_reviewers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->set_group_reviewers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **reviewer_id_list** | [**ReviewerIDList**](ReviewerIDList.md)|  | 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated IDs of owners that are reviewers for this group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group_visibility**
> VisibilityInfo set_group_visibility(group_id, visibility_info)

Sets the visibility of this group.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.visibility_info import VisibilityInfo
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
    api_instance = opal_security.GroupsApi(api_client)
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.
    visibility_info = opal_security.VisibilityInfo() # VisibilityInfo | 

    try:
        api_response = api_instance.set_group_visibility(group_id, visibility_info)
        print("The response of GroupsApi->set_group_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->set_group_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. | 
 **visibility_info** | [**VisibilityInfo**](VisibilityInfo.md)|  | 

### Return type

[**VisibilityInfo**](VisibilityInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The visibility info of this group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_groups**
> UpdateGroupInfoList update_groups(update_group_info_list)

Bulk updates a list of groups.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.update_group_info_list import UpdateGroupInfoList
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
    api_instance = opal_security.GroupsApi(api_client)
    update_group_info_list = opal_security.UpdateGroupInfoList() # UpdateGroupInfoList | Groups to be updated

    try:
        api_response = api_instance.update_groups(update_group_info_list)
        print("The response of GroupsApi->update_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->update_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_group_info_list** | [**UpdateGroupInfoList**](UpdateGroupInfoList.md)| Groups to be updated | 

### Return type

[**UpdateGroupInfoList**](UpdateGroupInfoList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resulting updated group infos. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

