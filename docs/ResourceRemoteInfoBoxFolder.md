# ResourceRemoteInfoBoxFolder

Remote info for Box Folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The resource id of the Box Folder. | 

## Example

```python
from opal_security.models.resource_remote_info_box_folder import ResourceRemoteInfoBoxFolder

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoBoxFolder from a JSON string
resource_remote_info_box_folder_instance = ResourceRemoteInfoBoxFolder.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoBoxFolder.to_json())

# convert the object into a dict
resource_remote_info_box_folder_dict = resource_remote_info_box_folder_instance.to_dict()
# create an instance of ResourceRemoteInfoBoxFolder from a dict
resource_remote_info_box_folder_from_dict = ResourceRemoteInfoBoxFolder.from_dict(resource_remote_info_box_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


