# ResourceRemoteInfoTwingateResource

Remote info for Twingate resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The id of the Twingate resource. | 

## Example

```python
from opal_security.models.resource_remote_info_twingate_resource import ResourceRemoteInfoTwingateResource

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoTwingateResource from a JSON string
resource_remote_info_twingate_resource_instance = ResourceRemoteInfoTwingateResource.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoTwingateResource.to_json())

# convert the object into a dict
resource_remote_info_twingate_resource_dict = resource_remote_info_twingate_resource_instance.to_dict()
# create an instance of ResourceRemoteInfoTwingateResource from a dict
resource_remote_info_twingate_resource_from_dict = ResourceRemoteInfoTwingateResource.from_dict(resource_remote_info_twingate_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


