# ResourceAccessLevel

# Access Level Object ### Description The `AccessLevel` object is used to represent the level of access that a principal has. The \"default\" access level is a `AccessLevel` object whose fields are all empty strings.  ### Usage Example View the `AccessLevel` of a resource/user or resource/group pair to see the level of access granted to the resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level_name** | **str** | The human-readable name of the access level. | 
**access_level_remote_id** | **str** | The machine-readable identifier of the access level. | 

## Example

```python
from opal_security.models.resource_access_level import ResourceAccessLevel

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAccessLevel from a JSON string
resource_access_level_instance = ResourceAccessLevel.from_json(json)
# print the JSON string representation of the object
print(ResourceAccessLevel.to_json())

# convert the object into a dict
resource_access_level_dict = resource_access_level_instance.to_dict()
# create an instance of ResourceAccessLevel from a dict
resource_access_level_from_dict = ResourceAccessLevel.from_dict(resource_access_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


