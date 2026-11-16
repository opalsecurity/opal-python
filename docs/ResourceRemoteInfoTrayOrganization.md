# ResourceRemoteInfoTrayOrganization

Remote info for Tray Organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | The organization id of the Tray Organization. | 

## Example

```python
from opal_security.models.resource_remote_info_tray_organization import ResourceRemoteInfoTrayOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoTrayOrganization from a JSON string
resource_remote_info_tray_organization_instance = ResourceRemoteInfoTrayOrganization.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoTrayOrganization.to_json())

# convert the object into a dict
resource_remote_info_tray_organization_dict = resource_remote_info_tray_organization_instance.to_dict()
# create an instance of ResourceRemoteInfoTrayOrganization from a dict
resource_remote_info_tray_organization_from_dict = ResourceRemoteInfoTrayOrganization.from_dict(resource_remote_info_tray_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


