# ResourceRemoteInfoOpenaiPlatformProject

Remote info for OpenAI Platform project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The id of the project. | 

## Example

```python
from opal_security.models.resource_remote_info_openai_platform_project import ResourceRemoteInfoOpenaiPlatformProject

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoOpenaiPlatformProject from a JSON string
resource_remote_info_openai_platform_project_instance = ResourceRemoteInfoOpenaiPlatformProject.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoOpenaiPlatformProject.to_json())

# convert the object into a dict
resource_remote_info_openai_platform_project_dict = resource_remote_info_openai_platform_project_instance.to_dict()
# create an instance of ResourceRemoteInfoOpenaiPlatformProject from a dict
resource_remote_info_openai_platform_project_from_dict = ResourceRemoteInfoOpenaiPlatformProject.from_dict(resource_remote_info_openai_platform_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


