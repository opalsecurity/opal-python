# opal_security.OpalScriptsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_opal_script**](OpalScriptsApi.md#create_opal_script) | **POST** /opal-scripts | Create OpalScript
[**delete_opal_script**](OpalScriptsApi.md#delete_opal_script) | **DELETE** /opal-scripts/{opal_script_id} | Delete OpalScript
[**get_opal_script**](OpalScriptsApi.md#get_opal_script) | **GET** /opal-scripts/{opal_script_id} | Get OpalScript by ID
[**get_opal_script_from_name**](OpalScriptsApi.md#get_opal_script_from_name) | **GET** /opal-scripts/name/{opal_script_name} | Get OpalScript by name
[**get_opal_scripts**](OpalScriptsApi.md#get_opal_scripts) | **GET** /opal-scripts | List OpalScripts
[**update_opal_script**](OpalScriptsApi.md#update_opal_script) | **PUT** /opal-scripts/{opal_script_id} | Update OpalScript


# **create_opal_script**
> OpalScript create_opal_script(create_opal_script_info)

Create OpalScript

Creates a new `OpalScript`.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_opal_script_info import CreateOpalScriptInfo
from opal_security.models.opal_script import OpalScript
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
    api_instance = opal_security.OpalScriptsApi(api_client)
    create_opal_script_info = opal_security.CreateOpalScriptInfo() # CreateOpalScriptInfo | 

    try:
        # Create OpalScript
        api_response = api_instance.create_opal_script(create_opal_script_info)
        print("The response of OpalScriptsApi->create_opal_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpalScriptsApi->create_opal_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_opal_script_info** | [**CreateOpalScriptInfo**](CreateOpalScriptInfo.md)|  | 

### Return type

[**OpalScript**](OpalScript.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created OpalScript. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_opal_script**
> delete_opal_script(opal_script_id)

Delete OpalScript

Deletes an `OpalScript`, along with the service user that backs it. A script that is still named as a reviewer, or referenced by a delegation, is rejected until those references are removed.

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
    api_instance = opal_security.OpalScriptsApi(api_client)
    opal_script_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the OpalScript.

    try:
        # Delete OpalScript
        api_instance.delete_opal_script(opal_script_id)
    except Exception as e:
        print("Exception when calling OpalScriptsApi->delete_opal_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opal_script_id** | **UUID**| The ID of the OpalScript. | 

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
**200** | The OpalScript was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_opal_script**
> OpalScript get_opal_script(opal_script_id)

Get OpalScript by ID

Returns an `OpalScript` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.opal_script import OpalScript
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
    api_instance = opal_security.OpalScriptsApi(api_client)
    opal_script_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the OpalScript.

    try:
        # Get OpalScript by ID
        api_response = api_instance.get_opal_script(opal_script_id)
        print("The response of OpalScriptsApi->get_opal_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpalScriptsApi->get_opal_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opal_script_id** | **UUID**| The ID of the OpalScript. | 

### Return type

[**OpalScript**](OpalScript.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The OpalScript associated with the passed-in ID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_opal_script_from_name**
> OpalScript get_opal_script_from_name(opal_script_name)

Get OpalScript by name

Returns the `OpalScript` whose name exactly matches the given name. OpalScript names are not unique; when more than one script matches, the request fails and the script must be referenced by ID instead.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.opal_script import OpalScript
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
    api_instance = opal_security.OpalScriptsApi(api_client)
    opal_script_name = 'MFA check' # str | The name of the OpalScript.

    try:
        # Get OpalScript by name
        api_response = api_instance.get_opal_script_from_name(opal_script_name)
        print("The response of OpalScriptsApi->get_opal_script_from_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpalScriptsApi->get_opal_script_from_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opal_script_name** | **str**| The name of the OpalScript. | 

### Return type

[**OpalScript**](OpalScript.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The OpalScript associated with the passed-in name. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_opal_scripts**
> OpalScriptList get_opal_scripts()

List OpalScripts

Returns the `OpalScript` objects in the caller's organization.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.opal_script_list import OpalScriptList
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
    api_instance = opal_security.OpalScriptsApi(api_client)

    try:
        # List OpalScripts
        api_response = api_instance.get_opal_scripts()
        print("The response of OpalScriptsApi->get_opal_scripts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpalScriptsApi->get_opal_scripts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpalScriptList**](OpalScriptList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The OpalScripts in the organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_opal_script**
> OpalScript update_opal_script(opal_script_id, update_opal_script_info)

Update OpalScript

Updates an `OpalScript` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.opal_script import OpalScript
from opal_security.models.update_opal_script_info import UpdateOpalScriptInfo
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
    api_instance = opal_security.OpalScriptsApi(api_client)
    opal_script_id = UUID('32acc112-21ff-4669-91c2-21e27683eaa1') # UUID | The ID of the OpalScript.
    update_opal_script_info = opal_security.UpdateOpalScriptInfo() # UpdateOpalScriptInfo | 

    try:
        # Update OpalScript
        api_response = api_instance.update_opal_script(opal_script_id, update_opal_script_info)
        print("The response of OpalScriptsApi->update_opal_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpalScriptsApi->update_opal_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opal_script_id** | **UUID**| The ID of the OpalScript. | 
 **update_opal_script_info** | [**UpdateOpalScriptInfo**](UpdateOpalScriptInfo.md)|  | 

### Return type

[**OpalScript**](OpalScript.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated OpalScript. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

