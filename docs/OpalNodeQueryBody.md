# OpalNodeQueryBody

The filter body for a NODE-type OpalQuery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_filters** | [**AccessEntityFilters**](AccessEntityFilters.md) |  | [optional] 
**access_filters** | [**AccessRelationshipFilters**](AccessRelationshipFilters.md) |  | [optional] 

## Example

```python
from opal_security.models.opal_node_query_body import OpalNodeQueryBody

# TODO update the JSON string below
json = "{}"
# create an instance of OpalNodeQueryBody from a JSON string
opal_node_query_body_instance = OpalNodeQueryBody.from_json(json)
# print the JSON string representation of the object
print(OpalNodeQueryBody.to_json())

# convert the object into a dict
opal_node_query_body_dict = opal_node_query_body_instance.to_dict()
# create an instance of OpalNodeQueryBody from a dict
opal_node_query_body_from_dict = OpalNodeQueryBody.from_dict(opal_node_query_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


