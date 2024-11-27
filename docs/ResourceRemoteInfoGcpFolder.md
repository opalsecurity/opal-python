# ResourceRemoteInfoGcpFolder

Remote info for GCP folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** | The id of the folder. | 

## Example

```python
from opal_security.models.resource_remote_info_gcp_folder import ResourceRemoteInfoGcpFolder

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGcpFolder from a JSON string
resource_remote_info_gcp_folder_instance = ResourceRemoteInfoGcpFolder.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGcpFolder.to_json())

# convert the object into a dict
resource_remote_info_gcp_folder_dict = resource_remote_info_gcp_folder_instance.to_dict()
# create an instance of ResourceRemoteInfoGcpFolder from a dict
resource_remote_info_gcp_folder_from_dict = ResourceRemoteInfoGcpFolder.from_dict(resource_remote_info_gcp_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


