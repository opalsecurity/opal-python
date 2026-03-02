# ResourceNHI

# Resource Non-Human Identity Direct Access Object ### Description This object is used to represent a non-human identity with direct access to a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource. | 
**non_human_identity_id** | **str** | The resource ID of the non-human identity. | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | [optional] 
**expiration_date** | **datetime** | The day and time the non-human identity&#39;s access will expire. | [optional] 

## Example

```python
from opal_security.models.resource_nhi import ResourceNHI

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceNHI from a JSON string
resource_nhi_instance = ResourceNHI.from_json(json)
# print the JSON string representation of the object
print(ResourceNHI.to_json())

# convert the object into a dict
resource_nhi_dict = resource_nhi_instance.to_dict()
# create an instance of ResourceNHI from a dict
resource_nhi_from_dict = ResourceNHI.from_dict(resource_nhi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


