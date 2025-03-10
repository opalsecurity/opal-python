# opal_security.ComingSoonApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bundle**](ComingSoonApi.md#create_bundle) | **POST** /experimental/bundles | 
[**delete_bundle**](ComingSoonApi.md#delete_bundle) | **DELETE** /experimental/bundles/{bundle_id} | 
[**get_bundle**](ComingSoonApi.md#get_bundle) | **GET** /experimental/bundles/{bundle_id} | 
[**get_bundles**](ComingSoonApi.md#get_bundles) | **GET** /experimental/bundles | 


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
    api_instance = opal_security.ComingSoonApi(api_client)
    create_bundle_info = opal_security.CreateBundleInfo() # CreateBundleInfo | 

    try:
        api_response = api_instance.create_bundle(create_bundle_info)
        print("The response of ComingSoonApi->create_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComingSoonApi->create_bundle: %s\n" % e)
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
    api_instance = opal_security.ComingSoonApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.

    try:
        api_instance.delete_bundle(bundle_id)
    except Exception as e:
        print("Exception when calling ComingSoonApi->delete_bundle: %s\n" % e)
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
**204** | The bundle was successfully deleted. |  -  |

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
    api_instance = opal_security.ComingSoonApi(api_client)
    bundle_id = '32acc112-21ff-4669-91c2-21e27683eaa1' # str | The ID of the bundle.

    try:
        api_response = api_instance.get_bundle(bundle_id)
        print("The response of ComingSoonApi->get_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComingSoonApi->get_bundle: %s\n" % e)
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
    api_instance = opal_security.ComingSoonApi(api_client)
    page_size = 200 # int | The maximum number of bundles to return from the beginning of the list. Default is 200, max is 1000. (optional)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | A cursor indicating where to start fetching items after a specific point. (optional)
    contains = 'Engineering' # str | A filter for the bundle name. (optional)

    try:
        api_response = api_instance.get_bundles(page_size=page_size, cursor=cursor, contains=contains)
        print("The response of ComingSoonApi->get_bundles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComingSoonApi->get_bundles: %s\n" % e)
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

