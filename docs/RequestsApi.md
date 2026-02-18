# opal_security.RequestsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_request**](RequestsApi.md#approve_request) | **POST** /requests/{id}/approve | 
[**create_request**](RequestsApi.md#create_request) | **POST** /requests | 
[**create_request_comment**](RequestsApi.md#create_request_comment) | **POST** /requests/{id}/comments | 
[**deny_request**](RequestsApi.md#deny_request) | **POST** /requests/{id}/deny | 
[**get_request**](RequestsApi.md#get_request) | **GET** /requests/{id} | Get request by ID
[**get_request_comments**](RequestsApi.md#get_request_comments) | **GET** /requests/{id}/comments | 
[**get_requests**](RequestsApi.md#get_requests) | **GET** /requests | Get requests
[**get_requests_relay**](RequestsApi.md#get_requests_relay) | **GET** /requests/relay | Get requests via Relay


# **approve_request**
> ApproveRequest200Response approve_request(id, approve_request_request)

Approve an access request

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.approve_request200_response import ApproveRequest200Response
from opal_security.models.approve_request_request import ApproveRequestRequest
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
    api_instance = opal_security.RequestsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The ID of the request to approve
    approve_request_request = opal_security.ApproveRequestRequest() # ApproveRequestRequest | Approval parameters

    try:
        api_response = api_instance.approve_request(id, approve_request_request)
        print("The response of RequestsApi->approve_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->approve_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the request to approve | 
 **approve_request_request** | [**ApproveRequestRequest**](ApproveRequestRequest.md)| Approval parameters | 

### Return type

[**ApproveRequest200Response**](ApproveRequest200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successfully approved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_request**
> CreateRequest200Response create_request(create_request_info)

Create an access request

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_request200_response import CreateRequest200Response
from opal_security.models.create_request_info import CreateRequestInfo
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
    api_instance = opal_security.RequestsApi(api_client)
    create_request_info = opal_security.CreateRequestInfo() # CreateRequestInfo | Resources to be updated

    try:
        api_response = api_instance.create_request(create_request_info)
        print("The response of RequestsApi->create_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->create_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request_info** | [**CreateRequestInfo**](CreateRequestInfo.md)| Resources to be updated | 

### Return type

[**CreateRequest200Response**](CreateRequest200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resulting request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_request_comment**
> ApproveRequest200Response create_request_comment(id, create_request_comment_request)

Comment on an access request

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.approve_request200_response import ApproveRequest200Response
from opal_security.models.create_request_comment_request import CreateRequestCommentRequest
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
    api_instance = opal_security.RequestsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The ID of the request to comment on
    create_request_comment_request = opal_security.CreateRequestCommentRequest() # CreateRequestCommentRequest | Comment parameters

    try:
        api_response = api_instance.create_request_comment(id, create_request_comment_request)
        print("The response of RequestsApi->create_request_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->create_request_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the request to comment on | 
 **create_request_comment_request** | [**CreateRequestCommentRequest**](CreateRequestCommentRequest.md)| Comment parameters | 

### Return type

[**ApproveRequest200Response**](ApproveRequest200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successfully commented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deny_request**
> ApproveRequest200Response deny_request(id, deny_request_request)

Deny an access request

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.approve_request200_response import ApproveRequest200Response
from opal_security.models.deny_request_request import DenyRequestRequest
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
    api_instance = opal_security.RequestsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The ID of the request to deny
    deny_request_request = opal_security.DenyRequestRequest() # DenyRequestRequest | Denial parameters

    try:
        api_response = api_instance.deny_request(id, deny_request_request)
        print("The response of RequestsApi->deny_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->deny_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the request to deny | 
 **deny_request_request** | [**DenyRequestRequest**](DenyRequestRequest.md)| Denial parameters | 

### Return type

[**ApproveRequest200Response**](ApproveRequest200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successfully denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request**
> Request get_request(id)

Get request by ID

Returns a request by ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.request import Request
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
    api_instance = opal_security.RequestsApi(api_client)
    id = UUID('4baf8423-db0a-4037-a4cf-f79c60cb67a5') # UUID | The ID of the request.

    try:
        # Get request by ID
        api_response = api_instance.get_request(id)
        print("The response of RequestsApi->get_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the request. | 

### Return type

[**Request**](Request.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested request object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_comments**
> RequestCommentList get_request_comments(id)

Returns a list of comments for a specific request.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.request_comment_list import RequestCommentList
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
    api_instance = opal_security.RequestsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The ID of the request to get comments for

    try:
        api_response = api_instance.get_request_comments(id)
        print("The response of RequestsApi->get_request_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_request_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The ID of the request to get comments for | 

### Return type

[**RequestCommentList**](RequestCommentList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of comments associated with the specified request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requests**
> RequestList get_requests(start_date_filter=start_date_filter, end_date_filter=end_date_filter, requester_id=requester_id, target_user_id=target_user_id, cursor=cursor, page_size=page_size, show_pending_only=show_pending_only)

Get requests

Returns a list of requests for your organization that is visible by the admin.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.request_list import RequestList
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
    api_instance = opal_security.RequestsApi(api_client)
    start_date_filter = '2021-11-01' # str | A start date filter for the events. (optional)
    end_date_filter = '2021-11-12' # str | An end date filter for the events. (optional)
    requester_id = UUID('37cb7e41-12ba-46da-92ff-030abe0450b1') # UUID | Filter requests by their requester ID. (optional)
    target_user_id = UUID('37cb7e41-12ba-46da-92ff-030abe0450b1') # UUID | Filter requests by their target user ID. (optional)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)
    show_pending_only = True # bool | Boolean toggle for if it should only show pending requests. (optional)

    try:
        # Get requests
        api_response = api_instance.get_requests(start_date_filter=start_date_filter, end_date_filter=end_date_filter, requester_id=requester_id, target_user_id=target_user_id, cursor=cursor, page_size=page_size, show_pending_only=show_pending_only)
        print("The response of RequestsApi->get_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_filter** | **str**| A start date filter for the events. | [optional] 
 **end_date_filter** | **str**| An end date filter for the events. | [optional] 
 **requester_id** | **UUID**| Filter requests by their requester ID. | [optional] 
 **target_user_id** | **UUID**| Filter requests by their target user ID. | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 
 **show_pending_only** | **bool**| Boolean toggle for if it should only show pending requests. | [optional] 

### Return type

[**RequestList**](RequestList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requests. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requests_relay**
> RequestConnection get_requests_relay(first=first, after=after, last=last, before=before, status=status, to=to, var_from=var_from)

Get requests via Relay

Returns a paginated list of requests using Relay-style cursor pagination.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.request_connection import RequestConnection
from opal_security.models.request_status_enum import RequestStatusEnum
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
    api_instance = opal_security.RequestsApi(api_client)
    first = 10 # int | Number of results to return after the cursor. Use either first/after or last/before, not both. (optional)
    after = 'Y3Vyc29yOnYyOpK5MjAyMS0wMS0wN1QwNzo0MToyNy4xMTlaFjYwZmM2YmJlZjk4YzE1N2ZhNjFhYjk4Nw==' # str | Cursor to fetch results after. Used with 'first' for forward pagination. (optional)
    last = 10 # int | Number of results to return before the cursor. Use either first/after or last/before, not both. (optional)
    before = 'Y3Vyc29yOnYyOpK5MjAyMS0wMS0wN1QwNzo0MToyNy4xMTlaFjYwZmM2YmJlZjk4YzE1N2ZhNjFhYjk4Nw==' # str | Cursor to fetch results before. Used with 'last' for backward pagination. (optional)
    status = opal_security.RequestStatusEnum() # RequestStatusEnum | Filter requests by their status. (optional)
    to = UUID('37cb7e41-12ba-46da-92ff-030abe0450b1') # UUID | Filter requests assigned to a specific user ID. (optional)
    var_from = UUID('37cb7e41-12ba-46da-92ff-030abe0450b1') # UUID | Filter requests made by a specific user ID. (optional)

    try:
        # Get requests via Relay
        api_response = api_instance.get_requests_relay(first=first, after=after, last=last, before=before, status=status, to=to, var_from=var_from)
        print("The response of RequestsApi->get_requests_relay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_requests_relay: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first** | **int**| Number of results to return after the cursor. Use either first/after or last/before, not both. | [optional] 
 **after** | **str**| Cursor to fetch results after. Used with &#39;first&#39; for forward pagination. | [optional] 
 **last** | **int**| Number of results to return before the cursor. Use either first/after or last/before, not both. | [optional] 
 **before** | **str**| Cursor to fetch results before. Used with &#39;last&#39; for backward pagination. | [optional] 
 **status** | [**RequestStatusEnum**](.md)| Filter requests by their status. | [optional] 
 **to** | **UUID**| Filter requests assigned to a specific user ID. | [optional] 
 **var_from** | **UUID**| Filter requests made by a specific user ID. | [optional] 

### Return type

[**RequestConnection**](RequestConnection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of requests using Relay-style cursor pagination. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

