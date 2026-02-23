# ResourceRemoteInfoTailscaleSsh

Remote info for Tailscale SSH tag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_name** | **str** | The name of the tag. | 

## Example

```python
from opal_security.models.resource_remote_info_tailscale_ssh import ResourceRemoteInfoTailscaleSsh

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoTailscaleSsh from a JSON string
resource_remote_info_tailscale_ssh_instance = ResourceRemoteInfoTailscaleSsh.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoTailscaleSsh.to_json())

# convert the object into a dict
resource_remote_info_tailscale_ssh_dict = resource_remote_info_tailscale_ssh_instance.to_dict()
# create an instance of ResourceRemoteInfoTailscaleSsh from a dict
resource_remote_info_tailscale_ssh_from_dict = ResourceRemoteInfoTailscaleSsh.from_dict(resource_remote_info_tailscale_ssh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


