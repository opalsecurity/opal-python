# GroupRemoteInfoRampLocation

Remote info for Ramp location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** | The ID of the Ramp location. | 

## Example

```python
from opal_security.models.group_remote_info_ramp_location import GroupRemoteInfoRampLocation

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoRampLocation from a JSON string
group_remote_info_ramp_location_instance = GroupRemoteInfoRampLocation.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoRampLocation.to_json())

# convert the object into a dict
group_remote_info_ramp_location_dict = group_remote_info_ramp_location_instance.to_dict()
# create an instance of GroupRemoteInfoRampLocation from a dict
group_remote_info_ramp_location_from_dict = GroupRemoteInfoRampLocation.from_dict(group_remote_info_ramp_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


