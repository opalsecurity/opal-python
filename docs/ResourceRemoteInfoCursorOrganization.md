# ResourceRemoteInfoCursorOrganization

Remote info for a Cursor organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | The id of the organization. | 

## Example

```python
from opal_security.models.resource_remote_info_cursor_organization import ResourceRemoteInfoCursorOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoCursorOrganization from a JSON string
resource_remote_info_cursor_organization_instance = ResourceRemoteInfoCursorOrganization.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoCursorOrganization.to_json())

# convert the object into a dict
resource_remote_info_cursor_organization_dict = resource_remote_info_cursor_organization_instance.to_dict()
# create an instance of ResourceRemoteInfoCursorOrganization from a dict
resource_remote_info_cursor_organization_from_dict = ResourceRemoteInfoCursorOrganization.from_dict(resource_remote_info_cursor_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


