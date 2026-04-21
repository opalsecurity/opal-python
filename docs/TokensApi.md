# opal_security.TokensApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_token**](TokensApi.md#delete_token) | **DELETE** /tokens/{token_id} | Delete token
[**get_tokens**](TokensApi.md#get_tokens) | **GET** /tokens | Get tokens


# **delete_token**
> delete_token(token_id)

Delete token

Deletes a first-party API token. Admins can delete any token. Non-admins can only delete their own tokens when the organization allows all users to create API tokens.

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
    api_instance = opal_security.TokensApi(api_client)
    token_id = UUID('f454d283-ca87-4a8a-bdbb-df212eca5353') # UUID | The ID of the token to delete.

    try:
        # Delete token
        api_instance.delete_token(token_id)
    except Exception as e:
        print("Exception when calling TokensApi->delete_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **UUID**| The ID of the token to delete. | 

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
**200** | The token was successfully deleted. |  -  |
**403** | Not authorized to delete this token. |  -  |
**404** | Token not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens**
> PaginatedTokensList get_tokens(cursor=cursor, page_size=page_size, token_ids=token_ids, user_id=user_id)

Get tokens

Returns a list of first-party API tokens for your organization. Requires admin access.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_tokens_list import PaginatedTokensList
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
    api_instance = opal_security.TokensApi(api_client)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)
    token_ids = None # List[UUID] | Filter by token IDs. (optional)
    user_id = UUID('29827fb8-f2dd-4e80-9576-28e31e9934ac') # UUID | Filter by user ID. (optional)

    try:
        # Get tokens
        api_response = api_instance.get_tokens(cursor=cursor, page_size=page_size, token_ids=token_ids, user_id=user_id)
        print("The response of TokensApi->get_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->get_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 
 **token_ids** | [**List[UUID]**](UUID.md)| Filter by token IDs. | [optional] 
 **user_id** | **UUID**| Filter by user ID. | [optional] 

### Return type

[**PaginatedTokensList**](PaginatedTokensList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of API tokens for your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

