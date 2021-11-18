# ResourceAccessLevel

# Access Level Object ### Description The `ResourceAccessLevel` object is used to represent the level of access that a user has to a resource or a resource has to a group. The \"default\" access level is a `ResourceAccessLevel` object whose fields are all empty strings.  ### Usage Example View the `ResourceAccessLevel` of a resource/user or resource/group pair to see the level of access granted to the resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level_name** | **str** | The human-readable name of the access level. | 
**access_level_remote_id** | **str** | The machine-readable identifier of the access level. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


