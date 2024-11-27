# ResourceRemoteInfoGitlabProject

Remote info for Gitlab project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The id of the project. | 

## Example

```python
from opal_security.models.resource_remote_info_gitlab_project import ResourceRemoteInfoGitlabProject

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGitlabProject from a JSON string
resource_remote_info_gitlab_project_instance = ResourceRemoteInfoGitlabProject.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGitlabProject.to_json())

# convert the object into a dict
resource_remote_info_gitlab_project_dict = resource_remote_info_gitlab_project_instance.to_dict()
# create an instance of ResourceRemoteInfoGitlabProject from a dict
resource_remote_info_gitlab_project_from_dict = ResourceRemoteInfoGitlabProject.from_dict(resource_remote_info_gitlab_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


