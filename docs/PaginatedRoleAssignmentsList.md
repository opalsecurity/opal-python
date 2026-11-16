# PaginatedRoleAssignmentsList

A paginated page of role assignments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[RoleAssignment]**](RoleAssignment.md) |  | 

## Example

```python
from opal_security.models.paginated_role_assignments_list import PaginatedRoleAssignmentsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRoleAssignmentsList from a JSON string
paginated_role_assignments_list_instance = PaginatedRoleAssignmentsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRoleAssignmentsList.to_json())

# convert the object into a dict
paginated_role_assignments_list_dict = paginated_role_assignments_list_instance.to_dict()
# create an instance of PaginatedRoleAssignmentsList from a dict
paginated_role_assignments_list_from_dict = PaginatedRoleAssignmentsList.from_dict(paginated_role_assignments_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


