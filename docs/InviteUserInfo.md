# InviteUserInfo

The information required to invite a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**role** | [**UserProductRoleEnum**](UserProductRoleEnum.md) |  | 

## Example

```python
from opal_security.models.invite_user_info import InviteUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUserInfo from a JSON string
invite_user_info_instance = InviteUserInfo.from_json(json)
# print the JSON string representation of the object
print(InviteUserInfo.to_json())

# convert the object into a dict
invite_user_info_dict = invite_user_info_instance.to_dict()
# create an instance of InviteUserInfo from a dict
invite_user_info_from_dict = InviteUserInfo.from_dict(invite_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


