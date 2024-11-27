# ResourceRemoteInfoGithubRepo

Remote info for GitHub repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_id** | **str** | The id of the repository. | [optional] 
**repo_name** | **str** | The name of the repository. | 

## Example

```python
from opal_security.models.resource_remote_info_github_repo import ResourceRemoteInfoGithubRepo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGithubRepo from a JSON string
resource_remote_info_github_repo_instance = ResourceRemoteInfoGithubRepo.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGithubRepo.to_json())

# convert the object into a dict
resource_remote_info_github_repo_dict = resource_remote_info_github_repo_instance.to_dict()
# create an instance of ResourceRemoteInfoGithubRepo from a dict
resource_remote_info_github_repo_from_dict = ResourceRemoteInfoGithubRepo.from_dict(resource_remote_info_github_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


