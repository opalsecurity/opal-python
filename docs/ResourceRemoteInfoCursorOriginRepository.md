# ResourceRemoteInfoCursorOriginRepository

Remote info for a Cursor Origin repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_name** | **str** | The repository&#39;s owner slug and name. | 

## Example

```python
from opal_security.models.resource_remote_info_cursor_origin_repository import ResourceRemoteInfoCursorOriginRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoCursorOriginRepository from a JSON string
resource_remote_info_cursor_origin_repository_instance = ResourceRemoteInfoCursorOriginRepository.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoCursorOriginRepository.to_json())

# convert the object into a dict
resource_remote_info_cursor_origin_repository_dict = resource_remote_info_cursor_origin_repository_instance.to_dict()
# create an instance of ResourceRemoteInfoCursorOriginRepository from a dict
resource_remote_info_cursor_origin_repository_from_dict = ResourceRemoteInfoCursorOriginRepository.from_dict(resource_remote_info_cursor_origin_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


