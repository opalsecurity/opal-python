# ResourceRemoteInfoAlicloudEcsInstance

Remote info for AliCloud ECS instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | The ID of the ECS instance. | 

## Example

```python
from opal_security.models.resource_remote_info_alicloud_ecs_instance import ResourceRemoteInfoAlicloudEcsInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAlicloudEcsInstance from a JSON string
resource_remote_info_alicloud_ecs_instance_instance = ResourceRemoteInfoAlicloudEcsInstance.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAlicloudEcsInstance.to_json())

# convert the object into a dict
resource_remote_info_alicloud_ecs_instance_dict = resource_remote_info_alicloud_ecs_instance_instance.to_dict()
# create an instance of ResourceRemoteInfoAlicloudEcsInstance from a dict
resource_remote_info_alicloud_ecs_instance_from_dict = ResourceRemoteInfoAlicloudEcsInstance.from_dict(resource_remote_info_alicloud_ecs_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


