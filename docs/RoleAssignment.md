# RoleAssignment

A role assignment representing access granted to a principal for an entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the role assignment. | 
**entity_id** | **UUID** | The ID of the entity (resource or group) being accessed. | 
**entity_type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**principal_id** | **UUID** | The ID of the principal being granted access. | 
**principal_type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) | The level of access granted. Null when the entity does not define access levels. | [optional] 
**expiration** | **datetime** | When this access expires. Null when the grant is indefinite. | [optional] 
**granted_at** | **datetime** | When this access was first granted. | [optional] 

## Example

```python
from opal_security.models.role_assignment import RoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssignment from a JSON string
role_assignment_instance = RoleAssignment.from_json(json)
# print the JSON string representation of the object
print(RoleAssignment.to_json())

# convert the object into a dict
role_assignment_dict = role_assignment_instance.to_dict()
# create an instance of RoleAssignment from a dict
role_assignment_from_dict = RoleAssignment.from_dict(role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


