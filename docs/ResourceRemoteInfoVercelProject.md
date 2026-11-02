# ResourceRemoteInfoVercelProject

Remote info for Vercel project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The Vercel project id. | 

## Example

```python
from opal_security.models.resource_remote_info_vercel_project import ResourceRemoteInfoVercelProject

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoVercelProject from a JSON string
resource_remote_info_vercel_project_instance = ResourceRemoteInfoVercelProject.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoVercelProject.to_json())

# convert the object into a dict
resource_remote_info_vercel_project_dict = resource_remote_info_vercel_project_instance.to_dict()
# create an instance of ResourceRemoteInfoVercelProject from a dict
resource_remote_info_vercel_project_from_dict = ResourceRemoteInfoVercelProject.from_dict(resource_remote_info_vercel_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


