# ResourceRemoteInfoDatastaxAstraRole

Remote info for an Astra role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The id of the role. | 

## Example

```python
from opal_security.models.resource_remote_info_datastax_astra_role import ResourceRemoteInfoDatastaxAstraRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoDatastaxAstraRole from a JSON string
resource_remote_info_datastax_astra_role_instance = ResourceRemoteInfoDatastaxAstraRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoDatastaxAstraRole.to_json())

# convert the object into a dict
resource_remote_info_datastax_astra_role_dict = resource_remote_info_datastax_astra_role_instance.to_dict()
# create an instance of ResourceRemoteInfoDatastaxAstraRole from a dict
resource_remote_info_datastax_astra_role_from_dict = ResourceRemoteInfoDatastaxAstraRole.from_dict(resource_remote_info_datastax_astra_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


