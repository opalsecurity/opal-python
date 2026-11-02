# AddRoleAssignmentInput

A single role assignment to create in a batch add request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** | The ID of the entity (resource or group) being accessed. | 
**entity_type** | [**EntityTypeEnum**](EntityTypeEnum.md) | The type of the entity being accessed. Must be &#x60;RESOURCE&#x60; or &#x60;GROUP&#x60;. | 
**principal_id** | **UUID** | The ID of the principal (user, group, or resource) being granted access. | 
**principal_type** | [**EntityTypeEnum**](EntityTypeEnum.md) | The type of the principal being granted access. Must be &#x60;RESOURCE&#x60;, &#x60;GROUP&#x60;, or &#x60;USER&#x60;. | 
**access_level_remote_id** | **str** | Remote ID of the access level to grant. Omit for entities that only have a single default access level. | [optional] 
**duration_minutes** | **int** | Duration of the grant in minutes. Omit or send &#x60;0&#x60; for an indefinite grant. | [optional] 

## Example

```python
from opal_security.models.add_role_assignment_input import AddRoleAssignmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of AddRoleAssignmentInput from a JSON string
add_role_assignment_input_instance = AddRoleAssignmentInput.from_json(json)
# print the JSON string representation of the object
print(AddRoleAssignmentInput.to_json())

# convert the object into a dict
add_role_assignment_input_dict = add_role_assignment_input_instance.to_dict()
# create an instance of AddRoleAssignmentInput from a dict
add_role_assignment_input_from_dict = AddRoleAssignmentInput.from_dict(add_role_assignment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


