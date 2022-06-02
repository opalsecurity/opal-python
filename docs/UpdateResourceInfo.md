# UpdateResourceInfo

# UpdateResourceInfo Object ### Description The `UpdateResourceInfo` object is used as an input to the UpdateResource API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource. | 
**name** | **str** | The name of the resource. | [optional] 
**description** | **str** | A description of the resource. | [optional] 
**owner_team_id** | **str** | The ID of the owning team of the resource. | [optional] 
**visibility** | [**VisibilityEnum**](VisibilityEnum.md) |  | [optional] 
**max_duration** | **int** | The maximum duration access to the resource can be requested for (in minutes). Use 0 to set to indefinite. | [optional] 
**require_manager_approval** | **bool** | A bool representing whether or not access requests to the resource require manager approval. | [optional] 
**require_support_ticket** | **bool** | A bool representing whether or not access requests to the resource require a support ticket. | [optional] 
**folder_id** | **str** | The ID of the folder that the resource is located in. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


