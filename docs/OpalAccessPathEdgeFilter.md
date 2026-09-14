# OpalAccessPathEdgeFilter

Constraints on the access path edges themselves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_only** | **bool** | When true, only return direct (depth-1) principal-to-entitlement edges. | [optional] 
**access_duration_type** | **str** | Constrain results by whether the terminal access expires. | [optional] 

## Example

```python
from opal_security.models.opal_access_path_edge_filter import OpalAccessPathEdgeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessPathEdgeFilter from a JSON string
opal_access_path_edge_filter_instance = OpalAccessPathEdgeFilter.from_json(json)
# print the JSON string representation of the object
print(OpalAccessPathEdgeFilter.to_json())

# convert the object into a dict
opal_access_path_edge_filter_dict = opal_access_path_edge_filter_instance.to_dict()
# create an instance of OpalAccessPathEdgeFilter from a dict
opal_access_path_edge_filter_from_dict = OpalAccessPathEdgeFilter.from_dict(opal_access_path_edge_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


