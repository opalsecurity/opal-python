# OpalAccessPathResultEdge

A single ACCESS_PATH result edge containing the matched path and its pagination cursor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | [**OpalAccessPathResultNode**](OpalAccessPathResultNode.md) |  | 
**cursor** | **str** | Opaque cursor for this path, used for pagination. | 

## Example

```python
from opal_security.models.opal_access_path_result_edge import OpalAccessPathResultEdge

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessPathResultEdge from a JSON string
opal_access_path_result_edge_instance = OpalAccessPathResultEdge.from_json(json)
# print the JSON string representation of the object
print(OpalAccessPathResultEdge.to_json())

# convert the object into a dict
opal_access_path_result_edge_dict = opal_access_path_result_edge_instance.to_dict()
# create an instance of OpalAccessPathResultEdge from a dict
opal_access_path_result_edge_from_dict = OpalAccessPathResultEdge.from_dict(opal_access_path_result_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


