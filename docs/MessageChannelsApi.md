# opal_security.MessageChannelsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_message_channel**](MessageChannelsApi.md#create_message_channel) | **POST** /message-channels | 
[**get_message_channel**](MessageChannelsApi.md#get_message_channel) | **GET** /message-channels/{message_channel_id} | 
[**get_message_channels**](MessageChannelsApi.md#get_message_channels) | **GET** /message-channels | 


# **create_message_channel**
> MessageChannel create_message_channel(create_message_channel_info)

Creates a `MessageChannel` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.create_message_channel_info import CreateMessageChannelInfo
from opal_security.models.message_channel import MessageChannel
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
    api_instance = opal_security.MessageChannelsApi(api_client)
    create_message_channel_info = opal_security.CreateMessageChannelInfo() # CreateMessageChannelInfo | The `MessageChannel` object to be created.

    try:
        api_response = api_instance.create_message_channel(create_message_channel_info)
        print("The response of MessageChannelsApi->create_message_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageChannelsApi->create_message_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_message_channel_info** | [**CreateMessageChannelInfo**](CreateMessageChannelInfo.md)| The &#x60;MessageChannel&#x60; object to be created. | 

### Return type

[**MessageChannel**](MessageChannel.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The message channel that was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_channel**
> MessageChannel get_message_channel(message_channel_id)

Gets a `MessageChannel` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.message_channel import MessageChannel
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
    api_instance = opal_security.MessageChannelsApi(api_client)
    message_channel_id = '4baf8423-db0a-4037-a4cf-f79c60cb67a5' # str | The ID of the message_channel.

    try:
        api_response = api_instance.get_message_channel(message_channel_id)
        print("The response of MessageChannelsApi->get_message_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageChannelsApi->get_message_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_channel_id** | **str**| The ID of the message_channel. | 

### Return type

[**MessageChannel**](MessageChannel.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested message channel. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_channels**
> MessageChannelList get_message_channels()

Returns a list of `MessageChannel` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.message_channel_list import MessageChannelList
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
    api_instance = opal_security.MessageChannelsApi(api_client)

    try:
        api_response = api_instance.get_message_channels()
        print("The response of MessageChannelsApi->get_message_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageChannelsApi->get_message_channels: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MessageChannelList**](MessageChannelList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of message channels for your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

