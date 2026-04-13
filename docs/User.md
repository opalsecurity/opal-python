# User

# User Object ### Description The `User` object is used to represent a user.  ### Usage Example Fetch from the `LIST Sessions` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The ID of the user. | 
**email** | **str** | The email of the user. | 
**full_name** | **str** | The full name of the user. | 
**first_name** | **str** | The first name of the user. | 
**last_name** | **str** | The last name of the user. | 
**position** | **str** | The user&#39;s position. | 
**hr_idp_status** | [**UserHrIdpStatusEnum**](UserHrIdpStatusEnum.md) |  | [optional] 

## Example

```python
from opal_security.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


