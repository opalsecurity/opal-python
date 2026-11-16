# OpalAccessResultEdge

A single ACCESS result edge containing the matched access grant and its pagination cursor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | [**OpalAccessResultNode**](OpalAccessResultNode.md) |  | 
**cursor** | **str** | Opaque cursor for this grant, used for pagination. | 

## Example

```python
from opal_security.models.opal_access_result_edge import OpalAccessResultEdge

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessResultEdge from a JSON string
opal_access_result_edge_instance = OpalAccessResultEdge.from_json(json)
# print the JSON string representation of the object
print(OpalAccessResultEdge.to_json())

# convert the object into a dict
opal_access_result_edge_dict = opal_access_result_edge_instance.to_dict()
# create an instance of OpalAccessResultEdge from a dict
opal_access_result_edge_from_dict = OpalAccessResultEdge.from_dict(opal_access_result_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


