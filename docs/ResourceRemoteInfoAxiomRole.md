# ResourceRemoteInfoAxiomRole

Remote info for Axiom base role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The ID of the Axiom base role. | 

## Example

```python
from opal_security.models.resource_remote_info_axiom_role import ResourceRemoteInfoAxiomRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAxiomRole from a JSON string
resource_remote_info_axiom_role_instance = ResourceRemoteInfoAxiomRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAxiomRole.to_json())

# convert the object into a dict
resource_remote_info_axiom_role_dict = resource_remote_info_axiom_role_instance.to_dict()
# create an instance of ResourceRemoteInfoAxiomRole from a dict
resource_remote_info_axiom_role_from_dict = ResourceRemoteInfoAxiomRole.from_dict(resource_remote_info_axiom_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


