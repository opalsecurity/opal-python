# RequestEdge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | [**Request**](Request.md) |  | 
**cursor** | **str** | The cursor for this request edge | 

## Example

```python
from opal_security.models.request_edge import RequestEdge

# TODO update the JSON string below
json = "{}"
# create an instance of RequestEdge from a JSON string
request_edge_instance = RequestEdge.from_json(json)
# print the JSON string representation of the object
print(RequestEdge.to_json())

# convert the object into a dict
request_edge_dict = request_edge_instance.to_dict()
# create an instance of RequestEdge from a dict
request_edge_from_dict = RequestEdge.from_dict(request_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


