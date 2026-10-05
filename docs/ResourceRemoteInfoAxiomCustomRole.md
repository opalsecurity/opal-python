# ResourceRemoteInfoAxiomCustomRole

Remote info for Axiom custom RBAC role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The ID of the Axiom custom role. | 

## Example

```python
from opal_security.models.resource_remote_info_axiom_custom_role import ResourceRemoteInfoAxiomCustomRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAxiomCustomRole from a JSON string
resource_remote_info_axiom_custom_role_instance = ResourceRemoteInfoAxiomCustomRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAxiomCustomRole.to_json())

# convert the object into a dict
resource_remote_info_axiom_custom_role_dict = resource_remote_info_axiom_custom_role_instance.to_dict()
# create an instance of ResourceRemoteInfoAxiomCustomRole from a dict
resource_remote_info_axiom_custom_role_from_dict = ResourceRemoteInfoAxiomCustomRole.from_dict(resource_remote_info_axiom_custom_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


