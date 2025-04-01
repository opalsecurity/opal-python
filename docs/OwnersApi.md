# opal_security.OwnersApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_owner**](OwnersApi.md#create_owner) | **POST** /owners | 
[**delete_owner**](OwnersApi.md#delete_owner) | **DELETE** /owners/{owner_id} | 
[**get_owner**](OwnersApi.md#get_owner) | **GET** /owners/{owner_id} | 
[**get_owner_from_name**](OwnersApi.md#get_owner_from_name) | **GET** /owners/name/{owner_name} | 
[**get_owner_users**](OwnersApi.md#get_owner_users) | **GET** /owners/{owner_id}/users | 
[**get_owners**](OwnersApi.md#get_owners) | **GET** /owners | 
[**set_owner_users**](OwnersApi.md#set_owner_users) | **PUT** /owners/{owner_id}/users | 
[**update_owners**](OwnersApi.md#update_owners) | **PUT** /owners | 


# **create_owner**
> Owner create_owner(create_owner_info)

Creates an owner.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_owner_info import CreateOwnerInfo
from opal_security.models.owner import Owner
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
    api_instance = opal_security.OwnersApi(api_client)
    create_owner_info = opal_security.CreateOwnerInfo() # CreateOwnerInfo | 

    try:
        api_response = api_instance.create_owner(create_owner_info)
        print("The response of OwnersApi->create_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnersApi->create_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_owner_info** | [**CreateOwnerInfo**](CreateOwnerInfo.md)|  | 

### Return type

[**Owner**](Owner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The owner just created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_owner**
> delete_owner(owner_id)

Deletes an owner.

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
    api_instance = opal_security.OwnersApi(api_client)
    owner_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the owner.

    try:
        api_instance.delete_owner(owner_id)
    except Exception as e:
        print("Exception when calling OwnersApi->delete_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| The ID of the owner. | 

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
**200** | The owner was successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_owner**
> Owner get_owner(owner_id)

Returns an `Owner` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.owner import Owner
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
    api_instance = opal_security.OwnersApi(api_client)
    owner_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the owner.

    try:
        api_response = api_instance.get_owner(owner_id)
        print("The response of OwnersApi->get_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnersApi->get_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| The ID of the owner. | 

### Return type

[**Owner**](Owner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The owner object associated with the passed-in ID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_owner_from_name**
> Owner get_owner_from_name(owner_name)

Returns an `Owner` object. Does not support owners with `/` in their name, use /owners?name=... instead.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.owner import Owner
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
    api_instance = opal_security.OwnersApi(api_client)
    owner_name = 'MyOwner' # str | The name of the owner.

    try:
        api_response = api_instance.get_owner_from_name(owner_name)
        print("The response of OwnersApi->get_owner_from_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnersApi->get_owner_from_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **str**| The name of the owner. | 

### Return type

[**Owner**](Owner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The owner object associated with the passed-in name. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_owner_users**
> UserList get_owner_users(owner_id)

Gets the list of users for this owner, in escalation priority order if applicable.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.user_list import UserList
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
    api_instance = opal_security.OwnersApi(api_client)
    owner_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the owner.

    try:
        api_response = api_instance.get_owner_users(owner_id)
        print("The response of OwnersApi->get_owner_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnersApi->get_owner_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| The ID of the owner. | 

### Return type

[**UserList**](UserList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The users for this owner. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_owners**
> PaginatedOwnersList get_owners(cursor=cursor, page_size=page_size, name=name)

Returns a list of `Owner` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_owners_list import PaginatedOwnersList
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
    api_instance = opal_security.OwnersApi(api_client)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)
    name = '200' # str | Owner name to filter by. (optional)

    try:
        api_response = api_instance.get_owners(cursor=cursor, page_size=page_size, name=name)
        print("The response of OwnersApi->get_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnersApi->get_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 
 **name** | **str**| Owner name to filter by. | [optional] 

### Return type

[**PaginatedOwnersList**](PaginatedOwnersList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page worth of owners in your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_owner_users**
> UserList set_owner_users(owner_id, user_id_list)

Sets the list of users for this owner. If escalation is enabled, the order of this list is the escalation priority order of the users. If the owner has a source group, adding or removing users from this list won't be possible.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.user_id_list import UserIDList
from opal_security.models.user_list import UserList
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
    api_instance = opal_security.OwnersApi(api_client)
    owner_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the owner.
    user_id_list = opal_security.UserIDList() # UserIDList | 

    try:
        api_response = api_instance.set_owner_users(owner_id, user_id_list)
        print("The response of OwnersApi->set_owner_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnersApi->set_owner_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| The ID of the owner. | 
 **user_id_list** | [**UserIDList**](UserIDList.md)|  | 

### Return type

[**UserList**](UserList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated users for the owner. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_owners**
> UpdateOwnerInfoList update_owners(update_owner_info_list)

Bulk updates a list of owners.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.update_owner_info_list import UpdateOwnerInfoList
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
    api_instance = opal_security.OwnersApi(api_client)
    update_owner_info_list = opal_security.UpdateOwnerInfoList() # UpdateOwnerInfoList | Owners to be updated

    try:
        api_response = api_instance.update_owners(update_owner_info_list)
        print("The response of OwnersApi->update_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnersApi->update_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_owner_info_list** | [**UpdateOwnerInfoList**](UpdateOwnerInfoList.md)| Owners to be updated | 

### Return type

[**UpdateOwnerInfoList**](UpdateOwnerInfoList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resulting updated owner infos. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

