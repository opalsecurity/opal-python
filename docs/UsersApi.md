# opal.UsersApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user**](UsersApi.md#user) | **GET** /user | 


# **user**
> User user()



Returns a `User` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import opal
from opal.api import users_api
from opal.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "32acc112-21ff-4669-91c2-21e27683eaa1" # str | The user ID of the user. (optional)
    email = "johndoe@domain.org" # str | The email of the user. If both user ID and email are provided, user ID will take precedence. If neither are provided, an error will occur. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.user(user_id=user_id, email=email)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling UsersApi->user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID of the user. | [optional]
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

