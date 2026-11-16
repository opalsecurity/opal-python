# ResourceCustomAccessLevelResponse

A custom access level for a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_custom_access_level_id** | **UUID** | The unique ID of the custom access level. | 
**resource_id** | **UUID** | The resource this access level belongs to. | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | 
**policy** | **str** | The policy document for this access level. | [optional] 
**requestable_by_default** | **bool** | Whether this role is requestable. | 
**stackable_sensitivity_index** | **int** | The sensitivity index in the access hierarchy. Null if unranked. | [optional] 
**member_resource_ids** | **List[UUID]** | When addressed via a parent resource, lists the child resource IDs that back this aggregated entry. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from opal_security.models.resource_custom_access_level_response import ResourceCustomAccessLevelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCustomAccessLevelResponse from a JSON string
resource_custom_access_level_response_instance = ResourceCustomAccessLevelResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceCustomAccessLevelResponse.to_json())

# convert the object into a dict
resource_custom_access_level_response_dict = resource_custom_access_level_response_instance.to_dict()
# create an instance of ResourceCustomAccessLevelResponse from a dict
resource_custom_access_level_response_from_dict = ResourceCustomAccessLevelResponse.from_dict(resource_custom_access_level_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


