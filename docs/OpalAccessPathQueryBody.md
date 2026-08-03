# OpalAccessPathQueryBody

Edge-query filters for an ACCESS_PATH OpalQuery. At least one of principalFilter or entitlementFilter is required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_filter** | [**AccessEntityFilters**](AccessEntityFilters.md) |  | [optional] 
**entitlement_filter** | [**AccessEntityFilters**](AccessEntityFilters.md) |  | [optional] 
**principal_access_filters** | [**AccessRelationshipFilters**](AccessRelationshipFilters.md) | Advanced access filter on the principal side of each path. Restricts results to principals that additionally satisfy these access-edge constraints: &#x60;hasAccessTo&#x60; keeps only principals that also have access to a matching entity; &#x60;isAccessibleBy&#x60; keeps only principals that are also accessible by a matching entity. Only takes effect when &#x60;principalFilter&#x60; is also supplied (it refines that filter); on its own it has no effect.  | [optional] 
**entitlement_access_filters** | [**AccessRelationshipFilters**](AccessRelationshipFilters.md) | Advanced access filter on the entitlement side of each path. Restricts results to entitlements that additionally satisfy these access-edge constraints: &#x60;hasAccessTo&#x60; keeps only entitlements that also have access to a matching entity; &#x60;isAccessibleBy&#x60; keeps only entitlements that are also accessible by a matching entity. Only takes effect when &#x60;entitlementFilter&#x60; is also supplied (it refines that filter); on its own it has no effect.  | [optional] 
**access_level_remote_ids** | **List[str]** | Filter by access-level remote IDs on the terminal edge. | [optional] 
**access_level_names** | **List[str]** | Filter by access-level display names on the terminal edge. | [optional] 
**edge_filter** | [**OpalAccessPathEdgeFilter**](OpalAccessPathEdgeFilter.md) |  | [optional] 

## Example

```python
from opal_security.models.opal_access_path_query_body import OpalAccessPathQueryBody

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessPathQueryBody from a JSON string
opal_access_path_query_body_instance = OpalAccessPathQueryBody.from_json(json)
# print the JSON string representation of the object
print(OpalAccessPathQueryBody.to_json())

# convert the object into a dict
opal_access_path_query_body_dict = opal_access_path_query_body_instance.to_dict()
# create an instance of OpalAccessPathQueryBody from a dict
opal_access_path_query_body_from_dict = OpalAccessPathQueryBody.from_dict(opal_access_path_query_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


