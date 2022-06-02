# opal.GroupsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_group**](GroupsApi.md#convert_group) | **PUT** /groups/{group_id}/convert | 
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /groups/{group_id} | 
[**get_group_message_channels**](GroupsApi.md#get_group_message_channels) | **GET** /groups/{group_id}/message-channels | 
[**get_group_reviewers**](GroupsApi.md#get_group_reviewers) | **GET** /groups/{group_id}/reviewers | 
[**get_group_tags**](GroupsApi.md#get_group_tags) | **GET** /groups/{group_id}/tags | 
[**get_groups**](GroupsApi.md#get_groups) | **GET** /groups | 
[**set_group_message_channels**](GroupsApi.md#set_group_message_channels) | **PUT** /groups/{group_id}/message-channels | 
[**set_group_reviewers**](GroupsApi.md#set_group_reviewers) | **PUT** /groups/{group_id}/reviewers | 
[**update_groups**](GroupsApi.md#update_groups) | **PUT** /groups | 


# **convert_group**
> Group convert_group(group_id, group_function, new_admin_id_list)



Updates a groups function.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import groups_api
from opal.model.group_function_enum import GroupFunctionEnum
from opal.model.group import Group
from opal.model.new_admin_id_list import NewAdminIDList
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the group.
    group_function = GroupFunctionEnum("TEAM") # GroupFunctionEnum | The group function to convert to.
    new_admin_id_list = NewAdminIDList(
        admin_ids=[
            "admin_ids_example",
        ],
    ) # NewAdminIDList | 
    owner_team_id = "7c86c85d-0651-43e2-a748-d69d658418e8" # str | The ID of the owning team of the group. Required when converting from Team to Group. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.convert_group(group_id, group_function, new_admin_id_list)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling GroupsApi->convert_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.convert_group(group_id, group_function, new_admin_id_list, owner_team_id=owner_team_id)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling GroupsApi->convert_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. |
 **group_function** | **GroupFunctionEnum**| The group function to convert to. |
 **new_admin_id_list** | [**NewAdminIDList**](NewAdminIDList.md)|  |
 **owner_team_id** | **str**| The ID of the owning team of the group. Required when converting from Team to Group. | [optional]

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
**200** | The converted group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id)



Deletes a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the group.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_group(group_id)
    except opal.ApiException as e:
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

# **get_group_message_channels**
> MessageChannelList get_group_message_channels(group_id)



Gets the list of message channels attached to a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the group.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_group_message_channels(group_id)
        pprint(api_response)
    except opal.ApiException as e:
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
**200** | The message channels attached to the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_reviewers**
> [str] get_group_reviewers(group_id)



Gets the list of team/user IDs of the reviewers for a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the group.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_group_reviewers(group_id)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling GroupsApi->get_group_reviewers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. |

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
**200** | The IDs of teams/users that are reviewers for this group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_tags**
> TagsList get_group_tags(group_id)



Returns all tags applied to the group.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = "1b978423-db0a-4037-a4cf-f79c60cb67b3" # str | The ID of the group whose tags to return.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_group_tags(group_id)
        pprint(api_response)
    except opal.ApiException as e:
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

# **get_groups**
> PaginatedGroupsList get_groups()



Returns a list of groups for your organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import groups_api
from opal.model.group_function_enum import GroupFunctionEnum
from opal.model.paginated_groups_list import PaginatedGroupsList
from opal.model.group_type_enum import GroupTypeEnum
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
    api_instance = groups_api.GroupsApi(api_client)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)
    group_function_filter = GroupFunctionEnum("REGULAR") # GroupFunctionEnum | The group function to filter by. (optional)
    group_type_filter = GroupTypeEnum("OPAL_GROUP") # GroupTypeEnum | The group type to filter by. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_groups(cursor=cursor, page_size=page_size, group_function_filter=group_function_filter, group_type_filter=group_type_filter)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling GroupsApi->get_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional]
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional]
 **group_function_filter** | **GroupFunctionEnum**| The group function to filter by. | [optional]
 **group_type_filter** | **GroupTypeEnum**| The group type to filter by. | [optional]

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

# **set_group_message_channels**
> [str] set_group_message_channels(group_id, message_channel_id_list)



Sets the list of message channels attached to a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the group.
    message_channel_id_list = MessageChannelIDList(
        message_channel_ids=[
            "message_channel_ids_example",
        ],
    ) # MessageChannelIDList | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_group_message_channels(group_id, message_channel_id_list)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling GroupsApi->set_group_message_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. |
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
**200** | The updated message channel IDs for the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group_reviewers**
> [str] set_group_reviewers(group_id, reviewer_id_list)



Sets the list of reviewers for a group.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = "4baf8423-db0a-4037-a4cf-f79c60cb67a5" # str | The ID of the group.
    reviewer_id_list = ReviewerIDList(
        reviewer_ids=[
            "reviewer_ids_example",
        ],
    ) # ReviewerIDList | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_group_reviewers(group_id, reviewer_id_list)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling GroupsApi->set_group_reviewers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the group. |
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
**200** | The updated IDs of teams/users that are reviewers for this group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_groups**
> UpdateGroupInfoList update_groups(update_group_info_list)



Bulk updates a list of groups.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import groups_api
from opal.model.update_group_info_list import UpdateGroupInfoList
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
    api_instance = groups_api.GroupsApi(api_client)
    update_group_info_list = UpdateGroupInfoList(
        groups=[
            UpdateGroupInfo(
                group_id="f454d283-ca87-4a8a-bdbb-df212eca5353",
                name="api-group",
                description="This group represents Active Directory group "Payments Production Admin". We use this AD group to facilitate staging deployments and qualifying new releases.",
                owner_team_id="7c86c85d-0651-43e2-a748-d69d658418e8",
                visibility=VisibilityEnum("GLOBAL"),
                max_duration=120,
                require_manager_approval=False,
                require_support_ticket=False,
                folder_id="e27cb7b0-98e2-4555-9916-9e6d8ca6b079",
            ),
        ],
    ) # UpdateGroupInfoList | Groups to be updated

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_groups(update_group_info_list)
        pprint(api_response)
    except opal.ApiException as e:
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

