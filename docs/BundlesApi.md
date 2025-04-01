# opal_security.BundlesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bundle_group**](BundlesApi.md#add_bundle_group) | **POST** /bundles/{bundle_id}/groups | 
[**add_bundle_resource**](BundlesApi.md#add_bundle_resource) | **POST** /bundles/{bundle_id}/resources | 
[**create_bundle**](BundlesApi.md#create_bundle) | **POST** /bundles | 
[**delete_bundle**](BundlesApi.md#delete_bundle) | **DELETE** /bundles/{bundle_id} | 
[**get_bundle**](BundlesApi.md#get_bundle) | **GET** /bundles/{bundle_id} | 
[**get_bundle_groups**](BundlesApi.md#get_bundle_groups) | **GET** /bundles/{bundle_id}/groups | 
[**get_bundle_resources**](BundlesApi.md#get_bundle_resources) | **GET** /bundles/{bundle_id}/resources | 
[**get_bundle_visibility**](BundlesApi.md#get_bundle_visibility) | **GET** /bundles/{bundle_id}/visibility | 
[**get_bundles**](BundlesApi.md#get_bundles) | **GET** /bundles | 
[**remove_bundle_group**](BundlesApi.md#remove_bundle_group) | **DELETE** /bundles/{bundle_id}/groups/{group_id} | 
[**remove_bundle_resource**](BundlesApi.md#remove_bundle_resource) | **DELETE** /bundles/{bundle_id}/resources/{resource_id} | 
[**set_bundle_visibility**](BundlesApi.md#set_bundle_visibility) | **PUT** /bundles/{bundle_id}/visibility | 
[**update_bundle**](BundlesApi.md#update_bundle) | **PUT** /bundles/{bundle_id} | 


# **add_bundle_group**
> BundleGroup add_bundle_group(bundle_id, add_bundle_group_request)

Adds a group to a bundle.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.add_bundle_group_request import AddBundleGroupRequest
from opal_security.models.bundle_group import BundleGroup
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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.
    add_bundle_group_request = opal_security.AddBundleGroupRequest() # AddBundleGroupRequest | 

    try:
        api_response = api_instance.add_bundle_group(bundle_id, add_bundle_group_request)
        print("The response of BundlesApi->add_bundle_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->add_bundle_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle. | 
 **add_bundle_group_request** | [**AddBundleGroupRequest**](AddBundleGroupRequest.md)|  | 

### Return type

[**BundleGroup**](BundleGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Group was successfully added to the bundle. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bundle_resource**
> BundleResource add_bundle_resource(bundle_id, add_bundle_resource_request=add_bundle_resource_request)

Adds a resource to a bundle.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.add_bundle_resource_request import AddBundleResourceRequest
from opal_security.models.bundle_resource import BundleResource
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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.
    add_bundle_resource_request = opal_security.AddBundleResourceRequest() # AddBundleResourceRequest |  (optional)

    try:
        api_response = api_instance.add_bundle_resource(bundle_id, add_bundle_resource_request=add_bundle_resource_request)
        print("The response of BundlesApi->add_bundle_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->add_bundle_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle. | 
 **add_bundle_resource_request** | [**AddBundleResourceRequest**](AddBundleResourceRequest.md)|  | [optional] 

### Return type

[**BundleResource**](BundleResource.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource was successfully added to the bundle. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bundle**
> Bundle create_bundle(create_bundle_info)

Creates a bundle.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.bundle import Bundle
from opal_security.models.create_bundle_info import CreateBundleInfo
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
    api_instance = opal_security.BundlesApi(api_client)
    create_bundle_info = opal_security.CreateBundleInfo() # CreateBundleInfo | 

    try:
        api_response = api_instance.create_bundle(create_bundle_info)
        print("The response of BundlesApi->create_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->create_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bundle_info** | [**CreateBundleInfo**](CreateBundleInfo.md)|  | 

### Return type

[**Bundle**](Bundle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The bundle successfully created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bundle**
> delete_bundle(bundle_id)

Deletes a bundle.

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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.

    try:
        api_instance.delete_bundle(bundle_id)
    except Exception as e:
        print("Exception when calling BundlesApi->delete_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle. | 

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
**200** | The bundle was successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle**
> Bundle get_bundle(bundle_id)

Returns a `Bundle` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.bundle import Bundle
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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.

    try:
        api_response = api_instance.get_bundle(bundle_id)
        print("The response of BundlesApi->get_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->get_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle. | 

### Return type

[**Bundle**](Bundle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested &#x60;Bundle&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_groups**
> PaginatedBundleGroupList get_bundle_groups(bundle_id, page_size=page_size, cursor=cursor)

Returns a list of `Group` objects in a given bundle.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_bundle_group_list import PaginatedBundleGroupList
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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.
    page_size = 200 # int | The maximum number of groups to return from the beginning of the list. Default is 200, max is 1000. (optional)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | A cursor indicating where to start fetching items after a specific point. (optional)

    try:
        api_response = api_instance.get_bundle_groups(bundle_id, page_size=page_size, cursor=cursor)
        print("The response of BundlesApi->get_bundle_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->get_bundle_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle. | 
 **page_size** | **int**| The maximum number of groups to return from the beginning of the list. Default is 200, max is 1000. | [optional] 
 **cursor** | **str**| A cursor indicating where to start fetching items after a specific point. | [optional] 

### Return type

[**PaginatedBundleGroupList**](PaginatedBundleGroupList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of groups for the bundle. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_resources**
> PaginatedBundleResourceList get_bundle_resources(bundle_id, page_size=page_size, cursor=cursor)

Returns a list of `Resource` objects in a given bundle.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_bundle_resource_list import PaginatedBundleResourceList
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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.
    page_size = 200 # int | The maximum number of resources to return from the beginning of the list. Default is 200, max is 1000. (optional)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | A cursor indicating where to start fetching items after a specific point. (optional)

    try:
        api_response = api_instance.get_bundle_resources(bundle_id, page_size=page_size, cursor=cursor)
        print("The response of BundlesApi->get_bundle_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->get_bundle_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle. | 
 **page_size** | **int**| The maximum number of resources to return from the beginning of the list. Default is 200, max is 1000. | [optional] 
 **cursor** | **str**| A cursor indicating where to start fetching items after a specific point. | [optional] 

### Return type

[**PaginatedBundleResourceList**](PaginatedBundleResourceList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resources for the bundle. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_visibility**
> VisibilityInfo get_bundle_visibility(bundle_id)

Gets the visibility of the bundle.

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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.

    try:
        api_response = api_instance.get_bundle_visibility(bundle_id)
        print("The response of BundlesApi->get_bundle_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->get_bundle_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle. | 

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
**200** | The visibility details of a bundle. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundles**
> PaginatedBundleList get_bundles(page_size=page_size, cursor=cursor, contains=contains)

Returns a list of `Bundle` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_bundle_list import PaginatedBundleList
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
    api_instance = opal_security.BundlesApi(api_client)
    page_size = 200 # int | The maximum number of bundles to return from the beginning of the list. Default is 200, max is 1000. (optional)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | A cursor indicating where to start fetching items after a specific point. (optional)
    contains = 'Engineering' # str | A filter for the bundle name. (optional)

    try:
        api_response = api_instance.get_bundles(page_size=page_size, cursor=cursor, contains=contains)
        print("The response of BundlesApi->get_bundles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->get_bundles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The maximum number of bundles to return from the beginning of the list. Default is 200, max is 1000. | [optional] 
 **cursor** | **str**| A cursor indicating where to start fetching items after a specific point. | [optional] 
 **contains** | **str**| A filter for the bundle name. | [optional] 

### Return type

[**PaginatedBundleList**](PaginatedBundleList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of bundles for your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_bundle_group**
> remove_bundle_group(bundle_id, group_id)

Removes a group from a bundle.

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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.
    group_id = '72e75a6f-7183-48c5-94ff-6013f213314b' # str | The ID of the group to remove.

    try:
        api_instance.remove_bundle_group(bundle_id, group_id)
    except Exception as e:
        print("Exception when calling BundlesApi->remove_bundle_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle. | 
 **group_id** | **str**| The ID of the group to remove. | 

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
**200** | Group was successfully removed from the bundle. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_bundle_resource**
> remove_bundle_resource(bundle_id, resource_id, access_level_remote_id=access_level_remote_id)

Removes a resource from a bundle.

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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.
    resource_id = '72e75a6f-7183-48c5-94ff-6013f213314b' # str | The ID of the resource to remove.
    access_level_remote_id = 'arn:aws:iam::590304332660:role/AdministratorAccess' # str | The remote ID of the access level to grant. If omitted, the default access level remote ID value (empty string) is used. (optional)

    try:
        api_instance.remove_bundle_resource(bundle_id, resource_id, access_level_remote_id=access_level_remote_id)
    except Exception as e:
        print("Exception when calling BundlesApi->remove_bundle_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle. | 
 **resource_id** | **str**| The ID of the resource to remove. | 
 **access_level_remote_id** | **str**| The remote ID of the access level to grant. If omitted, the default access level remote ID value (empty string) is used. | [optional] 

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
**200** | Resource was successfully removed from the bundle. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_bundle_visibility**
> set_bundle_visibility(bundle_id, visibility_info)

Sets the visibility of the bundle.

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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.
    visibility_info = opal_security.VisibilityInfo() # VisibilityInfo | 

    try:
        api_instance.set_bundle_visibility(bundle_id, visibility_info)
    except Exception as e:
        print("Exception when calling BundlesApi->set_bundle_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle. | 
 **visibility_info** | [**VisibilityInfo**](VisibilityInfo.md)|  | 

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
**200** | The visibility details of the bundle were successfully set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bundle**
> Bundle update_bundle(bundle_id, bundle)

Updates a bundle.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.bundle import Bundle
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
    api_instance = opal_security.BundlesApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle to be updated.
    bundle = opal_security.Bundle() # Bundle | 

    try:
        api_response = api_instance.update_bundle(bundle_id, bundle)
        print("The response of BundlesApi->update_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->update_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle to be updated. | 
 **bundle** | [**Bundle**](Bundle.md)|  | 

### Return type

[**Bundle**](Bundle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The bundle was successfully updated. |  -  |
**204** | No changes detected (no-op) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

