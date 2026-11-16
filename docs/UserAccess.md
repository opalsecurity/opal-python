# UserAccess

# User Access Object ### Description The `UserAccess` object represents a user's access to a single resource or group at one access level, either directly or indirectly (for example, through group membership).  ### Usage Example Fetch from the `GET /users/{user_id}/access` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | [**UserAccessEntityTypeEnum**](UserAccessEntityTypeEnum.md) |  | 
**entity_id** | **UUID** | The ID of the resource or group. | 
**entity_name** | **str** | The name of the resource or group. | 
**description** | **str** | The description of the resource or group. | 
**access_level** | [**UserAccessLevel**](UserAccessLevel.md) |  | 
**expiration_date** | **datetime** | The day and time the user&#39;s access will expire. If the user has more than one way to access the entity, this is the latest expiration. Null if the access does not expire. | [optional] 
**has_direct_access** | **bool** | The user has direct access to this entity (vs. indirectly, like through a group). | 
**num_access_paths** | **int** | The number of ways in which the user has access to this entity (directly and indirectly). | 
**propagation_status** | [**PropagationStatus**](PropagationStatus.md) |  | [optional] 

## Example

```python
from opal_security.models.user_access import UserAccess

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccess from a JSON string
user_access_instance = UserAccess.from_json(json)
# print the JSON string representation of the object
print(UserAccess.to_json())

# convert the object into a dict
user_access_dict = user_access_instance.to_dict()
# create an instance of UserAccess from a dict
user_access_from_dict = UserAccess.from_dict(user_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


