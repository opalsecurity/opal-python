# opal_security.ServiceUsersApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_user**](ServiceUsersApi.md#create_service_user) | **POST** /service-users | Create service user


# **create_service_user**
> User create_service_user(create_service_user_request)

Create service user

Creates a new service user (a non-human identity owned by a team). Mirrors
the GraphQL `createServiceUser` mutation; admin-only.

The returned `User` object is the newly created service user and is a
regular `User` row — read it later via `GET /users/{user_id}`, delete it
with `DELETE /users/{user_id}`, and manage its tags via the usual
`/users/{user_id}/tags` endpoints.

**Role grants are a separate concern.** To grant a service user access
to resources or groups, use `POST /role-assignments` (or the per-pair
endpoints such as `/resources/{id}/users/{id}`). Keeping role
assignments out of this request body means each grant stays
independently addressable — the shape Terraform and other declarative
clients prefer, with no field here that would silently drift when a
grant is added or revoked through a different code path.

**Automations are not configurable here either.** The GraphQL mutation
accepts a wide typed-union of automation configuration; that surface is
intentionally omitted from this REST endpoint for the same reason.
Service users created through this endpoint start with no automations.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_service_user_request import CreateServiceUserRequest
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
    api_instance = opal_security.ServiceUsersApi(api_client)
    create_service_user_request = opal_security.CreateServiceUserRequest() # CreateServiceUserRequest | 

    try:
        # Create service user
        api_response = api_instance.create_service_user(create_service_user_request)
        print("The response of ServiceUsersApi->create_service_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceUsersApi->create_service_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_service_user_request** | [**CreateServiceUserRequest**](CreateServiceUserRequest.md)|  | 

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
**200** | The created service user. |  -  |
**400** | Invalid request body: malformed JSON, unknown field, missing or empty &#x60;name&#x60;, or missing / malformed &#x60;owner_id&#x60;.  |  -  |
**403** | Caller is not an admin. |  -  |
**404** | The &#x60;owner_id&#x60; does not reference an owner in the organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

