# ResourceAccessUser

# Resource Access User Object ### Description The `ResourceAccessUser` object is used to represent a user with access to a resource, either directly or indirectly through group(s).  ### Usage Example Fetch from the `LIST ResourceUsers` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource. | 
**user_id** | **str** | The ID of the user. | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | 
**full_name** | **str** | The user&#39;s full name. | 
**email** | **str** | The user&#39;s email. | 
**expiration_date** | **datetime** | The day and time the user&#39;s access will expire. | [optional] 
**has_direct_access** | **bool** | The user has direct access to this resources (vs. indirectly, like through a group). | 
**num_access_paths** | **int** | The number of ways in which the user has access through this resource (directly and indirectly). | 
**propagation_status** | [**PropagationStatus**](PropagationStatus.md) |  | [optional] 

## Example

```python
from opal_security.models.resource_access_user import ResourceAccessUser

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAccessUser from a JSON string
resource_access_user_instance = ResourceAccessUser.from_json(json)
# print the JSON string representation of the object
print(ResourceAccessUser.to_json())

# convert the object into a dict
resource_access_user_dict = resource_access_user_instance.to_dict()
# create an instance of ResourceAccessUser from a dict
resource_access_user_from_dict = ResourceAccessUser.from_dict(resource_access_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


