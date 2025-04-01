# opal_security.ResourcesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_resource_nhi**](ResourcesApi.md#add_resource_nhi) | **POST** /resources/{resource_id}/non-human-identities/{non_human_identity_id} | 
[**add_resource_user**](ResourcesApi.md#add_resource_user) | **POST** /resources/{resource_id}/users/{user_id} | 
[**create_resource**](ResourcesApi.md#create_resource) | **POST** /resources | 
[**delete_resource**](ResourcesApi.md#delete_resource) | **DELETE** /resources/{resource_id} | 
[**delete_resource_nhi**](ResourcesApi.md#delete_resource_nhi) | **DELETE** /resources/{resource_id}/non-human-identities/{non_human_identity_id} | 
[**delete_resource_user**](ResourcesApi.md#delete_resource_user) | **DELETE** /resources/{resource_id}/users/{user_id} | 
[**get_resource**](ResourcesApi.md#get_resource) | **GET** /resources/{resource_id} | 
[**get_resource_message_channels**](ResourcesApi.md#get_resource_message_channels) | **GET** /resources/{resource_id}/message-channels | 
[**get_resource_nhis**](ResourcesApi.md#get_resource_nhis) | **GET** /resources/{resource_id}/non-human-identities | 
[**get_resource_reviewer_stages**](ResourcesApi.md#get_resource_reviewer_stages) | **GET** /resources/{resource_id}/reviewer-stages | 
[**get_resource_reviewers**](ResourcesApi.md#get_resource_reviewers) | **GET** /resources/{resource_id}/reviewers | 
[**get_resource_tags**](ResourcesApi.md#get_resource_tags) | **GET** /resources/{resource_id}/tags | 
[**get_resource_users**](ResourcesApi.md#get_resource_users) | **GET** /resources/{resource_id}/users | 
[**get_resource_visibility**](ResourcesApi.md#get_resource_visibility) | **GET** /resources/{resource_id}/visibility | 
[**get_resources**](ResourcesApi.md#get_resources) | **GET** /resources | 
[**resource_user_access_status_retrieve**](ResourcesApi.md#resource_user_access_status_retrieve) | **GET** /resource-user-access-status/{resource_id}/{user_id} | 
[**set_resource_message_channels**](ResourcesApi.md#set_resource_message_channels) | **PUT** /resources/{resource_id}/message-channels | 
[**set_resource_reviewer_stages**](ResourcesApi.md#set_resource_reviewer_stages) | **PUT** /resources/{resource_id}/reviewer-stages | 
[**set_resource_reviewers**](ResourcesApi.md#set_resource_reviewers) | **PUT** /resources/{resource_id}/reviewers | 
[**set_resource_visibility**](ResourcesApi.md#set_resource_visibility) | **PUT** /resources/{resource_id}/visibility | 
[**update_resource_user**](ResourcesApi.md#update_resource_user) | **PUT** /resources/{resource_id}/users/{user_id} | 
[**update_resources**](ResourcesApi.md#update_resources) | **PUT** /resources | 


# **add_resource_nhi**
> ResourceNHI add_resource_nhi(resource_id, non_human_identity_id, add_resource_nhi_request=add_resource_nhi_request)

Gives a non-human identity access to this resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.add_resource_nhi_request import AddResourceNhiRequest
from opal_security.models.resource_nhi import ResourceNHI
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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    non_human_identity_id = 'f92aa855-cea9-4814-b9d8-f2a60d3e4a06' # str | The resource ID of the non-human identity to add.
    add_resource_nhi_request = opal_security.AddResourceNhiRequest() # AddResourceNhiRequest |  (optional)

    try:
        api_response = api_instance.add_resource_nhi(resource_id, non_human_identity_id, add_resource_nhi_request=add_resource_nhi_request)
        print("The response of ResourcesApi->add_resource_nhi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->add_resource_nhi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
 **non_human_identity_id** | **str**| The resource ID of the non-human identity to add. | 
 **add_resource_nhi_request** | [**AddResourceNhiRequest**](AddResourceNhiRequest.md)|  | [optional] 

### Return type

[**ResourceNHI**](ResourceNHI.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the access that the non-human identity was granted to the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_resource_user**
> ResourceUser add_resource_user(resource_id, user_id, duration_minutes=duration_minutes, access_level_remote_id=access_level_remote_id, add_resource_user_request=add_resource_user_request)

Adds a user to this resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.add_resource_user_request import AddResourceUserRequest
from opal_security.models.resource_user import ResourceUser
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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    user_id = 'f92aa855-cea9-4814-b9d8-f2a60d3e4a06' # str | The ID of the user to add.
    duration_minutes = 60 # int | The duration for which the resource can be accessed (in minutes). Use 0 to set to indefinite. (optional)
    access_level_remote_id = 'arn:aws:iam::590304332660:role/AdministratorAccess' # str | The remote ID of the access level to grant to this user. If omitted, the default access level remote ID value (empty string) is used. (optional)
    add_resource_user_request = opal_security.AddResourceUserRequest() # AddResourceUserRequest |  (optional)

    try:
        api_response = api_instance.add_resource_user(resource_id, user_id, duration_minutes=duration_minutes, access_level_remote_id=access_level_remote_id, add_resource_user_request=add_resource_user_request)
        print("The response of ResourcesApi->add_resource_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->add_resource_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
 **user_id** | **str**| The ID of the user to add. | 
 **duration_minutes** | **int**| The duration for which the resource can be accessed (in minutes). Use 0 to set to indefinite. | [optional] 
 **access_level_remote_id** | **str**| The remote ID of the access level to grant to this user. If omitted, the default access level remote ID value (empty string) is used. | [optional] 
 **add_resource_user_request** | [**AddResourceUserRequest**](AddResourceUserRequest.md)|  | [optional] 

### Return type

[**ResourceUser**](ResourceUser.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ResourceUser that was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_resource**
> Resource create_resource(create_resource_info)

Creates a resource. See [here](https://docs.opal.dev/reference/end-system-objects) for details about importing resources.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_resource_info import CreateResourceInfo
from opal_security.models.resource import Resource
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
    api_instance = opal_security.ResourcesApi(api_client)
    create_resource_info = opal_security.CreateResourceInfo() # CreateResourceInfo | 

    try:
        api_response = api_instance.create_resource(create_resource_info)
        print("The response of ResourcesApi->create_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->create_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_resource_info** | [**CreateResourceInfo**](CreateResourceInfo.md)|  | 

### Return type

[**Resource**](Resource.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resource just created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource**
> delete_resource(resource_id)

Deletes a resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.

    try:
        api_instance.delete_resource(resource_id)
    except Exception as e:
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

# **delete_resource_nhi**
> delete_resource_nhi(resource_id, non_human_identity_id, access_level_remote_id=access_level_remote_id)

Removes a non-human identity's direct access from this resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    non_human_identity_id = 'f92aa855-cea9-4814-b9d8-f2a60d3e4a06' # str | The resource ID of the non-human identity to remove from this resource.
    access_level_remote_id = 'roles/cloudsql.instanceUser' # str | The remote ID of the access level for which this non-human identity has direct access. If omitted, the default access level remote ID value (empty string) is assumed. (optional)

    try:
        api_instance.delete_resource_nhi(resource_id, non_human_identity_id, access_level_remote_id=access_level_remote_id)
    except Exception as e:
        print("Exception when calling ResourcesApi->delete_resource_nhi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
 **non_human_identity_id** | **str**| The resource ID of the non-human identity to remove from this resource. | 
 **access_level_remote_id** | **str**| The remote ID of the access level for which this non-human identity has direct access. If omitted, the default access level remote ID value (empty string) is assumed. | [optional] 

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
**200** | This non-human identity&#39;s access was successfully removed from this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_user**
> delete_resource_user(resource_id, user_id, access_level_remote_id=access_level_remote_id)

Removes a user's direct access from this resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    user_id = 'f92aa855-cea9-4814-b9d8-f2a60d3e4a06' # str | The ID of a user to remove from this resource.
    access_level_remote_id = 'arn:aws:iam::590304332660:role/AdministratorAccess' # str | The remote ID of the access level for which this user has direct access. If omitted, the default access level remote ID value (empty string) is assumed. (optional)

    try:
        api_instance.delete_resource_user(resource_id, user_id, access_level_remote_id=access_level_remote_id)
    except Exception as e:
        print("Exception when calling ResourcesApi->delete_resource_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
 **user_id** | **str**| The ID of a user to remove from this resource. | 
 **access_level_remote_id** | **str**| The remote ID of the access level for which this user has direct access. If omitted, the default access level remote ID value (empty string) is assumed. | [optional] 

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
**200** | This user&#39;s access was successfully removed from this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource**
> Resource get_resource(resource_id)

Retrieves a resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.resource import Resource
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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.

    try:
        api_response = api_instance.get_resource(resource_id)
        print("The response of ResourcesApi->get_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->get_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 

### Return type

[**Resource**](Resource.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_message_channels**
> MessageChannelList get_resource_message_channels(resource_id)

Gets the list of audit message channels attached to a resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.

    try:
        api_response = api_instance.get_resource_message_channels(resource_id)
        print("The response of ResourcesApi->get_resource_message_channels:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | The audit message channels attached to the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_nhis**
> AccessList get_resource_nhis(resource_id, limit=limit)

Gets the list of non-human identities with access to this resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.access_list import AccessList
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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    limit = 200 # int | Limit the number of results returned. (optional)

    try:
        api_response = api_instance.get_resource_nhis(resource_id, limit=limit)
        print("The response of ResourcesApi->get_resource_nhis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->get_resource_nhis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
 **limit** | **int**| Limit the number of results returned. | [optional] 

### Return type

[**AccessList**](AccessList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of non-human identities with access to this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_reviewer_stages**
> List[ReviewerStage] get_resource_reviewer_stages(resource_id)

Gets the list reviewer stages for a resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.

    try:
        api_response = api_instance.get_resource_reviewer_stages(resource_id)
        print("The response of ResourcesApi->get_resource_reviewer_stages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->get_resource_reviewer_stages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 

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
**200** | The reviewer stages for this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_reviewers**
> List[str] get_resource_reviewers(resource_id)

Gets the list of owner IDs of the reviewers for a resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.

    try:
        api_response = api_instance.get_resource_reviewers(resource_id)
        print("The response of ResourcesApi->get_resource_reviewers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->get_resource_reviewers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 

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
**200** | The IDs of owners that are reviewers for this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_tags**
> TagsList get_resource_tags(resource_id)

Returns all tags applied to the resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '1b978423-db0a-4037-a4cf-f79c60cb67b3' # str | The ID of the resource whose tags to return.

    try:
        api_response = api_instance.get_resource_tags(resource_id)
        print("The response of ResourcesApi->get_resource_tags:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_resource_users**
> ResourceAccessUserList get_resource_users(resource_id, limit=limit)

Gets the list of users for this resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.resource_access_user_list import ResourceAccessUserList
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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    limit = 200 # int | Limit the number of results returned. (optional)

    try:
        api_response = api_instance.get_resource_users(resource_id, limit=limit)
        print("The response of ResourcesApi->get_resource_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->get_resource_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
 **limit** | **int**| Limit the number of results returned. | [optional] 

### Return type

[**ResourceAccessUserList**](ResourceAccessUserList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with access to this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_visibility**
> VisibilityInfo get_resource_visibility(resource_id)

Gets the visibility of this resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.

    try:
        api_response = api_instance.get_resource_visibility(resource_id)
        print("The response of ResourcesApi->get_resource_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->get_resource_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 

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
**200** | The visibility info of this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> PaginatedResourcesList get_resources(cursor=cursor, page_size=page_size, resource_type_filter=resource_type_filter, resource_ids=resource_ids, resource_name=resource_name, parent_resource_id=parent_resource_id)

Returns a list of resources for your organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_resources_list import PaginatedResourcesList
from opal_security.models.resource_type_enum import ResourceTypeEnum
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
    api_instance = opal_security.ResourcesApi(api_client)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)
    resource_type_filter = opal_security.ResourceTypeEnum() # ResourceTypeEnum | The resource type to filter by. (optional)
    resource_ids = ['[\"4baf8423-db0a-4037-a4cf-f79c60cb67a5\",\"1b978423-db0a-4037-a4cf-f79c60cb67b3\"]'] # List[str] | The resource ids to filter by. (optional)
    resource_name = 'example-name' # str | Resource name. (optional)
    parent_resource_id = '[\"4baf8423-db0a-4037-a4cf-f79c60cb67a5\"]' # str | The parent resource id to filter by. (optional)

    try:
        api_response = api_instance.get_resources(cursor=cursor, page_size=page_size, resource_type_filter=resource_type_filter, resource_ids=resource_ids, resource_name=resource_name, parent_resource_id=parent_resource_id)
        print("The response of ResourcesApi->get_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->get_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 
 **resource_type_filter** | [**ResourceTypeEnum**](.md)| The resource type to filter by. | [optional] 
 **resource_ids** | [**List[str]**](str.md)| The resource ids to filter by. | [optional] 
 **resource_name** | **str**| Resource name. | [optional] 
 **parent_resource_id** | **str**| The parent resource id to filter by. | [optional] 

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
> ResourceUserAccessStatus resource_user_access_status_retrieve(resource_id, user_id, access_level_remote_id=access_level_remote_id, cursor=cursor, page_size=page_size)

Get user's access status to a resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.resource_user_access_status import ResourceUserAccessStatus
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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '1b978423-db0a-4037-a4cf-f79c60cb67b3' # str | The ID of the resource.
    user_id = '29827fb8-f2dd-4e80-9576-28e31e9934ac' # str | The ID of the user.
    access_level_remote_id = 'arn:aws:iam::590304332660:role/AdministratorAccess' # str | The remote ID of the access level that you wish to query for the resource. If omitted, the default access level remote ID value (empty string) is used. (optional)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

    try:
        api_response = api_instance.resource_user_access_status_retrieve(resource_id, user_id, access_level_remote_id=access_level_remote_id, cursor=cursor, page_size=page_size)
        print("The response of ResourcesApi->resource_user_access_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
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

# **set_resource_message_channels**
> List[str] set_resource_message_channels(resource_id, message_channel_id_list)

Sets the list of audit message channels attached to a resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    message_channel_id_list = opal_security.MessageChannelIDList() # MessageChannelIDList | 

    try:
        api_response = api_instance.set_resource_message_channels(resource_id, message_channel_id_list)
        print("The response of ResourcesApi->set_resource_message_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->set_resource_message_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
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
**200** | The updated audit message channel IDs for the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_resource_reviewer_stages**
> List[ReviewerStage] set_resource_reviewer_stages(resource_id, reviewer_stage_list)

Sets the list of reviewer stages for a resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    reviewer_stage_list = opal_security.ReviewerStageList() # ReviewerStageList | 

    try:
        api_response = api_instance.set_resource_reviewer_stages(resource_id, reviewer_stage_list)
        print("The response of ResourcesApi->set_resource_reviewer_stages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->set_resource_reviewer_stages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
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
**200** | The updated reviewer stages for this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_resource_reviewers**
> List[str] set_resource_reviewers(resource_id, reviewer_id_list)

Sets the list of reviewers for a resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    reviewer_id_list = opal_security.ReviewerIDList() # ReviewerIDList | 

    try:
        api_response = api_instance.set_resource_reviewers(resource_id, reviewer_id_list)
        print("The response of ResourcesApi->set_resource_reviewers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->set_resource_reviewers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
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
**200** | The updated IDs of owners that are reviewers for this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_resource_visibility**
> VisibilityInfo set_resource_visibility(resource_id, visibility_info)

Sets the visibility of this resource.

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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    visibility_info = opal_security.VisibilityInfo() # VisibilityInfo | 

    try:
        api_response = api_instance.set_resource_visibility(resource_id, visibility_info)
        print("The response of ResourcesApi->set_resource_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->set_resource_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
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
**200** | The visibility info of this resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_user**
> ResourceUser update_resource_user(resource_id, user_id, update_resource_user_request)

Updates a user's access level or duration on this resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.resource_user import ResourceUser
from opal_security.models.update_resource_user_request import UpdateResourceUserRequest
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
    api_instance = opal_security.ResourcesApi(api_client)
    resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the resource.
    user_id = 'f92aa855-cea9-4814-b9d8-f2a60d3e4a06' # str | The ID of the user whose access is being updated.
    update_resource_user_request = opal_security.UpdateResourceUserRequest() # UpdateResourceUserRequest | 

    try:
        api_response = api_instance.update_resource_user(resource_id, user_id, update_resource_user_request)
        print("The response of ResourcesApi->update_resource_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->update_resource_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource. | 
 **user_id** | **str**| The ID of the user whose access is being updated. | 
 **update_resource_user_request** | [**UpdateResourceUserRequest**](UpdateResourceUserRequest.md)|  | 

### Return type

[**ResourceUser**](ResourceUser.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ResourceUser was successfully updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resources**
> UpdateResourceInfoList update_resources(update_resource_info_list)

Bulk updates a list of resources.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.update_resource_info_list import UpdateResourceInfoList
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
    api_instance = opal_security.ResourcesApi(api_client)
    update_resource_info_list = opal_security.UpdateResourceInfoList() # UpdateResourceInfoList | Resources to be updated

    try:
        api_response = api_instance.update_resources(update_resource_info_list)
        print("The response of ResourcesApi->update_resources:\n")
        pprint(api_response)
    except Exception as e:
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

