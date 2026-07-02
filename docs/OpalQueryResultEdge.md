# OpalQueryResultEdge

A single result edge from an OpalQuery, containing the matched entity and its pagination cursor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | [**OpalQueryResultNode**](OpalQueryResultNode.md) |  | 
**cursor** | **str** | Opaque cursor for this entity, used for pagination. | 

## Example

```python
from opal_security.models.opal_query_result_edge import OpalQueryResultEdge

# TODO update the JSON string below
json = "{}"
# create an instance of OpalQueryResultEdge from a JSON string
opal_query_result_edge_instance = OpalQueryResultEdge.from_json(json)
# print the JSON string representation of the object
print(OpalQueryResultEdge.to_json())

# convert the object into a dict
opal_query_result_edge_dict = opal_query_result_edge_instance.to_dict()
# create an instance of OpalQueryResultEdge from a dict
opal_query_result_edge_from_dict = OpalQueryResultEdge.from_dict(opal_query_result_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


