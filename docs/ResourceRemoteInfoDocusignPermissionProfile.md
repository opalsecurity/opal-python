# ResourceRemoteInfoDocusignPermissionProfile

Remote info for Docusign permission profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_profile_id** | **str** | The ID of the Docusign permission profile. | 

## Example

```python
from opal_security.models.resource_remote_info_docusign_permission_profile import ResourceRemoteInfoDocusignPermissionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoDocusignPermissionProfile from a JSON string
resource_remote_info_docusign_permission_profile_instance = ResourceRemoteInfoDocusignPermissionProfile.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoDocusignPermissionProfile.to_json())

# convert the object into a dict
resource_remote_info_docusign_permission_profile_dict = resource_remote_info_docusign_permission_profile_instance.to_dict()
# create an instance of ResourceRemoteInfoDocusignPermissionProfile from a dict
resource_remote_info_docusign_permission_profile_from_dict = ResourceRemoteInfoDocusignPermissionProfile.from_dict(resource_remote_info_docusign_permission_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


