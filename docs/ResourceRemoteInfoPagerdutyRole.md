# ResourceRemoteInfoPagerdutyRole

Remote info for Pagerduty role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | The name of the role. | 

## Example

```python
from opal_security.models.resource_remote_info_pagerduty_role import ResourceRemoteInfoPagerdutyRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoPagerdutyRole from a JSON string
resource_remote_info_pagerduty_role_instance = ResourceRemoteInfoPagerdutyRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoPagerdutyRole.to_json())

# convert the object into a dict
resource_remote_info_pagerduty_role_dict = resource_remote_info_pagerduty_role_instance.to_dict()
# create an instance of ResourceRemoteInfoPagerdutyRole from a dict
resource_remote_info_pagerduty_role_from_dict = ResourceRemoteInfoPagerdutyRole.from_dict(resource_remote_info_pagerduty_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


