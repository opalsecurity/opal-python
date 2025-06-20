# RequestConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges** | [**List[RequestEdge]**](RequestEdge.md) |  | 
**page_info** | [**PageInfo**](PageInfo.md) |  | 
**total_count** | **int** | The total number of items available | 

## Example

```python
from opal_security.models.request_connection import RequestConnection

# TODO update the JSON string below
json = "{}"
# create an instance of RequestConnection from a JSON string
request_connection_instance = RequestConnection.from_json(json)
# print the JSON string representation of the object
print(RequestConnection.to_json())

# convert the object into a dict
request_connection_dict = request_connection_instance.to_dict()
# create an instance of RequestConnection from a dict
request_connection_from_dict = RequestConnection.from_dict(request_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


