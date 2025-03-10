# GroupUser

# Group Access User Object ### Description The `GroupAccessUser` object is used to represent a user with access to a group.  ### Usage Example Fetch from the `LIST GroupUsers` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the group. | 
**user_id** | **str** | The ID of the user. | 
**access_level** | [**GroupAccessLevel**](GroupAccessLevel.md) |  | [optional] 
**full_name** | **str** | The user&#39;s full name. | 
**email** | **str** | The user&#39;s email. | 
**expiration_date** | **datetime** | The day and time the user&#39;s access will expire. | [optional] 
**propagation_status** | [**PropagationStatus**](PropagationStatus.md) |  | [optional] 

## Example

```python
from opal_security.models.group_user import GroupUser

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUser from a JSON string
group_user_instance = GroupUser.from_json(json)
# print the JSON string representation of the object
print(GroupUser.to_json())

# convert the object into a dict
group_user_dict = group_user_instance.to_dict()
# create an instance of GroupUser from a dict
group_user_from_dict = GroupUser.from_dict(group_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


