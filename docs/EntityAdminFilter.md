# EntityAdminFilter

Filters GROUP and RESOURCE entities by their admin owner. USER entities never match, in either polarity. `not` inverts the match within the resource/group domain (self-negating, like IdpStatusFilter): omit it (or false) to include entities owned by the given owners, set it true to exclude them. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_ids** | **List[UUID]** | The owner (group) UUIDs to match entities against. | 
**var_not** | **bool** | Invert the match — return resources/groups NOT owned by the given owners. | [optional] 

## Example

```python
from opal_security.models.entity_admin_filter import EntityAdminFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAdminFilter from a JSON string
entity_admin_filter_instance = EntityAdminFilter.from_json(json)
# print the JSON string representation of the object
print(EntityAdminFilter.to_json())

# convert the object into a dict
entity_admin_filter_dict = entity_admin_filter_instance.to_dict()
# create an instance of EntityAdminFilter from a dict
entity_admin_filter_from_dict = EntityAdminFilter.from_dict(entity_admin_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


