# ResourceRemoteInfoAlicloudRamRole

Remote info for AliCloud RAM role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_arn** | **str** | The ARN of the AliCloud RAM role. | 

## Example

```python
from opal_security.models.resource_remote_info_alicloud_ram_role import ResourceRemoteInfoAlicloudRamRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAlicloudRamRole from a JSON string
resource_remote_info_alicloud_ram_role_instance = ResourceRemoteInfoAlicloudRamRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAlicloudRamRole.to_json())

# convert the object into a dict
resource_remote_info_alicloud_ram_role_dict = resource_remote_info_alicloud_ram_role_instance.to_dict()
# create an instance of ResourceRemoteInfoAlicloudRamRole from a dict
resource_remote_info_alicloud_ram_role_from_dict = ResourceRemoteInfoAlicloudRamRole.from_dict(resource_remote_info_alicloud_ram_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


