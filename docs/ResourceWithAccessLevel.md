# ResourceWithAccessLevel

Information about a resource and corresponding access level

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource. | 
**access_level_remote_id** | **str** | The ID of the resource. | [optional] 

## Example

```python
from opal_security.models.resource_with_access_level import ResourceWithAccessLevel

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceWithAccessLevel from a JSON string
resource_with_access_level_instance = ResourceWithAccessLevel.from_json(json)
# print the JSON string representation of the object
print(ResourceWithAccessLevel.to_json())

# convert the object into a dict
resource_with_access_level_dict = resource_with_access_level_instance.to_dict()
# create an instance of ResourceWithAccessLevel from a dict
resource_with_access_level_from_dict = ResourceWithAccessLevel.from_dict(resource_with_access_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


