# ResourceUserAccessStatus

# AccessStatus Object ### Description The `AccessStatus` object is used to represent the user's access to the resource.  ### Usage Example View the `AccessStatus` for a resource/user pair to determine if the user has access to the resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource. | 
**user_id** | **str** | The ID of the user. | 
**status** | [**ResourceUserAccessStatusEnum**](ResourceUserAccessStatusEnum.md) |  | 
**expiration_date** | **datetime, none_type** | The day and time the user&#39;s access will expire. | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


