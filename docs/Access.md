# Access

# Access Object ### Description The `Access` object is used to represent a principal's access to an entity, either directly or inherited.  ### Usage Example Fetch from the `LIST ResourceNonHumanIdentities` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_id** | **str** | The ID of the principal with access. | 
**principal_type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**entity_id** | **str** | The ID of the entity being accessed. | 
**entity_type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) |  | [optional] 
**expiration_date** | **datetime** | The day and time the principal&#39;s access will expire. | [optional] 
**has_direct_access** | **bool** | The principal has direct access to this entity (vs. inherited access). | 
**num_access_paths** | **int** | The number of ways in which the principal has access to this entity (directly and inherited). | 

## Example

```python
from opal_security.models.access import Access

# TODO update the JSON string below
json = "{}"
# create an instance of Access from a JSON string
access_instance = Access.from_json(json)
# print the JSON string representation of the object
print(Access.to_json())

# convert the object into a dict
access_dict = access_instance.to_dict()
# create an instance of Access from a dict
access_from_dict = Access.from_dict(access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


