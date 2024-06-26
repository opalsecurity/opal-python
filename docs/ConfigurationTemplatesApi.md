# opal.ConfigurationTemplatesApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration_template**](ConfigurationTemplatesApi.md#create_configuration_template) | **POST** /configuration-templates | 
[**get_configuration_templates**](ConfigurationTemplatesApi.md#get_configuration_templates) | **GET** /configuration-templates | 
[**update_configuration_template**](ConfigurationTemplatesApi.md#update_configuration_template) | **PUT** /configuration-templates | 


# **create_configuration_template**
> ConfigurationTemplate create_configuration_template(create_configuration_template_info)



Creates a configuration template.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal
from opal.models.configuration_template import ConfigurationTemplate
from opal.models.create_configuration_template_info import CreateConfigurationTemplateInfo
from opal.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal.ConfigurationTemplatesApi(api_client)
    create_configuration_template_info = opal.CreateConfigurationTemplateInfo() # CreateConfigurationTemplateInfo | 

    try:
        api_response = api_instance.create_configuration_template(create_configuration_template_info)
        print("The response of ConfigurationTemplatesApi->create_configuration_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTemplatesApi->create_configuration_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_configuration_template_info** | [**CreateConfigurationTemplateInfo**](CreateConfigurationTemplateInfo.md)|  | 

### Return type

[**ConfigurationTemplate**](ConfigurationTemplate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration template just created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_templates**
> PaginatedConfigurationTemplateList get_configuration_templates()



Returns a list of `ConfigurationTemplate` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal
from opal.models.paginated_configuration_template_list import PaginatedConfigurationTemplateList
from opal.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal.ConfigurationTemplatesApi(api_client)

    try:
        api_response = api_instance.get_configuration_templates()
        print("The response of ConfigurationTemplatesApi->get_configuration_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTemplatesApi->get_configuration_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaginatedConfigurationTemplateList**](PaginatedConfigurationTemplateList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page worth of configuration templates for your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration_template**
> ConfigurationTemplate update_configuration_template(update_configuration_template_info)



Update a configuration template.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal
from opal.models.configuration_template import ConfigurationTemplate
from opal.models.update_configuration_template_info import UpdateConfigurationTemplateInfo
from opal.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal.ConfigurationTemplatesApi(api_client)
    update_configuration_template_info = opal.UpdateConfigurationTemplateInfo() # UpdateConfigurationTemplateInfo | Configuration template to be updated

    try:
        api_response = api_instance.update_configuration_template(update_configuration_template_info)
        print("The response of ConfigurationTemplatesApi->update_configuration_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTemplatesApi->update_configuration_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_configuration_template_info** | [**UpdateConfigurationTemplateInfo**](UpdateConfigurationTemplateInfo.md)| Configuration template to be updated | 

### Return type

[**ConfigurationTemplate**](ConfigurationTemplate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration template just updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

