# Session

# Session Object ### Description The `Session` object is used to represent an access session. Some resources can be accessed temporarily via a time-bounded session.  ### Usage Example Fetch from the `LIST Sessions` endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | The ID of the connection. | 
**user_id** | **str** | The ID of the user. | 
**resource_id** | **str** | The ID of the resource. | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | 
**expiration_date** | **datetime** | The day and time the user&#39;s access will expire. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


