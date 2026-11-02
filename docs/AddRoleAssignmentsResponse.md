# AddRoleAssignmentsResponse

Response body for `POST /role-assignments`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_ids** | **List[str]** | Opaque IDs of push tasks enqueued to propagate the new assignments to end systems. Each ID is a base64-encoded, URL-safe string that mirrors the identifier returned by the GraphQL &#x60;addRoleAssignments&#x60; mutation. | 
**entries** | [**List[AddRoleAssignmentsEntry]**](AddRoleAssignmentsEntry.md) | One entry per role assignment created, in request order. | 

## Example

```python
from opal_security.models.add_role_assignments_response import AddRoleAssignmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddRoleAssignmentsResponse from a JSON string
add_role_assignments_response_instance = AddRoleAssignmentsResponse.from_json(json)
# print the JSON string representation of the object
print(AddRoleAssignmentsResponse.to_json())

# convert the object into a dict
add_role_assignments_response_dict = add_role_assignments_response_instance.to_dict()
# create an instance of AddRoleAssignmentsResponse from a dict
add_role_assignments_response_from_dict = AddRoleAssignmentsResponse.from_dict(add_role_assignments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


