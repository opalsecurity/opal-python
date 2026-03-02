# ResourceUser

# Resource User Object ### Description The `ResourceUser` object is used to represent a user with direct access to a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource. | 
**user_id** | **str** | The ID of the user. | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | 
**full_name** | **str** | The user&#39;s full name. | 
**email** | **str** | The user&#39;s email. | 
**expiration_date** | **datetime** | The day and time the user&#39;s access will expire. | [optional] 

## Example

```python
from opal_security.models.resource_user import ResourceUser

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceUser from a JSON string
resource_user_instance = ResourceUser.from_json(json)
# print the JSON string representation of the object
print(ResourceUser.to_json())

# convert the object into a dict
resource_user_dict = resource_user_instance.to_dict()
# create an instance of ResourceUser from a dict
resource_user_from_dict = ResourceUser.from_dict(resource_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


