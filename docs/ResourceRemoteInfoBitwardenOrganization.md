# ResourceRemoteInfoBitwardenOrganization

Remote info for Bitwarden Organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | The organization id of the Bitwarden Organization. | 

## Example

```python
from opal_security.models.resource_remote_info_bitwarden_organization import ResourceRemoteInfoBitwardenOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoBitwardenOrganization from a JSON string
resource_remote_info_bitwarden_organization_instance = ResourceRemoteInfoBitwardenOrganization.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoBitwardenOrganization.to_json())

# convert the object into a dict
resource_remote_info_bitwarden_organization_dict = resource_remote_info_bitwarden_organization_instance.to_dict()
# create an instance of ResourceRemoteInfoBitwardenOrganization from a dict
resource_remote_info_bitwarden_organization_from_dict = ResourceRemoteInfoBitwardenOrganization.from_dict(resource_remote_info_bitwarden_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


