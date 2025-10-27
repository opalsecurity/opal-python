# ResourceRemoteInfoOracleFusionRole

Remote info for Oracle Fusion role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The id of the role. | 

## Example

```python
from opal_security.models.resource_remote_info_oracle_fusion_role import ResourceRemoteInfoOracleFusionRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoOracleFusionRole from a JSON string
resource_remote_info_oracle_fusion_role_instance = ResourceRemoteInfoOracleFusionRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoOracleFusionRole.to_json())

# convert the object into a dict
resource_remote_info_oracle_fusion_role_dict = resource_remote_info_oracle_fusion_role_instance.to_dict()
# create an instance of ResourceRemoteInfoOracleFusionRole from a dict
resource_remote_info_oracle_fusion_role_from_dict = ResourceRemoteInfoOracleFusionRole.from_dict(resource_remote_info_oracle_fusion_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


