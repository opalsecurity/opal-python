# RemoveRoleAssignmentsEntry

A single revoked role assignment in a `RemoveRoleAssignmentsResponse`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_assignment** | [**RoleAssignment**](RoleAssignment.md) |  | 

## Example

```python
from opal_security.models.remove_role_assignments_entry import RemoveRoleAssignmentsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveRoleAssignmentsEntry from a JSON string
remove_role_assignments_entry_instance = RemoveRoleAssignmentsEntry.from_json(json)
# print the JSON string representation of the object
print(RemoveRoleAssignmentsEntry.to_json())

# convert the object into a dict
remove_role_assignments_entry_dict = remove_role_assignments_entry_instance.to_dict()
# create an instance of RemoveRoleAssignmentsEntry from a dict
remove_role_assignments_entry_from_dict = RemoveRoleAssignmentsEntry.from_dict(remove_role_assignments_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


