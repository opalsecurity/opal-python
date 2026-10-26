# AddRoleAssignmentsEntry

A single entry in the result of `POST /role-assignments`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_assignment** | [**RoleAssignment**](RoleAssignment.md) |  | 

## Example

```python
from opal_security.models.add_role_assignments_entry import AddRoleAssignmentsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AddRoleAssignmentsEntry from a JSON string
add_role_assignments_entry_instance = AddRoleAssignmentsEntry.from_json(json)
# print the JSON string representation of the object
print(AddRoleAssignmentsEntry.to_json())

# convert the object into a dict
add_role_assignments_entry_dict = add_role_assignments_entry_instance.to_dict()
# create an instance of AddRoleAssignmentsEntry from a dict
add_role_assignments_entry_from_dict = AddRoleAssignmentsEntry.from_dict(add_role_assignments_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


