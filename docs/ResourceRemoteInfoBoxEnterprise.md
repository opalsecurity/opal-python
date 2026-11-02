# ResourceRemoteInfoBoxEnterprise

Remote info for Box Enterprise.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The resource id of the Box Enterprise. | 

## Example

```python
from opal_security.models.resource_remote_info_box_enterprise import ResourceRemoteInfoBoxEnterprise

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoBoxEnterprise from a JSON string
resource_remote_info_box_enterprise_instance = ResourceRemoteInfoBoxEnterprise.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoBoxEnterprise.to_json())

# convert the object into a dict
resource_remote_info_box_enterprise_dict = resource_remote_info_box_enterprise_instance.to_dict()
# create an instance of ResourceRemoteInfoBoxEnterprise from a dict
resource_remote_info_box_enterprise_from_dict = ResourceRemoteInfoBoxEnterprise.from_dict(resource_remote_info_box_enterprise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


