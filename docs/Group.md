# Group

# Group Object ### Description The `Group` object is used to represent a group.  ### Usage Example Update from the `UPDATE Groups` endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the group. | 
**name** | **str** | The name of the group. | [optional] 
**description** | **str** | A description of the group. | [optional] 
**owner_team_id** | **str** | The ID of the owning team of the group. | [optional] 
**group_function** | [**GroupFunctionEnum**](GroupFunctionEnum.md) |  | [optional] 
**group_type** | [**GroupTypeEnum**](GroupTypeEnum.md) |  | [optional] 
**visibility** | [**VisibilityEnum**](VisibilityEnum.md) |  | [optional] 
**max_duration** | **int** | The maximum duration access to the group can be requested for (in minutes). | [optional] 
**require_manager_approval** | **bool** | A bool representing whether or not access requests to the group require manager approval. | [optional] 
**require_support_ticket** | **bool** | A bool representing whether or not access requests to the group require a support ticket. | [optional] 
**folder_id** | **str** | The ID of the folder that the group is located in. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


