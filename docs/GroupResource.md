# GroupResource

# GroupResource Object ### Description The `GroupResource` object is used to represent a relationship between a group and a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **UUID** | The ID of the group. | 
**resource_id** | **UUID** | The ID of the resource. | 
**group_name** | **str** | The name of the group | [optional] 
**resource_name** | **str** | The name of the resource | [optional] 
**expiration_date** | **datetime** | The day and time the group&#39;s access will expire. | [optional] 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | 

## Example

```python
from opal_security.models.group_resource import GroupResource

# TODO update the JSON string below
json = "{}"
# create an instance of GroupResource from a JSON string
group_resource_instance = GroupResource.from_json(json)
# print the JSON string representation of the object
print(GroupResource.to_json())

# convert the object into a dict
group_resource_dict = group_resource_instance.to_dict()
# create an instance of GroupResource from a dict
group_resource_from_dict = GroupResource.from_dict(group_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


