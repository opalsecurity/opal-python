# RemoveRoleAssignmentsRequest

Request body for `DELETE /role-assignments`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_assignments** | [**List[RemoveRoleAssignmentInput]**](RemoveRoleAssignmentInput.md) |  | 

## Example

```python
from opal_security.models.remove_role_assignments_request import RemoveRoleAssignmentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveRoleAssignmentsRequest from a JSON string
remove_role_assignments_request_instance = RemoveRoleAssignmentsRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveRoleAssignmentsRequest.to_json())

# convert the object into a dict
remove_role_assignments_request_dict = remove_role_assignments_request_instance.to_dict()
# create an instance of RemoveRoleAssignmentsRequest from a dict
remove_role_assignments_request_from_dict = RemoveRoleAssignmentsRequest.from_dict(remove_role_assignments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


