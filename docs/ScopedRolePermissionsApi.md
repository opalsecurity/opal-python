# opal_security.ScopedRolePermissionsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resource_scoped_role_permissions**](ScopedRolePermissionsApi.md#get_resource_scoped_role_permissions) | **GET** /resources/{resource_id}/scoped-role-permissions | 
[**set_resource_scoped_role_permissions**](ScopedRolePermissionsApi.md#set_resource_scoped_role_permissions) | **PUT** /resources/{resource_id}/scoped-role-permissions | 


# **get_resource_scoped_role_permissions**
> ScopedRolePermissionList get_resource_scoped_role_permissions(resource_id)



Returns all the scoped role permissions that apply to the given resource. Only OPAL_SCOPED_ROLE resource type supports this field.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.scoped_role_permission_list import ScopedRolePermissionList
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
    api_instance = opal_security.ScopedRolePermissionsApi(api_client)
    resource_id = '1b978423-db0a-4037-a4cf-f79c60cb67b3' # str | The ID of the resource whose scoped role permissions belong to.

    try:
        api_response = api_instance.get_resource_scoped_role_permissions(resource_id)
        print("The response of ScopedRolePermissionsApi->get_resource_scoped_role_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScopedRolePermissionsApi->get_resource_scoped_role_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource whose scoped role permissions belong to. | 

### Return type

[**ScopedRolePermissionList**](ScopedRolePermissionList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The role permissions that this Opal Scoped Role has. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_resource_scoped_role_permissions**
> ScopedRolePermissionList set_resource_scoped_role_permissions(resource_id, scoped_role_permission_list)



Sets all the scoped role permissions on an OPAL_SCOPED_ROLE resource.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.scoped_role_permission_list import ScopedRolePermissionList
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
    api_instance = opal_security.ScopedRolePermissionsApi(api_client)
    resource_id = '1b978423-db0a-4037-a4cf-f79c60cb67b3' # str | The ID of the resource whose scoped role permissions belong to. Must be of OPAL_SCOPED_ROLE resource type.
    scoped_role_permission_list = opal_security.ScopedRolePermissionList() # ScopedRolePermissionList | 

    try:
        api_response = api_instance.set_resource_scoped_role_permissions(resource_id, scoped_role_permission_list)
        print("The response of ScopedRolePermissionsApi->set_resource_scoped_role_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScopedRolePermissionsApi->set_resource_scoped_role_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The ID of the resource whose scoped role permissions belong to. Must be of OPAL_SCOPED_ROLE resource type. | 
 **scoped_role_permission_list** | [**ScopedRolePermissionList**](ScopedRolePermissionList.md)|  | 

### Return type

[**ScopedRolePermissionList**](ScopedRolePermissionList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The role permissions that this Opal Scoped Role has. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

