# ResourceUser

# Resource User Object ### Description The `ResourceUser` object is used to represent a user with access to a resource.  ### Usage Example Fetch from the `LIST ResourceUsers` endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource. | 
**user_id** | **str** | The ID of the user. | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | 
**full_name** | **str** | The user&#39;s full name. | 
**email** | **str** | The user&#39;s email. | 
**expiration_date** | **datetime, none_type** | The day and time the user&#39;s access will expire. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


