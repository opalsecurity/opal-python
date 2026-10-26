# AddRoleAssignmentsRequest

Request body for `POST /role-assignments`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_assignments** | [**List[AddRoleAssignmentInput]**](AddRoleAssignmentInput.md) | The list of role assignments to add. | 

## Example

```python
from opal_security.models.add_role_assignments_request import AddRoleAssignmentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddRoleAssignmentsRequest from a JSON string
add_role_assignments_request_instance = AddRoleAssignmentsRequest.from_json(json)
# print the JSON string representation of the object
print(AddRoleAssignmentsRequest.to_json())

# convert the object into a dict
add_role_assignments_request_dict = add_role_assignments_request_instance.to_dict()
# create an instance of AddRoleAssignmentsRequest from a dict
add_role_assignments_request_from_dict = AddRoleAssignmentsRequest.from_dict(add_role_assignments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


