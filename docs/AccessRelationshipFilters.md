# AccessRelationshipFilters

Filters the returned nodes by the access edges connected to them. When `isAccessibleBy` and `hasAccessTo` are provided, the returned nodes must satisfy both edge constraints simultaneously. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_accessible_by** | [**AccessEntityFilters**](AccessEntityFilters.md) | Inbound-edge filter. The returned node must be accessible by at least one entity matching this filter. | [optional] 
**has_access_to** | [**AccessEntityFilters**](AccessEntityFilters.md) | Outbound-edge filter. The returned node must have access to at least one entity matching this filter. | [optional] 

## Example

```python
from opal_security.models.access_relationship_filters import AccessRelationshipFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRelationshipFilters from a JSON string
access_relationship_filters_instance = AccessRelationshipFilters.from_json(json)
# print the JSON string representation of the object
print(AccessRelationshipFilters.to_json())

# convert the object into a dict
access_relationship_filters_dict = access_relationship_filters_instance.to_dict()
# create an instance of AccessRelationshipFilters from a dict
access_relationship_filters_from_dict = AccessRelationshipFilters.from_dict(access_relationship_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


