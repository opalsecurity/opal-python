# GroupRemoteInfoTailscaleGroup

Remote info for Tailscale group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Tailscale group. | 

## Example

```python
from opal_security.models.group_remote_info_tailscale_group import GroupRemoteInfoTailscaleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoTailscaleGroup from a JSON string
group_remote_info_tailscale_group_instance = GroupRemoteInfoTailscaleGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoTailscaleGroup.to_json())

# convert the object into a dict
group_remote_info_tailscale_group_dict = group_remote_info_tailscale_group_instance.to_dict()
# create an instance of GroupRemoteInfoTailscaleGroup from a dict
group_remote_info_tailscale_group_from_dict = GroupRemoteInfoTailscaleGroup.from_dict(group_remote_info_tailscale_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


