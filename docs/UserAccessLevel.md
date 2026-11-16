# UserAccessLevel

The level of access the user has to a resource or group. The \"default\" access level is an object whose fields are all empty strings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level_name** | **str** | The human-readable name of the access level. | 
**access_level_remote_id** | **str** | The machine-readable identifier of the access level. | 

## Example

```python
from opal_security.models.user_access_level import UserAccessLevel

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccessLevel from a JSON string
user_access_level_instance = UserAccessLevel.from_json(json)
# print the JSON string representation of the object
print(UserAccessLevel.to_json())

# convert the object into a dict
user_access_level_dict = user_access_level_instance.to_dict()
# create an instance of UserAccessLevel from a dict
user_access_level_from_dict = UserAccessLevel.from_dict(user_access_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


