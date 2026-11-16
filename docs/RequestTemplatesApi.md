# opal_security.RequestTemplatesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_request_template**](RequestTemplatesApi.md#create_request_template) | **POST** /request-templates | 
[**delete_request_template**](RequestTemplatesApi.md#delete_request_template) | **DELETE** /request-templates/{request_template_id} | 
[**get_request_template**](RequestTemplatesApi.md#get_request_template) | **GET** /request-templates/{request_template_id} | 
[**get_request_templates**](RequestTemplatesApi.md#get_request_templates) | **GET** /request-templates | 
[**update_request_template**](RequestTemplatesApi.md#update_request_template) | **PUT** /request-templates | 


# **create_request_template**
> RequestTemplate create_request_template(create_request_template_info)

Creates a request template.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_request_template_info import CreateRequestTemplateInfo
from opal_security.models.request_template import RequestTemplate
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
    api_instance = opal_security.RequestTemplatesApi(api_client)
    create_request_template_info = opal_security.CreateRequestTemplateInfo() # CreateRequestTemplateInfo | 

    try:
        api_response = api_instance.create_request_template(create_request_template_info)
        print("The response of RequestTemplatesApi->create_request_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestTemplatesApi->create_request_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request_template_info** | [**CreateRequestTemplateInfo**](CreateRequestTemplateInfo.md)|  | 

### Return type

[**RequestTemplate**](RequestTemplate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request template just created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_request_template**
> delete_request_template(request_template_id)

Deletes a request template.

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
    api_instance = opal_security.RequestTemplatesApi(api_client)
    request_template_id = UUID('4baf8423-db0a-4037-a4cf-f79c60cb67a5') # UUID | The ID of the request template.

    try:
        api_instance.delete_request_template(request_template_id)
    except Exception as e:
        print("Exception when calling RequestTemplatesApi->delete_request_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_template_id** | **UUID**| The ID of the request template. | 

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
**200** | The request template was successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_template**
> RequestTemplate get_request_template(request_template_id)

Returns a `RequestTemplate` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.request_template import RequestTemplate
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
    api_instance = opal_security.RequestTemplatesApi(api_client)
    request_template_id = UUID('4baf8423-db0a-4037-a4cf-f79c60cb67a5') # UUID | The ID of the request template.

    try:
        api_response = api_instance.get_request_template(request_template_id)
        print("The response of RequestTemplatesApi->get_request_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestTemplatesApi->get_request_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_template_id** | **UUID**| The ID of the request template. | 

### Return type

[**RequestTemplate**](RequestTemplate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested request template. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_templates**
> PaginatedRequestTemplateList get_request_templates()

Returns a list of `RequestTemplate` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.paginated_request_template_list import PaginatedRequestTemplateList
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
    api_instance = opal_security.RequestTemplatesApi(api_client)

    try:
        api_response = api_instance.get_request_templates()
        print("The response of RequestTemplatesApi->get_request_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestTemplatesApi->get_request_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaginatedRequestTemplateList**](PaginatedRequestTemplateList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page worth of request templates for your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_request_template**
> RequestTemplate update_request_template(update_request_template_info)

Updates a request template.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.request_template import RequestTemplate
from opal_security.models.update_request_template_info import UpdateRequestTemplateInfo
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
    api_instance = opal_security.RequestTemplatesApi(api_client)
    update_request_template_info = opal_security.UpdateRequestTemplateInfo() # UpdateRequestTemplateInfo | Request template to be updated

    try:
        api_response = api_instance.update_request_template(update_request_template_info)
        print("The response of RequestTemplatesApi->update_request_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestTemplatesApi->update_request_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_request_template_info** | [**UpdateRequestTemplateInfo**](UpdateRequestTemplateInfo.md)| Request template to be updated | 

### Return type

[**RequestTemplate**](RequestTemplate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request template just updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

