# ResourceRemoteInfoGithubOrg

Remote info for GitHub organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_name** | **str** | The name of the organization. | 

## Example

```python
from opal_security.models.resource_remote_info_github_org import ResourceRemoteInfoGithubOrg

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGithubOrg from a JSON string
resource_remote_info_github_org_instance = ResourceRemoteInfoGithubOrg.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGithubOrg.to_json())

# convert the object into a dict
resource_remote_info_github_org_dict = resource_remote_info_github_org_instance.to_dict()
# create an instance of ResourceRemoteInfoGithubOrg from a dict
resource_remote_info_github_org_from_dict = ResourceRemoteInfoGithubOrg.from_dict(resource_remote_info_github_org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


