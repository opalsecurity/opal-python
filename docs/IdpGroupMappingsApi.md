# opal_security.IdpGroupMappingsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_idp_group_mappings**](IdpGroupMappingsApi.md#delete_idp_group_mappings) | **DELETE** /idp-group-mappings/{app_resource_id}/{group_id}/ | 
[**get_idp_group_mappings**](IdpGroupMappingsApi.md#get_idp_group_mappings) | **GET** /idp-group-mappings/{app_resource_id} | 
[**update_idp_group_mappings**](IdpGroupMappingsApi.md#update_idp_group_mappings) | **PUT** /idp-group-mappings/{app_resource_id} | 


# **delete_idp_group_mappings**
> delete_idp_group_mappings(app_resource_id, group_id)

Deletes an `IdpGroupMapping` object.

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
    api_instance = opal_security.IdpGroupMappingsApi(api_client)
    app_resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the Okta app.
    group_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the group.

    try:
        api_instance.delete_idp_group_mappings(app_resource_id, group_id)
    except Exception as e:
        print("Exception when calling IdpGroupMappingsApi->delete_idp_group_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_resource_id** | **str**| The ID of the Okta app. | 
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
**200** | The IDP group mapping was successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idp_group_mappings**
> IdpGroupMappingList get_idp_group_mappings(app_resource_id)

Returns the configured set of available `IdpGroupMapping` objects for an Okta app.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.idp_group_mapping_list import IdpGroupMappingList
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
    api_instance = opal_security.IdpGroupMappingsApi(api_client)
    app_resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the Okta app.

    try:
        api_response = api_instance.get_idp_group_mappings(app_resource_id)
        print("The response of IdpGroupMappingsApi->get_idp_group_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdpGroupMappingsApi->get_idp_group_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_resource_id** | **str**| The ID of the Okta app. | 

### Return type

[**IdpGroupMappingList**](IdpGroupMappingList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configured set of available &#x60;IdpGroupMapping&#x60; objects for an Okta app. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_idp_group_mappings**
> update_idp_group_mappings(app_resource_id, update_idp_group_mappings_request)

Updates the list of available `IdpGroupMapping` objects for an Okta app.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.update_idp_group_mappings_request import UpdateIdpGroupMappingsRequest
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
    api_instance = opal_security.IdpGroupMappingsApi(api_client)
    app_resource_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the Okta app.
    update_idp_group_mappings_request = opal_security.UpdateIdpGroupMappingsRequest() # UpdateIdpGroupMappingsRequest | 

    try:
        api_instance.update_idp_group_mappings(app_resource_id, update_idp_group_mappings_request)
    except Exception as e:
        print("Exception when calling IdpGroupMappingsApi->update_idp_group_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_resource_id** | **str**| The ID of the Okta app. | 
 **update_idp_group_mappings_request** | [**UpdateIdpGroupMappingsRequest**](UpdateIdpGroupMappingsRequest.md)|  | 

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
**200** | The updated set of available &#x60;IdpGroupMapping&#x60; objects for an Okta app. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

