# AddGroupResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level_remote_id** | **str** | The remote ID of the access level to grant to this user. If omitted, the default access level remote ID value (empty string) is used. | [optional] 
**duration_minutes** | **int** | The duration for which the resource can be accessed (in minutes). Use 0 to set to indefinite. | [optional] 

## Example

```python
from opal_security.models.add_group_resource_request import AddGroupResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddGroupResourceRequest from a JSON string
add_group_resource_request_instance = AddGroupResourceRequest.from_json(json)
# print the JSON string representation of the object
print(AddGroupResourceRequest.to_json())

# convert the object into a dict
add_group_resource_request_dict = add_group_resource_request_instance.to_dict()
# create an instance of AddGroupResourceRequest from a dict
add_group_resource_request_from_dict = AddGroupResourceRequest.from_dict(add_group_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


