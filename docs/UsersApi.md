# opal_security.UsersApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | 
[**get_remote_users**](UsersApi.md#get_remote_users) | **GET** /users/remote_users | 
[**get_user_access**](UsersApi.md#get_user_access) | **GET** /users/{user_id}/access | Get a user&#39;s access
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{user_id} | Get user by ID
[**get_user_tags**](UsersApi.md#get_user_tags) | **GET** /users/{user_id}/tags | 
[**get_user_whoami**](UsersApi.md#get_user_whoami) | **GET** /users/whoami | 
[**get_users**](UsersApi.md#get_users) | **GET** /users | 
[**invite_user**](UsersApi.md#invite_user) | **POST** /users | 
[**reset_user_mfa**](UsersApi.md#reset_user_mfa) | **POST** /users/{user_id}/mfa/reset | Reset a user&#39;s Opal MFA
[**revoke_all_user_access**](UsersApi.md#revoke_all_user_access) | **POST** /users/{user_id}/revoke-all | Revoke all of a user&#39;s access
[**update_user**](UsersApi.md#update_user) | **PATCH** /users/{user_id} | 
[**user**](UsersApi.md#user) | **GET** /user | 


# **delete_user**
> User delete_user(user_id)

Deletes a user from your organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.user import User
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
    api_instance = opal_security.UsersApi(api_client)
    user_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The ID of the user to delete.

    try:
        api_response = api_instance.delete_user(user_id)
        print("The response of UsersApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The ID of the user to delete. | 

### Return type

[**User**](User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted user. |  -  |
**403** | The caller is not authorized to delete the user. |  -  |
**404** | The user was not found. |  -  |
**409** | The user cannot be deleted in its current state. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_users**
> PaginatedRemoteUsersList get_remote_users(third_party_provider=third_party_provider, user_id=user_id, remote_id=remote_id, cursor=cursor, page_size=page_size)

Returns a list of remote users for your organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_remote_users_list import PaginatedRemoteUsersList
from opal_security.models.third_party_provider_enum import ThirdPartyProviderEnum
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
    api_instance = opal_security.UsersApi(api_client)
    third_party_provider = [opal_security.ThirdPartyProviderEnum()] # List[ThirdPartyProviderEnum] | Filter remote users by their third party provider. (optional)
    user_id = [["32acc112-21ff-4669-91c2-21e27683eaa1"]] # List[UUID] | Filter remote users by their user ID. (optional)
    remote_id = ['[1234567890]'] # List[str] | Filter remote users by their remote ID. (optional)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

    try:
        api_response = api_instance.get_remote_users(third_party_provider=third_party_provider, user_id=user_id, remote_id=remote_id, cursor=cursor, page_size=page_size)
        print("The response of UsersApi->get_remote_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_remote_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_provider** | [**List[ThirdPartyProviderEnum]**](ThirdPartyProviderEnum.md)| Filter remote users by their third party provider. | [optional] 
 **user_id** | [**List[UUID]**](UUID.md)| Filter remote users by their user ID. | [optional] 
 **remote_id** | [**List[str]**](str.md)| Filter remote users by their remote ID. | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 

### Return type

[**PaginatedRemoteUsersList**](PaginatedRemoteUsersList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page worth users in your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_access**
> UserAccessList get_user_access(user_id, cursor=cursor, page_size=page_size, entity_type=entity_type, include_unmanaged=include_unmanaged)

Get a user's access

Returns all of the resources and groups the user has access to, in a single list. All
results are returned unless `page_size` is set, in which case the list is paginated.
Includes access the user has directly and access they have indirectly (for example, through
group membership or nested groups). Use `has_direct_access` and `num_access_paths` to tell
them apart.

Each row is one (resource or group, access level) pair. Only assignments the caller is
allowed to read are returned, so the list can be empty or partial for a caller without
permission to read assignments on the user's resources and groups. Results are ordered by
entity ID; the order is stable across pages but has no other meaning.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.user_access_entity_type_enum import UserAccessEntityTypeEnum
from opal_security.models.user_access_list import UserAccessList
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
    api_instance = opal_security.UsersApi(api_client)
    user_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the user whose access to return.
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The `next` cursor from a previous response. Resumes the list at that point. (optional)
    page_size = 200 # int | Number of results to return per page. Maximum is 1000. If omitted, all results are returned in a single response and `next` is null.  (optional)
    entity_type = opal_security.UserAccessEntityTypeEnum() # UserAccessEntityTypeEnum | Only return access to this type of entity. Omit to return both resources and groups. (optional)
    include_unmanaged = false # bool | Include the user's access to unmanaged resources. (optional)

    try:
        # Get a user's access
        api_response = api_instance.get_user_access(user_id, cursor=cursor, page_size=page_size, entity_type=entity_type, include_unmanaged=include_unmanaged)
        print("The response of UsersApi->get_user_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The ID of the user whose access to return. | 
 **cursor** | **str**| The &#x60;next&#x60; cursor from a previous response. Resumes the list at that point. | [optional] 
 **page_size** | **int**| Number of results to return per page. Maximum is 1000. If omitted, all results are returned in a single response and &#x60;next&#x60; is null.  | [optional] 
 **entity_type** | [**UserAccessEntityTypeEnum**](.md)| Only return access to this type of entity. Omit to return both resources and groups. | [optional] 
 **include_unmanaged** | **bool**| Include the user&#39;s access to unmanaged resources. | [optional] 

### Return type

[**UserAccessList**](UserAccessList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resources and groups the user has access to. |  -  |
**400** | The cursor, &#x60;entity_type&#x60;, or &#x60;user_id&#x60; is invalid. |  -  |
**404** | The user was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> User get_user_by_id(user_id)

Get user by ID

Returns a `User` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.user import User
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
    api_instance = opal_security.UsersApi(api_client)
    user_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the user.

    try:
        # Get user by ID
        api_response = api_instance.get_user_by_id(user_id)
        print("The response of UsersApi->get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The ID of the user. | 

### Return type

[**User**](User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested &#x60;User&#x60;. |  -  |
**404** | The user was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_tags**
> TagsList get_user_tags(user_id)

Returns all tags applied to the user.

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
    api_instance = opal_security.UsersApi(api_client)
    user_id = UUID('1b978423-db0a-4037-a4cf-f79c60cb67b3') # UUID | The ID of the user whose tags to return.

    try:
        api_response = api_instance.get_user_tags(user_id)
        print("The response of UsersApi->get_user_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The ID of the user whose tags to return. | 

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
**200** | The tags applied to the user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_whoami**
> User get_user_whoami()

Returns the user that the provided API token authenticates as.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.user import User
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
    api_instance = opal_security.UsersApi(api_client)

    try:
        api_response = api_instance.get_user_whoami()
        print("The response of UsersApi->get_user_whoami:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_whoami: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user that the API token authenticates as. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> PaginatedUsersList get_users(cursor=cursor, page_size=page_size, tag_ids=tag_ids)

Returns a list of users for your organization. Includes agent-labeled identities that appear on the Users page. Classic service accounts are not included.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_users_list import PaginatedUsersList
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
    api_instance = opal_security.UsersApi(api_client)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)
    tag_ids = None # List[UUID] | The IDs of the tags to filter by. Returns only users that have any of these tags applied. (optional)

    try:
        api_response = api_instance.get_users(cursor=cursor, page_size=page_size, tag_ids=tag_ids)
        print("The response of UsersApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 
 **tag_ids** | [**List[UUID]**](UUID.md)| The IDs of the tags to filter by. Returns only users that have any of these tags applied. | [optional] 

### Return type

[**PaginatedUsersList**](PaginatedUsersList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page worth users in your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user**
> User invite_user(invite_user_info)

Invites a user to your organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.invite_user_info import InviteUserInfo
from opal_security.models.user import User
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
    api_instance = opal_security.UsersApi(api_client)
    invite_user_info = opal_security.InviteUserInfo() # InviteUserInfo | 

    try:
        api_response = api_instance.invite_user(invite_user_info)
        print("The response of UsersApi->invite_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->invite_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_user_info** | [**InviteUserInfo**](InviteUserInfo.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The invited user. |  -  |
**400** | The invite input is invalid. |  -  |
**403** | The caller is not authorized to invite users. |  -  |
**409** | The user already belongs to another organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_user_mfa**
> EscalateRequest200Response reset_user_mfa(user_id)

Reset a user's Opal MFA

Deletes the user's Auth0 (Opal) MFA enrollments so they are prompted to
re-enroll on their next sign-in. Only applies to orgs that use Opal/Auth0
for MFA (not available on-prem, and a no-op success for users who have
never signed into Auth0).


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.escalate_request200_response import EscalateRequest200Response
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
    api_instance = opal_security.UsersApi(api_client)
    user_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the user whose MFA should be reset.

    try:
        # Reset a user's Opal MFA
        api_response = api_instance.reset_user_mfa(user_id)
        print("The response of UsersApi->reset_user_mfa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->reset_user_mfa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The ID of the user whose MFA should be reset. | 

### Return type

[**EscalateRequest200Response**](EscalateRequest200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The MFA enrollments were reset, or the user has no Auth0 enrollments to reset (never signed into Auth0).  |  -  |
**400** | The deployment does not support MFA reset (on-prem), the organization does not use Opal/Auth0 MFA, or the request body contained unknown JSON fields.  |  -  |
**403** | The caller is not authorized to reset MFA for this user. |  -  |
**404** | The user was not found. |  -  |
**409** | The Opal system user cannot be modified. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_all_user_access**
> EscalateRequest200Response revoke_all_user_access(user_id)

Revoke all of a user's access

Immediately removes all of a user's access across connected systems,
regardless of the user's status in the identity provider. Intended for
incident response, e.g. a security tool reacting to a compromised account.
Ends the user's Opal sessions, deletes their Opal API tokens and
third-party tokens, revokes their MCP OAuth grants, removes their direct
group, access rule and resource access (pushing the removals to the
connected systems), and cancels their pending access requests. Recorded
as a USER_ACCESS_REVOKED event with the caller as the actor.

This does not lock the user out, and the revocation does not last on its
own. The user and their accounts in connected systems are kept, and they
can sign in again through your identity provider. Access granted by Opal
access rules is granted again on the next access rule sync while the user
still matches the rule, and memberships that identity provider rules
control return on the next identity provider sync. To keep the user's
access revoked, also disable or deprovision them in your identity
provider. With the organization setting that revokes access for
deprovisioned users turned on, Opal then offboards them and stops granting
them access through access rules.

Also not removed: membership in groups computed by a connected system
(e.g. dynamic groups), access to unmanaged groups and resources, and the
user's owner and reviewer roles. Removal from connected systems runs
asynchronously; a 200 response means the removals were started, not that
every connected system has finished. A removal that failed permanently
before is retried. A removal that is already in progress is left to
finish and is not started again, so check its propagation status if it
stays pending.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.escalate_request200_response import EscalateRequest200Response
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
    api_instance = opal_security.UsersApi(api_client)
    user_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the user whose access should be revoked.

    try:
        # Revoke all of a user's access
        api_response = api_instance.revoke_all_user_access(user_id)
        print("The response of UsersApi->revoke_all_user_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->revoke_all_user_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The ID of the user whose access should be revoked. | 

### Return type

[**EscalateRequest200Response**](EscalateRequest200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user&#39;s access removal was started. |  -  |
**400** | The request body contained unknown JSON fields. |  -  |
**403** | The caller is not authorized to delete this user. |  -  |
**404** | The user was not found. |  -  |
**409** | The Opal system user cannot be modified, or the user is the last direct Opal admin. Their API tokens, third-party tokens and MCP OAuth grants are still revoked and their pending requests still canceled in that case.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, update_user_info)

Updates a user's position or manager.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.update_user_info import UpdateUserInfo
from opal_security.models.user import User
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
    api_instance = opal_security.UsersApi(api_client)
    user_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The ID of the user to update.
    update_user_info = opal_security.UpdateUserInfo() # UpdateUserInfo | 

    try:
        api_response = api_instance.update_user(user_id, update_user_info)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The ID of the user to update. | 
 **update_user_info** | [**UpdateUserInfo**](UpdateUserInfo.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated user. |  -  |
**400** | The update input is invalid. |  -  |
**403** | The caller is not authorized to update the user. |  -  |
**404** | The user was not found. |  -  |
**409** | The user is managed by an identity provider or is immutable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user**
> User user(user_id=user_id, email=email)

Returns a `User` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.user import User
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
    api_instance = opal_security.UsersApi(api_client)
    user_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The user ID of the user. (optional)
    email = 'johndoe@domain.org' # str | The email of the user. If both user ID and email are provided, user ID will take precedence. If neither are provided, an error will occur. (optional)

    try:
        api_response = api_instance.user(user_id=user_id, email=email)
        print("The response of UsersApi->user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The user ID of the user. | [optional] 
 **email** | **str**| The email of the user. If both user ID and email are provided, user ID will take precedence. If neither are provided, an error will occur. | [optional] 

### Return type

[**User**](User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user object associated with the passed-in email or ID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

