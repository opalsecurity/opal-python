# RemoveRoleAssignmentsResponse

Response body for `DELETE /role-assignments`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_ids** | **List[str]** | Opaque identifiers for the push tasks enqueued to propagate the revocation to the end system. Encoded identically to the &#x60;PushTaskId&#x60; scalar in the GraphQL API (base64 of the underlying protobuf). One ID per deferred revocation (today, resource/user grants are always deferred); empty when every revocation completed inline (resource/group, group/user, group/group). | 
**entries** | [**List[RemoveRoleAssignmentsEntry]**](RemoveRoleAssignmentsEntry.md) | One entry per role assignment that was removed inline. Shorter than the request when some assignments did not exist (idempotent), and empty when every revocation in the batch was deferred to an async propagation task — in that case &#x60;task_ids&#x60; carries one ID per deferred revocation and &#x60;entries&#x60; is empty. Resource/user grants are currently always deferred; the other &#x60;(entity, principal)&#x60; combinations complete inline and populate &#x60;entries&#x60;. | 

## Example

```python
from opal_security.models.remove_role_assignments_response import RemoveRoleAssignmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveRoleAssignmentsResponse from a JSON string
remove_role_assignments_response_instance = RemoveRoleAssignmentsResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveRoleAssignmentsResponse.to_json())

# convert the object into a dict
remove_role_assignments_response_dict = remove_role_assignments_response_instance.to_dict()
# create an instance of RemoveRoleAssignmentsResponse from a dict
remove_role_assignments_response_from_dict = RemoveRoleAssignmentsResponse.from_dict(remove_role_assignments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


