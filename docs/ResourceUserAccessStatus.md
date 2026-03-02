# ResourceUserAccessStatus

# AccessStatus Object ### Description The `AccessStatus` object is used to represent the user's access to the resource.  ### Usage Example View the `AccessStatus` for a resource/user pair to determine if the user has access to the resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource. | 
**user_id** | **str** | The ID of the user. | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | [optional] 
**status** | [**ResourceUserAccessStatusEnum**](ResourceUserAccessStatusEnum.md) |  | 
**expiration_date** | **datetime** | The day and time the user&#39;s access will expire. | [optional] 

## Example

```python
from opal_security.models.resource_user_access_status import ResourceUserAccessStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceUserAccessStatus from a JSON string
resource_user_access_status_instance = ResourceUserAccessStatus.from_json(json)
# print the JSON string representation of the object
print(ResourceUserAccessStatus.to_json())

# convert the object into a dict
resource_user_access_status_dict = resource_user_access_status_instance.to_dict()
# create an instance of ResourceUserAccessStatus from a dict
resource_user_access_status_from_dict = ResourceUserAccessStatus.from_dict(resource_user_access_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


