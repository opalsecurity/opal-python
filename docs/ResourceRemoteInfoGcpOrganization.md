# ResourceRemoteInfoGcpOrganization

Remote info for GCP organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | The id of the organization. | 

## Example

```python
from opal_security.models.resource_remote_info_gcp_organization import ResourceRemoteInfoGcpOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGcpOrganization from a JSON string
resource_remote_info_gcp_organization_instance = ResourceRemoteInfoGcpOrganization.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGcpOrganization.to_json())

# convert the object into a dict
resource_remote_info_gcp_organization_dict = resource_remote_info_gcp_organization_instance.to_dict()
# create an instance of ResourceRemoteInfoGcpOrganization from a dict
resource_remote_info_gcp_organization_from_dict = ResourceRemoteInfoGcpOrganization.from_dict(resource_remote_info_gcp_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


