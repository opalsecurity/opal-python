# opal_security.CampaignsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign**](CampaignsApi.md#create_campaign) | **POST** /campaigns | 
[**end_campaign**](CampaignsApi.md#end_campaign) | **POST** /campaigns/{campaign_id}/end | End campaign
[**get_campaign**](CampaignsApi.md#get_campaign) | **GET** /campaigns/{campaign_id} | Get campaign by ID
[**get_campaigns**](CampaignsApi.md#get_campaigns) | **GET** /campaigns | 
[**start_campaign**](CampaignsApi.md#start_campaign) | **POST** /campaigns/{campaign_id}/start | Start campaign
[**stop_campaign**](CampaignsApi.md#stop_campaign) | **POST** /campaigns/{campaign_id}/stop | Stop campaign
[**update_campaign**](CampaignsApi.md#update_campaign) | **PUT** /campaigns/{campaign_id} | Update campaign


# **create_campaign**
> Campaign create_campaign(create_campaign_info)

Creates a campaign. Campaign scope only supports direct access edges:
`configuration.query.edgeFilter.directOnly` defaults to `true`, is
always stored as `true`, and passing `false` returns 400.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.campaign import Campaign
from opal_security.models.create_campaign_info import CreateCampaignInfo
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
    api_instance = opal_security.CampaignsApi(api_client)
    create_campaign_info = opal_security.CreateCampaignInfo() # CreateCampaignInfo | 

    try:
        api_response = api_instance.create_campaign(create_campaign_info)
        print("The response of CampaignsApi->create_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->create_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_campaign_info** | [**CreateCampaignInfo**](CreateCampaignInfo.md)|  | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The campaign successfully created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_campaign**
> Campaign end_campaign(campaign_id)

End campaign

Ends a stopped campaign, setting `ended_at` and `ended_by_user_id`,
applying pending access changes, and queuing report generation.
Returns 400 unless the campaign is started and stopped and not already
ended.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.campaign import Campaign
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
    api_instance = opal_security.CampaignsApi(api_client)
    campaign_id = UUID('f454d283-ca87-4a8a-bdbb-df212eca5353') # UUID | The ID of the campaign.

    try:
        # End campaign
        api_response = api_instance.end_campaign(campaign_id)
        print("The response of CampaignsApi->end_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->end_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **UUID**| The ID of the campaign. | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ended &#x60;Campaign&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign**
> Campaign get_campaign(campaign_id)

Get campaign by ID

Returns a `Campaign` object.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.campaign import Campaign
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
    api_instance = opal_security.CampaignsApi(api_client)
    campaign_id = UUID('f454d283-ca87-4a8a-bdbb-df212eca5353') # UUID | The ID of the campaign.

    try:
        # Get campaign by ID
        api_response = api_instance.get_campaign(campaign_id)
        print("The response of CampaignsApi->get_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **UUID**| The ID of the campaign. | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested &#x60;Campaign&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaigns**
> PaginatedCampaignsList get_campaigns(cursor=cursor, page_size=page_size, name=name, status=status, created_at_after=created_at_after, created_at_before=created_at_before, started_at_after=started_at_after, started_at_before=started_at_before, ended_at_after=ended_at_after, ended_at_before=ended_at_before, stopped_at_after=stopped_at_after, stopped_at_before=stopped_at_before)

Returns a list of `Campaign` objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.campaign_status_enum import CampaignStatusEnum
from opal_security.models.paginated_campaigns_list import PaginatedCampaignsList
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
    api_instance = opal_security.CampaignsApi(api_client)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)
    name = 'Q3 Access Review' # str | Campaign name to filter by. Returns campaigns whose names contain this substring (case-insensitive). (optional)
    status = opal_security.CampaignStatusEnum() # CampaignStatusEnum | Filter by campaign status. Status is derived from lifecycle timestamps and review progress. (optional)
    created_at_after = '2026-01-01T00:00:00Z' # datetime | Include campaigns created after this timestamp (exclusive). ISO 8601 format. (optional)
    created_at_before = '2026-12-31T23:59:59Z' # datetime | Include campaigns created before this timestamp (exclusive). ISO 8601 format. (optional)
    started_at_after = '2026-01-01T00:00:00Z' # datetime | Include campaigns started after this timestamp (exclusive). ISO 8601 format. (optional)
    started_at_before = '2026-12-31T23:59:59Z' # datetime | Include campaigns started before this timestamp (exclusive). ISO 8601 format. (optional)
    ended_at_after = '2026-01-01T00:00:00Z' # datetime | Include campaigns ended after this timestamp (exclusive). ISO 8601 format. (optional)
    ended_at_before = '2026-12-31T23:59:59Z' # datetime | Include campaigns ended before this timestamp (exclusive). ISO 8601 format. (optional)
    stopped_at_after = '2026-01-01T00:00:00Z' # datetime | Include campaigns stopped after this timestamp (exclusive). ISO 8601 format. (optional)
    stopped_at_before = '2026-12-31T23:59:59Z' # datetime | Include campaigns stopped before this timestamp (exclusive). ISO 8601 format. (optional)

    try:
        api_response = api_instance.get_campaigns(cursor=cursor, page_size=page_size, name=name, status=status, created_at_after=created_at_after, created_at_before=created_at_before, started_at_after=started_at_after, started_at_before=started_at_before, ended_at_after=ended_at_after, ended_at_before=ended_at_before, stopped_at_after=stopped_at_after, stopped_at_before=stopped_at_before)
        print("The response of CampaignsApi->get_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 
 **name** | **str**| Campaign name to filter by. Returns campaigns whose names contain this substring (case-insensitive). | [optional] 
 **status** | [**CampaignStatusEnum**](.md)| Filter by campaign status. Status is derived from lifecycle timestamps and review progress. | [optional] 
 **created_at_after** | **datetime**| Include campaigns created after this timestamp (exclusive). ISO 8601 format. | [optional] 
 **created_at_before** | **datetime**| Include campaigns created before this timestamp (exclusive). ISO 8601 format. | [optional] 
 **started_at_after** | **datetime**| Include campaigns started after this timestamp (exclusive). ISO 8601 format. | [optional] 
 **started_at_before** | **datetime**| Include campaigns started before this timestamp (exclusive). ISO 8601 format. | [optional] 
 **ended_at_after** | **datetime**| Include campaigns ended after this timestamp (exclusive). ISO 8601 format. | [optional] 
 **ended_at_before** | **datetime**| Include campaigns ended before this timestamp (exclusive). ISO 8601 format. | [optional] 
 **stopped_at_after** | **datetime**| Include campaigns stopped after this timestamp (exclusive). ISO 8601 format. | [optional] 
 **stopped_at_before** | **datetime**| Include campaigns stopped before this timestamp (exclusive). ISO 8601 format. | [optional] 

### Return type

[**PaginatedCampaignsList**](PaginatedCampaignsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of campaigns for your organization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_campaign**
> Campaign start_campaign(campaign_id)

Start campaign

Starts a draft campaign immediately, setting `started_at` and
`started_by_user_id`. Returns 400 if the campaign is not in draft
state, or if it is a recurring template (`is_template: true`) —
templates spawn draft campaigns on their schedule and cannot be
started directly.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.campaign import Campaign
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
    api_instance = opal_security.CampaignsApi(api_client)
    campaign_id = UUID('f454d283-ca87-4a8a-bdbb-df212eca5353') # UUID | The ID of the campaign.

    try:
        # Start campaign
        api_response = api_instance.start_campaign(campaign_id)
        print("The response of CampaignsApi->start_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->start_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **UUID**| The ID of the campaign. | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The started &#x60;Campaign&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_campaign**
> Campaign stop_campaign(campaign_id, stop_campaign_request=stop_campaign_request)

Stop campaign

Stops an ongoing campaign immediately, setting `stopped_at` and
`stopped_by_user_id`. Returns 400 if the campaign has not started or
has already stopped.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.campaign import Campaign
from opal_security.models.stop_campaign_request import StopCampaignRequest
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
    api_instance = opal_security.CampaignsApi(api_client)
    campaign_id = UUID('f454d283-ca87-4a8a-bdbb-df212eca5353') # UUID | The ID of the campaign.
    stop_campaign_request = opal_security.StopCampaignRequest() # StopCampaignRequest |  (optional)

    try:
        # Stop campaign
        api_response = api_instance.stop_campaign(campaign_id, stop_campaign_request=stop_campaign_request)
        print("The response of CampaignsApi->stop_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->stop_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **UUID**| The ID of the campaign. | 
 **stop_campaign_request** | [**StopCampaignRequest**](StopCampaignRequest.md)|  | [optional] 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stopped &#x60;Campaign&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign**
> Campaign update_campaign(campaign_id, update_campaign_info)

Update campaign

Partially updates a campaign. Omitted fields are left unchanged.
`configuration.query` and `configuration.reviewer_assignment_policy`
cannot be updated after create; including either field returns 400.
`configuration.cron_expression` and
`configuration.recurring_duration_days` may only be set on template
campaigns; setting them on a one-off campaign returns 400.
`configuration.is_template` is immutable and not accepted on update.
Configuration updates on a stopped or ended (non-template) campaign
return 400. Name-only updates are still allowed.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.campaign import Campaign
from opal_security.models.update_campaign_info import UpdateCampaignInfo
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
    api_instance = opal_security.CampaignsApi(api_client)
    campaign_id = UUID('f454d283-ca87-4a8a-bdbb-df212eca5353') # UUID | The ID of the campaign.
    update_campaign_info = opal_security.UpdateCampaignInfo() # UpdateCampaignInfo | 

    try:
        # Update campaign
        api_response = api_instance.update_campaign(campaign_id, update_campaign_info)
        print("The response of CampaignsApi->update_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->update_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **UUID**| The ID of the campaign. | 
 **update_campaign_info** | [**UpdateCampaignInfo**](UpdateCampaignInfo.md)|  | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated &#x60;Campaign&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

