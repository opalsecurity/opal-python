# AddBundleGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the group to add. | 
**access_level_remote_id** | **str** | The remote ID of the access level to grant to this user. Required if the group being added requires an access level. If omitted, the default access level remote ID value (empty string) is used. | [optional] 
**access_level_name** | **str** | The name of the access level to grant to this user. If omitted, the default access level name value (empty string) is used. | [optional] 

## Example

```python
from opal_security.models.add_bundle_group_request import AddBundleGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddBundleGroupRequest from a JSON string
add_bundle_group_request_instance = AddBundleGroupRequest.from_json(json)
# print the JSON string representation of the object
print(AddBundleGroupRequest.to_json())

# convert the object into a dict
add_bundle_group_request_dict = add_bundle_group_request_instance.to_dict()
# create an instance of AddBundleGroupRequest from a dict
add_bundle_group_request_from_dict = AddBundleGroupRequest.from_dict(add_bundle_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


