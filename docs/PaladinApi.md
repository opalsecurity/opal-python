# opal_security.PaladinApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_paladin**](PaladinApi.md#create_paladin) | **POST** /paladin | Create Paladin
[**create_paladin_context_source**](PaladinApi.md#create_paladin_context_source) | **POST** /paladin/{paladin_id}/context-sources | Add a Paladin context source
[**delete_paladin**](PaladinApi.md#delete_paladin) | **DELETE** /paladin/{paladin_id} | Delete Paladin
[**delete_paladin_context_source**](PaladinApi.md#delete_paladin_context_source) | **DELETE** /paladin/{paladin_id}/context-sources/{context_source_id} | Remove a Paladin context source
[**get_paladin**](PaladinApi.md#get_paladin) | **GET** /paladin/{paladin_id} | Get Paladin by ID
[**get_paladin_from_name**](PaladinApi.md#get_paladin_from_name) | **GET** /paladin/name/{paladin_name} | Get Paladins by name
[**list_paladin_context_sources**](PaladinApi.md#list_paladin_context_sources) | **GET** /paladin/{paladin_id}/context-sources | List Paladin context sources
[**update_paladin**](PaladinApi.md#update_paladin) | **PUT** /paladin/{paladin_id} | Update Paladin


# **create_paladin**
> Paladin create_paladin(create_paladin_info)

Create Paladin

Creates a new `Paladin`.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_paladin_info import CreatePaladinInfo
from opal_security.models.paladin import Paladin
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
    api_instance = opal_security.PaladinApi(api_client)
    create_paladin_info = opal_security.CreatePaladinInfo() # CreatePaladinInfo | 

    try:
        # Create Paladin
        api_response = api_instance.create_paladin(create_paladin_info)
        print("The response of PaladinApi->create_paladin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaladinApi->create_paladin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_paladin_info** | [**CreatePaladinInfo**](CreatePaladinInfo.md)|  | 

### Return type

[**Paladin**](Paladin.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created Paladin. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_paladin_context_source**
> PaladinContextSource create_paladin_context_source(paladin_id, create_paladin_context_source_info)

Add a Paladin context source

Configures a context source (a Slack channel or a document) for a Paladin to read. Idempotent, so re-adding an existing source returns it.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_paladin_context_source_info import CreatePaladinContextSourceInfo
from opal_security.models.paladin_context_source import PaladinContextSource
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
    api_instance = opal_security.PaladinApi(api_client)
    paladin_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the Paladin.
    create_paladin_context_source_info = opal_security.CreatePaladinContextSourceInfo() # CreatePaladinContextSourceInfo | 

    try:
        # Add a Paladin context source
        api_response = api_instance.create_paladin_context_source(paladin_id, create_paladin_context_source_info)
        print("The response of PaladinApi->create_paladin_context_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaladinApi->create_paladin_context_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paladin_id** | **UUID**| The ID of the Paladin. | 
 **create_paladin_context_source_info** | [**CreatePaladinContextSourceInfo**](CreatePaladinContextSourceInfo.md)|  | 

### Return type

[**PaladinContextSource**](PaladinContextSource.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configured context source. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_paladin**
> delete_paladin(paladin_id)

Delete Paladin

Deletes a Paladin, removing the underlying service user.

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
    api_instance = opal_security.PaladinApi(api_client)
    paladin_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the Paladin.

    try:
        # Delete Paladin
        api_instance.delete_paladin(paladin_id)
    except Exception as e:
        print("Exception when calling PaladinApi->delete_paladin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paladin_id** | **UUID**| The ID of the Paladin. | 

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
**200** | The Paladin was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_paladin_context_source**
> delete_paladin_context_source(paladin_id, context_source_id)

Remove a Paladin context source

Removes a context source from a Paladin.

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
    api_instance = opal_security.PaladinApi(api_client)
    paladin_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the Paladin.
    context_source_id = UUID('8a1f2c3d-4b5e-6f70-8192-a3b4c5d6e7f8') # UUID | The ID of the context source.

    try:
        # Remove a Paladin context source
        api_instance.delete_paladin_context_source(paladin_id, context_source_id)
    except Exception as e:
        print("Exception when calling PaladinApi->delete_paladin_context_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paladin_id** | **UUID**| The ID of the Paladin. | 
 **context_source_id** | **UUID**| The ID of the context source. | 

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
**200** | The context source was removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paladin**
> Paladin get_paladin(paladin_id)

Get Paladin by ID

Returns a `Paladin` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paladin import Paladin
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
    api_instance = opal_security.PaladinApi(api_client)
    paladin_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the Paladin.

    try:
        # Get Paladin by ID
        api_response = api_instance.get_paladin(paladin_id)
        print("The response of PaladinApi->get_paladin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaladinApi->get_paladin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paladin_id** | **UUID**| The ID of the Paladin. | 

### Return type

[**Paladin**](Paladin.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Paladin associated with the passed-in ID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paladin_from_name**
> PaladinList get_paladin_from_name(paladin_name)

Get Paladins by name

Returns all Paladins whose name exactly matches the given name. Names are not unique, so the result is a list and may be empty.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paladin_list import PaladinList
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
    api_instance = opal_security.PaladinApi(api_client)
    paladin_name = 'paladin-agent-1' # str | The name of the Paladin.

    try:
        # Get Paladins by name
        api_response = api_instance.get_paladin_from_name(paladin_name)
        print("The response of PaladinApi->get_paladin_from_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaladinApi->get_paladin_from_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paladin_name** | **str**| The name of the Paladin. | 

### Return type

[**PaladinList**](PaladinList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of Paladins matching the passed-in name. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_paladin_context_sources**
> PaladinContextSourceList list_paladin_context_sources(paladin_id)

List Paladin context sources

Returns the context sources (Slack channels and documents) configured for a Paladin.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paladin_context_source_list import PaladinContextSourceList
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
    api_instance = opal_security.PaladinApi(api_client)
    paladin_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the Paladin.

    try:
        # List Paladin context sources
        api_response = api_instance.list_paladin_context_sources(paladin_id)
        print("The response of PaladinApi->list_paladin_context_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaladinApi->list_paladin_context_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paladin_id** | **UUID**| The ID of the Paladin. | 

### Return type

[**PaladinContextSourceList**](PaladinContextSourceList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The context sources configured for the Paladin. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_paladin**
> Paladin update_paladin(paladin_id, update_paladin_info)

Update Paladin

Updates a `Paladin` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paladin import Paladin
from opal_security.models.update_paladin_info import UpdatePaladinInfo
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
    api_instance = opal_security.PaladinApi(api_client)
    paladin_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the Paladin.
    update_paladin_info = opal_security.UpdatePaladinInfo() # UpdatePaladinInfo | 

    try:
        # Update Paladin
        api_response = api_instance.update_paladin(paladin_id, update_paladin_info)
        print("The response of PaladinApi->update_paladin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaladinApi->update_paladin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paladin_id** | **UUID**| The ID of the Paladin. | 
 **update_paladin_info** | [**UpdatePaladinInfo**](UpdatePaladinInfo.md)|  | 

### Return type

[**Paladin**](Paladin.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Paladin. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

