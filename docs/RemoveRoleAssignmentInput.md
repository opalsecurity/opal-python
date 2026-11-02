# RemoveRoleAssignmentInput

A single role assignment to revoke.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** | The ID of the entity (resource or group) to revoke access from. | 
**entity_type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**principal_id** | **UUID** | The ID of the principal (user, group, or resource) losing access. | 
**principal_type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**access_level_remote_id** | **str** | Remote ID of the specific access-level grant to revoke. The lookup is exact-match on this value against stored grants.  Required when the entity has access levels defined (the server returns 422 if omitted or sent as &#x60;null&#x60;/empty for such an entity). Must be omitted or &#x60;null&#x60; for entities with no access-level catalog (group memberships and resources that have no defined access levels); supplying a value in that case also returns 422. These rules mirror those of &#x60;POST /v1/role-assignments&#x60;.  A specified value that does not match any stored grant for this &#x60;(entity_id, principal_id)&#x60; pair is a successful idempotent no-op: HTTP 200 is returned and the entry is absent from &#x60;entries&#x60;.  | [optional] 

## Example

```python
from opal_security.models.remove_role_assignment_input import RemoveRoleAssignmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveRoleAssignmentInput from a JSON string
remove_role_assignment_input_instance = RemoveRoleAssignmentInput.from_json(json)
# print the JSON string representation of the object
print(RemoveRoleAssignmentInput.to_json())

# convert the object into a dict
remove_role_assignment_input_dict = remove_role_assignment_input_instance.to_dict()
# create an instance of RemoveRoleAssignmentInput from a dict
remove_role_assignment_input_from_dict = RemoveRoleAssignmentInput.from_dict(remove_role_assignment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


