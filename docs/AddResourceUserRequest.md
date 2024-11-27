# AddResourceUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_minutes** | **int** | The duration for which the resource can be accessed (in minutes). Use 0 to set to indefinite. | 
**access_level_remote_id** | **str** | The remote ID of the access level to grant to this user. If omitted, the default access level remote ID value (empty string) is used. | [optional] 

## Example

```python
from opal_security.models.add_resource_user_request import AddResourceUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddResourceUserRequest from a JSON string
add_resource_user_request_instance = AddResourceUserRequest.from_json(json)
# print the JSON string representation of the object
print(AddResourceUserRequest.to_json())

# convert the object into a dict
add_resource_user_request_dict = add_resource_user_request_instance.to_dict()
# create an instance of AddResourceUserRequest from a dict
add_resource_user_request_from_dict = AddResourceUserRequest.from_dict(add_resource_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


