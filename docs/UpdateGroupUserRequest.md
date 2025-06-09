# UpdateGroupUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_minutes** | **int** | The updated duration for which the group can be accessed (in minutes). Use 0 for indefinite. | 
**access_level_remote_id** | **str** | The updated remote ID of the access level granted to this user. | [optional] 

## Example

```python
from opal_security.models.update_group_user_request import UpdateGroupUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupUserRequest from a JSON string
update_group_user_request_instance = UpdateGroupUserRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupUserRequest.to_json())

# convert the object into a dict
update_group_user_request_dict = update_group_user_request_instance.to_dict()
# create an instance of UpdateGroupUserRequest from a dict
update_group_user_request_from_dict = UpdateGroupUserRequest.from_dict(update_group_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


